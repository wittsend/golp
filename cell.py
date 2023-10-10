from pyglet import shapes

# The cell memory object (keeps track of cell state and can be shared with other processes for
# multi-core processing)
class Cell:
    def __init__(self, current_state:int):
        self.next_state = current_state
        self.current_state = current_state
        self.state_changed = 1
        self.neighbours = []
        return

    def set_next_state(self, field):
        live_count = 0
        self.next_state=0
        for neighbour in self.neighbours:
            live_count += field[neighbour].current_state
            if live_count > 3: break
        if self.current_state == 1:
            if live_count == 2 or live_count == 3:
                self.next_state = 1
        else:
            if live_count == 3:
                self.next_state = 1
        self.state_changed = abs(self.next_state - self.current_state)
        return self.state_changed
    
    def set_current_state(self):
        self.current_state = self.next_state
        return self.current_state
    


# The cell graphics object (that represents the cell on screen)
class GraphicCell:
    COLOUR_ALIVE = (0,0,0)
    COLOUR_BORN = (0,127,0)
    COLOUR_DEAD = (255,255,255)
    
    def __init__(self, x:int, y:int, current_state, batch=None, cell_draw_sz:int = 1, circles:bool = False):
        self.x = x
        self.y = y
        self.cell_draw_sz = cell_draw_sz
        
        if current_state == 1:
            cell_colour =  GraphicCell.COLOUR_BORN
        else:
            cell_colour = GraphicCell.COLOUR_DEAD
        
        if cell_draw_sz == 1:
            self.graphic = shapes.Rectangle(self.x, self.y, 1, 1, cell_colour, batch=batch)
        else:
            if circles:
                self.graphic = shapes.Circle(self.x*self.cell_draw_sz, self.y*self.cell_draw_sz, self.cell_draw_sz/2, color=cell_colour, batch=batch)
                #self.graphic = Circle(Point(cell_draw_sz*(x + 0.5), cell_draw_sz*(y + 0.5)), cell_draw_sz)
            else:
                self.graphic = shapes.Rectangle(self.x*self.cell_draw_sz, self.y*self.cell_draw_sz, self.cell_draw_sz, self.cell_draw_sz, cell_colour, batch=batch)
                #self.graphic = Rectangle(Point(x*cell_draw_sz, y*cell_draw_sz), \
                #                        Point(cell_draw_sz*(x + 1) - 1, cell_draw_sz*(y + 1) - 1))

        return

    # def draw(self, window=None, current_state=0, state_changed=1):
    #     draw = False

    #     if window == None:
    #         self.graphic.undraw()
    #         return 0

    #     if current_state == 1:
    #         if state_changed == 1:
    #             draw = True
    #             fill_colour="green"
    #             ol_colour="green"
    #         else:
    #             fill_colour="black"
    #             ol_colour="black"
    #     else:
    #         if state_changed == 1:
    #             self.graphic.undraw()
    #             return current_state
    #         else:
    #             return current_state
    #     self.graphic.setFill(fill_colour)
    #     self.graphic.setOutline(ol_colour)
    #     if draw:
    #         try:
    #             self.graphic.draw(window)
    #         except:
    #             return
    #     return

    def draw(self, current_state=0, state_changed=1):
        visible = True

        if current_state == 1:
            visible = True
            if state_changed == 1:
                fill_colour=GraphicCell.COLOUR_BORN
            else:
                fill_colour=GraphicCell.COLOUR_ALIVE
        else:
            visible = False
        
        if visible == True:
            self.graphic.color = fill_colour
            self.graphic.visible = True
        else:
            self.graphic.visible = False
        return current_state
