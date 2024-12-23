import tkinter as tk

root = tk.Tk()
root.title("Test")
root.geometry("1800x900")
# root.state("zoomed")  # windows only

tk.Label(root, text="Najla'a is a bad sister", font=("verdana", 35)).grid(row=0, column=0)

frame = tk.LabelFrame(root)
frame.grid(row=0, column=1, padx=5, ipady=50)
tk.Label(frame, text="Najlaa is a Bad sis 2").grid(row=0, column=1)
def comm1(x):
    print("whatever it takes", x)
button = tk.Button(frame, text="butt", command= comm1(1)).grid(row=1, column=1)

tk.Entry(root).grid(row=2, column=1)
root.mainloop()