```python
import tkinter as tk
from tkinter import ttk

def go_to_page1():
    import page1
    page1.page1()

def go_to_page2():
    import page2
    page2.page2()

def go_to_page3():
    import page3
    page3.page3()

def go_to_page4():
    import page4
    page4.page4()

def page5():
    window = tk.Tk()
    window.title("Page 5")

    label = ttk.Label(window, text="This is Page 5")
    label.grid(column=0, row=0)

    button1 = ttk.Button(window, text="Go to Page 1", command=go_to_page1)
    button1.grid(column=1, row=1)

    button2 = ttk.Button(window, text="Go to Page 2", command=go_to_page2)
    button2.grid(column=1, row=2)

    button3 = ttk.Button(window, text="Go to Page 3", command=go_to_page3)
    button3.grid(column=1, row=3)

    button4 = ttk.Button(window, text="Go to Page 4", command=go_to_page4)
    button4.grid(column=1, row=4)

    window.mainloop()

if __name__ == "__main__":
    page5()
```