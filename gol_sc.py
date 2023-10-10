from graphics import *
from random import randint
from cell import Cell
from taskscheduler import TaskScheduler
from time import time_ns as current_time 

# field_width = 32
# field_height = 32
# cell_width = 24
field_width = 64
field_height = 64
cell_width = 12
# field_width = 320
# field_height = 240
# cell_width = 3




initial_state = (
    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
)


def wrap_coord(x:int, y:int):
    while x < 0:
        x += field_width
    while x >= field_width:
        x -= field_width
    while y < 0:
        y += field_height
    while y >= field_height:
        y -= field_height
    return x,y
    
def wrap_value(val:int):
    max = field_width*field_height
    while val < 0:
        val += field_width
    while val >= max:
        val -= field_width
    return val

def build_field_old(window, initial_state=None):
    neighbour_positions = (-1, 0, 1)
    field = []
    # Build the field
    for y in range (0, field_height):
        field.append([])
        for x in range (0, field_width):
            if initial_state != None:
                field[y].append(Cell(x, y, initial_state[y][x]))
            else:
                field[y].append(Cell(x, y, randint(0, 1)))
            field[y][x].draw(window)

    # Assign the neighbours to each cell
    for y in range (0, field_height):
        for x in range(0, field_width):
            for y_n in neighbour_positions:
                for x_n in neighbour_positions:
                    if not (x_n == 0 and y_n == 0):
                        w_x, w_y = wrap_coord(x + x_n, y + y_n)
                        field[y][x].neighbours.append(field[w_y][w_x])

    return field

def build_field(initial_state=None):
    neighbour_positions = (
        -field_width-1  ,-field_width   ,-field_width+1 ,
              -1        ,                      1        ,
         field_width-1  , field_width   , field_width+1
        )
    field = {}
    # Build the field
    for y in range (0, field_height):
        for x in range (0, field_width):
            if initial_state != None:
                field[y * field_width + x] = Cell(x, y, initial_state[y][x], cell_width)
            else:
                field[y * field_width + x] = Cell(x, y, randint(0, 1), cell_width)
            #field[y * field_width + x].draw(window)

    # Assign the neighbours to each cell
    for c_idx in range (0, len(field)):
        for n in neighbour_positions:
            n_idx = wrap_value(c_idx + n)
            field[c_idx].neighbours.append(field[n_idx])

    return field


def update_field_old(field):
    for y in range (0, field_height):
        for x in range (0, field_width):
            field[y][x].set_next_state()
    for y in range (0, field_height):
        for x in range (0, field_width):
            field[y][x].update_state()


def update_field(field, window):
    change_count = 0
    for c_idx in range (0, len(field)):
        change_count += (field[c_idx].set_next_state() * c_idx)
    for c_idx in range (0, len(field)):
        field[c_idx].update_state(window)
    return change_count


# Main
if __name__ == '__main__':

    task_field_update = TaskScheduler(24)
    task_flush = TaskScheduler(0)
    task_status_update = TaskScheduler(2)
    task_win_events = TaskScheduler(0)


    print('Creating graphic window...')
    win = GraphWin('Game of Life', field_width*cell_width, field_height*cell_width, autoflush=False)
    print('Generating the field...')
    #field = build_field(win, initial_state=initial_state)
    field = build_field()

    iter = 0
    iter_old = 0
    last_status_update=0.0
    change_count = 0
    change_count_old = 0
    zero_change_count = 0

    print('Starting simulation.')

    win.autoflush = False
    while (1):


        if task_field_update.it_is_time():
            change_count = update_field(field, win)
            iter+=1
            task_field_update.finished()
            task_win_events.it_is_time()
            try:
                #win.checkKey()
                win.checkMouse()
                if win.isClosed(): sys.exit()
                #win.flush()
                task_win_events.finished()
            except:
                sys.exit()


        if task_status_update.it_is_time():
            ctime = current_time()
            total_time = ctime - last_status_update
            #End game detection
            if (change_count_old - change_count) == 0:
                zero_change_count += 1
            else:
                zero_change_count = 0
            if zero_change_count >= 3:
                print("\nNo change detected. End.")
                break

            #print(f'{(iter-iter_old)/(current_time-last_status_update):.2f}cps, {iter} iterations, {change_count * 100/len(field):.2f}% change    ', end='\r')
            #print(f'{(iter-iter_old)/(ctime-last_status_update)/10**-9:.2f}cps, {iter} iterations, {change_count_old - change_count} change    ', end='\r')
            
            win_events_pct = task_win_events.get_run_time_pct(total_time)
            update_task_pct = task_field_update.get_run_time_pct(total_time)
            status_task_pct = task_status_update.get_run_time_pct(total_time)
            flush_task_pct = task_flush.get_run_time_pct(total_time)
            idle_pct = 100.0 - win_events_pct - update_task_pct - status_task_pct - flush_task_pct

            print(f'{(iter-iter_old)/(total_time)/10**-9:.2f}cps, {iter} iterations, WinEvents:{win_events_pct:3.2f}%, DrawEvents:{flush_task_pct:3.2f}%, FieldUpdate:{update_task_pct:3.2f}%, StatusUpdate:{status_task_pct:3.2f}%, Idle:{idle_pct:3.2f}%', end='\r')
            last_status_update = ctime
            iter_old = iter
            change_count_old = change_count
            task_status_update.finished()

    win.autoflush = True

    # Wait for user to close window.
    while (1):
        current_time = time.time()
        try:
            win.checkKey()
            win.checkMouse()
        except:
            sys.exit()
        time.sleep(0.1)
