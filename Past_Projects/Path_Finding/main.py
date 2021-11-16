# This project is designed to create a path finder that finds the quickest path to a destation

import pygame
import math
from queue import PriorityQueue

WIDTH = 800  # Width of the window
WIN = pygame.display.set_mode((WIDTH, WIDTH)) # Makes a square window
pygame.display.set_caption("A* Path Finding Algorithm") # setting caption for display

# Color codes for the code to use
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

# defining the cubes that will appear on the grid
# need to know the location, width, neighbors, color, etc,
class NODE:
    def __init__(self, row, col, width, total_rows): #
        self.row = row
        self.col = col
        self.x = row*width # self.x & self.y are coords needed for the positioning
        self.y = col*width
        self.color = WHITE # start will all white cubes
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    # initializing what the change in colors are
    # returns current position
    def get_pos(self):
        return self.row, self.col
    # Node was looked at
    def is_closed(self):
        return self.color == RED
    # Node is being examined
    def is_open(self):
        return self.color == GREEN
    # Color of barriers/objects/edges
    def is_barrier(self):
        return self.color == BLACK
    # Color of the starting point
    def is_start(self):
        return self.color == ORANGE
   # Start of the end point
    def is_end(self):
        return self.color == TURQUOISE
    # Resetting a color will go back to white
    def reset(self):
        self.color = WHITE

    # initializing what the original colors are
    def make_start(self): # Starting color
        self.color = ORANGE
    def make_closed(self):
        self.color = RED
    def make_open(self):
        self.color = GREEN
    def make_barrier(self):
        self.color = BLACK
    def make_end(self):
        self.color = TURQUOISE
    def make_path(self):
        self.color = PURPLE
    # drawing the rectangles for the board (win, colors, and positions of nodes with their dimensions)
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    # neighbors of the white spaces
    def update_neighbors(self, grid):
        # check up down left right for neighbors
        self.neighbors = []

        # checking if the row we are at is less than the total rows minus 1.Checking if we can go down.
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # Moving DOWN a row
            self.neighbors.append(grid[self.row + 1][self.col])

        # checking if the row we are at is greater than 0.Checking if we can go up.
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():  # Moving UP a row
            self.neighbors.append(grid[self.row - 1][self.col])

        # checking if the column we are at is less than the total columns minus 1.Checking if we can go right.
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():  # Moving RIGHT a column
            self.neighbors.append(grid[self.row][self.col + 1])

        # checking if the column we are at is more than 0.Checking if we can go left.
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():  # Moving LEFT a column
            self.neighbors.append(grid[self.row][self.col - 1])

    # Compare this spot and another spot. Statement will always read that other is bigger than current
    def __lt__(self, other):
        return False

# defining the heuristic function for calculating distance
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)

def reconstruct_path(came_from, current, draw):
	while current in came_from:
	    current = came_from[current]
	    current.make_path()
	    draw()

def algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue() # open set
    open_set.put((0, count, start))
    came_from = {} #where did this node come from
    g_score = {node: float("inf") for row in grid for node in row} # keeps track of closest current distance
    g_score[start] = 0
    f_score = {node: float("inf") for row in grid for node in row} #keeps track of predicted nodes
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start} #checking if there is a node in the PriorityQueue

    while not open_set.empty(): # if all nodes have been checked, then there is no path
        for event in pygame.event.get(): #creating a way to exit the loop
            if event.type == pygame.QUIT:
                pygame.quit()
        current = open_set.get()[2] #
        open_set_hash.remove(current)

        # The end has been found and the path needs to be created
        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]: #if a neighbor was better, update path to better path
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())

                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        draw()
        if current != start:
            current.make_closed()
    return False

# This functions creates the grid
def make_grid(rows, width):
    grid= []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = NODE(i, j, gap, rows)
            grid[i].append(node)
    return grid
# This function draws the grid lines
def draw_grid(win, rows, width):
    GAP = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i*GAP), (width, i*GAP))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * GAP, 0), (j * GAP, width))

#Funciton draws eveything
def draw(win, grid, rows, width):
    win.fill(WHITE)
    for row in grid:
        for node in row:
            node.draw(win)
    draw_grid(win, rows, width)
    pygame.display.update()

#tracks mouse position and changes the right node when clicked
def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos
    row = y//gap
    col = x//gap
    return row, col




def main(win, width):
    ROWS = 50 # Change this to change the number of grid
    grid = make_grid(ROWS, width)

    start = None # We do not want a set starting or end point
    end = None # We do not want a set starting or end point

    run = True # used to determine if the code has begun running
    # started = False # used to determine if the main algorithm has started
    while run:
        draw(win, grid, ROWS, width) # draws the grid line
        for event in pygame.event.get(): # while looping in the while loop, loop through all the events (timer start, click of mouse, etc) so far
            if event.type == pygame.QUIT: # if the x button has been pressed, stop running the game
                run = False

            if pygame.mouse.get_pressed()[0]: # if the left mouse button has been pressed,
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                if not start and node != end: # making our starting point (and our starting point is not our end point)
                    start = node
                    start.make_start()

                elif not end and node != start: # making our end point
                    end = node
                    end.make_end()

                elif node != end and node != start: # when we are not making out staring point or end point (creating a barrier)
                    node.make_barrier()

            elif pygame.mouse.get_pressed()[2]: # if the right mouse button has been pressed
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                node.reset() # reset the node
                if node == start:
                    start = None
                elif node == end:
                    end == None

            # Run the algorithm
            if event.type == pygame.KEYDOWN: # If we press a key down
                if event.key == pygame.K_SPACE and start and end: # and the key pressed down is the space bar
                    # Check neighbors
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    # call algorithm
                    algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)
                # Clears the board
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)


    pygame.quit()
main(WIN, WIDTH)