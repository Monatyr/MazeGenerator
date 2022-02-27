from tkinter import *
from tkinter import ttk

from plain import Plain
import sys


if __name__ == "__main__":
    args = sys.argv
    height, width = int(args[1]), int(args[2])
    v_multip, h_multip = 30, 30
    plain = Plain(height, width)

    root = Tk()
    root.title("Maze creator")
    root.geometry(f'{width*v_multip}x{height*h_multip}')
    lines_tag = "tag1"

    canvas = Canvas(root, height=height*v_multip, width=width*h_multip, bg='#fff')
    canvas.pack()

    def inner_loop(event):
        global plain
        canvas.delete(lines_tag)
        plain = Plain(height, width)
        root_cell = plain.grid[height//2][width//2]
        plain.create_dfs_maze(root_cell)
        
        for i, row in enumerate(plain.grid):
            for j, el in enumerate(row):
                if el.walls[0]:
                    canvas.create_line(j*h_multip, i*v_multip, j*h_multip, (i+1)*v_multip, fill='black', tags=lines_tag)
                if el.walls[1]:
                    canvas.create_line(j*h_multip, i*v_multip, (j+1)*h_multip, i*v_multip, fill='black', tags=lines_tag)
                if el.walls[2]:
                    canvas.create_line((j+1)*h_multip, i*v_multip, (j+1)*h_multip, (i+1)*v_multip, fill='black', tags=lines_tag)
                if el.walls[3]:
                    canvas.create_line(j*h_multip, (i+1)*v_multip, (j+1)*h_multip, (i+1)*v_multip, fill='black', tags=lines_tag)
        
        canvas.create_rectangle(1, height//2*v_multip+1, h_multip-1, (height//2+1)*v_multip-1, fill='lightgreen', outline='lightgreen', tags=lines_tag)
        canvas.create_rectangle(width*h_multip-h_multip+1, height//2*v_multip+1, width*h_multip-1, (height//2+1)*v_multip-1, fill='#d62d20', outline='#d62d20', tags=lines_tag)
        
    def solve_maze(event):
        solution_path = plain.solve((height//2, 0))
        for el in solution_path:
            canvas.create_rectangle(el[1]*h_multip+10, el[0]*v_multip+10, (el[1]+1)*h_multip-10, (el[0]+1)*v_multip-10, fill="orange", tags=lines_tag)

    inner_loop(None)
    root.bind("<Key>", inner_loop)
    root.bind('s', solve_maze)
    
    root.mainloop()