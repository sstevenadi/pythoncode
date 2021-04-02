import tkinter as tk
import mylib as lib
from collections import deque

def line(data):
    if len(data) > 0:
        last = data[-1]
        next = last + 1
    else:
        next = 1

    a.append(next)
    lb_last['text'] = str(next)

def next_antri(lb_meja,a):
    # val = lib.enqueue(data)
    val = a.popleft()
    lb_meja['text'] = str(val)

if __name__ == "__main__":
    a = deque()

    window = tk.Tk()
    mainFrame = tk.Frame(master=window, width=900, height=400)
    mainFrame.pack()

    lb_resp1 = tk.Label(master=mainFrame, text="Meja 01")
    lb_resp1.place(x=50, y=0)
    lb_resp2 = tk.Label(master=mainFrame, text="Meja 02")
    lb_resp2.place(x=250, y=0)
    lb_resp3 = tk.Label(master=mainFrame, text="Meja 03")
    lb_resp3.place(x=450, y=0)
    lb_resp4 = tk.Label(master=mainFrame, text="Meja 04")
    lb_resp4.place(x=650, y=0)

    lb_next1 = tk.Label(master=mainFrame, text="00")
    lb_next1.place(x=50, y=20)
    lb_next2 = tk.Label(master=mainFrame, text="00")
    lb_next2.place(x=250, y=20)
    lb_next3 = tk.Label(master=mainFrame, text="00")
    lb_next3.place(x=450, y=20)
    lb_next4 = tk.Label(master=mainFrame, text="00")
    lb_next4.place(x=650, y=20)

    next1 = tk.Button(master=mainFrame, text="Next", command=lambda meja=lb_next1: next_antri(meja,a))
    next1.place(x=30, y=50)
    next2 = tk.Button(master=mainFrame, text="Next", command=lambda meja=lb_next2: next_antri(meja,a))
    next2.place(x=230, y=50)
    next3 = tk.Button(master=mainFrame, text="Next", command=lambda meja=lb_next3: next_antri(meja,a))
    next3.place(x=430, y=50)
    next4 = tk.Button(master=mainFrame, text="Next", command=lambda meja=lb_next4: next_antri(meja,a))
    next4.place(x=630, y=50)

    lb_antri = tk.Label(master=mainFrame, text="Last Queue")
    lb_antri.place(x=200, y=100)
    lb_last = tk.Label(master=mainFrame, text="00")
    lb_last.place(x=200, y=150)

    antri = tk.Button(master=mainFrame, text="Queue", command=lambda : line(a))
    antri.place(x=550, y=150)

    window.mainloop()