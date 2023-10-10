from random import randint
from cell import Cell, GraphicCell
#from multiprocessing import Pool, JoinableQueue, Pipe
from PIL import Image, ImageTk
from graphics import Image as GraImage, Point


class Field:

    def __init__(self, field_width, field_height, initial_state=None, workers:int=1):
        self.width = field_width
        self.height = field_height
        self.field = self._build(initial_state)
        
        # Set up the worker processes
        self.worker_count = workers

        # Set up an instruction pipe to tell the processes what to do
        #self.pipe_instr_in, pipe_instr_out = Pipe(False)

        # Set up a queue to feed work to the processes
        #self.update_queue = JoinableQueue()

        

        #self.worker_pool.map_async(self.update_chunk, (pipe_instr_out, self.update_queue, 8))

        return

    
    def _wrap_coord(self, x:int, y:int):
        while x < 0:
            x += self.width
        while x >= self.width:
            x -= self.width
        while y < 0:
            y += self.height
        while y >= self.height:
            y -= self.height
        return x,y
        
    def _wrap_value(self, val:int):
        max = self.width*self.height
        while val < 0:
            val += self.width
        while val >= max:
            val -= self.width
        return val


    def _build(self, initial_state=None):
        neighbour_positions = (
            -self.width-1  ,-self.width   ,-self.width+1 ,
                   -1            ,                                1        ,
            self.width-1   , self.width   , self.width+1
            )
        field = []

        # Build the field
        for y in range (0, self.height):
            for x in range (0, self.width):
                if initial_state != None:
                    field.append(Cell(initial_state[y][x]))
                else:
                    field.append(Cell(randint(0, 1)))

        # Assign the neighbour addreses to each cell
        for c_idx in range (0, len(field)):
            field[c_idx].neighbours.clear()
            for n in neighbour_positions:
                n_idx = self._wrap_value(c_idx + n)
                field[c_idx].neighbours.append(n_idx)

        return field

    def get_cell(self, addr:int):
        if addr < 0 or addr >= len(self.field): 
            raise IndexError(f'Invalid cell address: {addr}')
        return self.field[addr]
    
    def get_workload(self, chunk:int, total_chunks:int):
        if total_chunks < 1:
            raise ValueError('Invalid number of chunks')
        if chunk < 1 or chunk > total_chunks:
            raise ValueError(f'Invalid number of chunks ({chunk}/{total_chunks})')
        
        chunk_sz = (int)(len(self.field)/total_chunks)
        chunk_end = chunk*chunk_sz
        chunk_start = chunk_end - chunk_sz
        return chunk_start, chunk_end

    def update_chunk(self, workload):
        chunk, total_chunks = workload
        chunk_start, chunk_end = self.get_workload(chunk, total_chunks)

        change_count = 0

        for c_idx in range(chunk_start, chunk_end):
            change_count += (self.field[c_idx].set_next_state(self.field) * c_idx)

        return change_count


    def update_chunk_2(self, workload):
        chunk, total_chunks = workload
        chunk_start, chunk_end = self.get_workload(chunk, total_chunks)
        for c_idx in range(chunk_start, chunk_end):
            self.field[c_idx].set_current_state()

    def update(self, g_field):
        change_count = 0
        # work = [(c, self.worker_count) for c in range(1,self.worker_count + 1)]
        # test = process_pool.map(self.update_chunk, work)
        # process_pool.map(self.update_chunk_2, work)
        # change_count = sum(test)
        cell_cnt = len(self.field)
        for c_idx in range(0, cell_cnt):
            change_count += (self.field[c_idx].set_next_state(self.field) * c_idx)
        for c_idx in range(0, cell_cnt):
            self.field[c_idx].set_current_state()
            #g_field.draw_idx(c_idx)

        return change_count
    


class GraphicsField:
    def __init__(self, field, batch, cell_draw_sz, circles=False):
        self.g_field = []
        self.field = field
        for y in range (0, self.field.height):
            for x in range (0, self.field.width):
                cell_state = self.field.get_cell(x*y + x).current_state
                self.g_field.append(GraphicCell(x, y, cell_state, batch, cell_draw_sz, circles))
        self.draw()

    # def draw_idx(self, c_idx):
    #     cell = self.field.get_cell(c_idx)
    #     self.g_field[c_idx].draw(cell.current_state, cell.state_changed)

    def draw(self):
        for c_idx in range(0, len(self.g_field)):
            cell = self.field.get_cell(c_idx)
            self.g_field[c_idx].draw(cell.current_state, cell.state_changed)
            #self.draw_idx(c_idx)