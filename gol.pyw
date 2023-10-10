from time import time_ns as current_time 
from field import Field, GraphicsField
import pyglet as gl

# field_width = 32
# field_height = 32
# cell_width = 24
# field_width = 64
# field_height = 64
# cell_width = 12
field_width = 128
field_height = 128
cell_width = 6
# field_width = 640
# field_height = 480
# cell_width = 2




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


iter = 0
iter_old = 0
change_count = 0
change_count_old = 0
zero_change_count = 0

def status_update(dt):
    global change_count
    global change_count_old
    global iter
    global iter_old
    global zero_change_count

    # End game detection
    if (change_count_old - change_count) == 0:
        zero_change_count += 1
    else:
        zero_change_count = 0
    if zero_change_count >= 3:
        print("\nNo change detected. End.")
        

    #print(f'{(iter-iter_old)/(current_time-last_status_update):.2f}cps, {iter} iterations, {change_count * 100/len(field):.2f}% change    ', end='\r')
    print(f'{(iter-iter_old)/dt:.2f}cps, {iter} iterations, {change_count_old - change_count} change    ', end='\r')
    
    #win_events_pct = task_win_events.get_run_time_pct(total_time)
    #update_task_pct = task_field_update.get_run_time_pct(total_time)
    #status_task_pct = task_status_update.get_run_time_pct(total_time)
    #idle_pct = 100.0 - win_events_pct - update_task_pct - status_task_pct

    #print(f'{(iter-iter_old)/(total_time)/10**-9:.2f}cps, {iter} iterations, WinEvents:{win_events_pct:3.2f}%, FieldUpdate:{update_task_pct:3.2f}%, StatusUpdate:{status_task_pct:3.2f}%, Idle:{idle_pct:3.2f}%', end='\r')
    iter_old = iter
    change_count_old = change_count


def refresh(dt, field, g_field):
    global iter
    global change_count
    change_count = field.update(g_field)
    iter += 1
    g_field.draw()
    return

# Main
#if __name__ == '__main__':


print('Generating the cell field...')
field = Field(field_width, field_height, initial_state=None)

print('Creating graphic window...')    

gl_config = gl.gl.Config(double_buffer=True)

win = gl.window.Window(field_width*cell_width, field_height*cell_width, config=gl_config)

print('Generating the graphics buffer...')
draw_batch = gl.graphics.Batch()

g_field = GraphicsField(field, draw_batch, cell_width)
g_background = gl.shapes.Rectangle(0,0,field_width*cell_width, field_height*cell_width, (255,255,255))

gl.clock.schedule(refresh, field, g_field)
gl.clock.schedule_interval(status_update, 0.5)

print('Starting simulation.')



@win.event
def on_draw():
    #win.clear()
    g_background.draw()
    draw_batch.draw()

gl.app.run()
