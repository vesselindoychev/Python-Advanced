import tkinter as tk

from screens import render_main_screen

if __name__ == '__main__':
    window = tk.Tk()
    window.geometry('600x600')
    window.title('GUI Product shop')
    render_main_screen(window)
    window.mainloop()
