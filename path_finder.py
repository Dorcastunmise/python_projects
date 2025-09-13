import curses
from curses import wrapper
import queue
import time


maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i,j) in path:
                stdscr.addstr(i, j*2, "X", RED)
            else:
                stdscr.addstr(i, j*2, value, BLUE)


def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j
    return None

def find_path(maze, stdscr):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)

    q= queue.Queue()  #FIFO queue (first-in first-out)
    q.put((start_pos, [start_pos]))

    visited = set() #will contain all positions/nodes visited in the maze

    while not q.empty():
        current_pos, path = q.get() #current_pos = start_pos, path = [start_pos]
        row, col = current_pos

        stdscr.clear()
        #stdscr.addstr(5, 5, "Path Finder Algorithm Visualization",blue_and_black) #(row, column, string, color)
        print_maze(maze, stdscr, path)
        time.sleep(0.2)
        stdscr.refresh()

        if maze[row][col] == end: #if the end (X) of the maze is found
            return path

        neighbours = find_neighbours(maze, row, col)
        for neighbour in neighbours:
            if neighbour in visited:
                continue

            r, c = neighbour
            if maze[r][c] == "#":
                continue

            new_path = path + [neighbour]
            q.put((neighbour, new_path))
            visited.add(neighbour)
 
def find_neighbours(maze, row, col):
    neighbours = []
    if row > 0: 
        neighbours.append((row - 1, col)) #to move up
    if row + 1 < len(maze): 
        neighbours.append((row + 1, col)) #to move down
    if col > 0:
        neighbours.append((row, col - 1)) #to move left
    if col + 1 < len(maze[0]):
        neighbours.append((row, col + 1)) #to move right
    return neighbours


def main(stdscr):      #stdscr - standard output screen
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK) #color pair 1 - blue text on black background
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK) #color pair 1 - blue text on black background
    
    find_path(maze, stdscr)
    stdscr.getch() #gets chracter input from user like the input function
    
wrapper(main) #wrapper initializes the curses module then calls the function passed to it(main here)
