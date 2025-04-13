from graphics import Canvas
import time

# Constants for canvas and cell settings
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_cells(canvas, eraser):
    """Change color of any blue cell that touches the eraser to white"""
    eraser_x = canvas.get_mouse_x()
    eraser_y = canvas.get_mouse_y()
    
    eraser_left = eraser_x
    eraser_top = eraser_y
    eraser_right = eraser_left + ERASER_SIZE
    eraser_bottom = eraser_top + ERASER_SIZE

    # Get all overlapping shapes
    touching = canvas.find_overlapping(eraser_left, eraser_top, eraser_right, eraser_bottom)

    for shape in touching:
        if shape != eraser:
            canvas.set_color(shape, 'white')

def main():
    # Create canvas
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Draw grid of blue squares
    for y in range(0, CANVAS_HEIGHT, CELL_SIZE):
        for x in range(0, CANVAS_WIDTH, CELL_SIZE):
            canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, 'blue')

    # Wait for click to start
    canvas.wait_for_click()
    click_x, click_y = canvas.get_last_click()

    # Create pink eraser rectangle
    eraser = canvas.create_rectangle(
        click_x,
        click_y,
        click_x + ERASER_SIZE,
        click_y + ERASER_SIZE,
        'pink'
    )

    # Start eraser movement
    while True:
        # Move eraser with mouse
        new_x = canvas.get_mouse_x()
        new_y = canvas.get_mouse_y()
        canvas.moveto(eraser, new_x, new_y)

        # Erase touching cells
        erase_cells(canvas, eraser)

        # Slight pause to avoid overload
        time.sleep(0.03)

# Run main
if __name__ == '__main__':
    main()
