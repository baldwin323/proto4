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

def go_to_page5():
    import page5
    page5.page5()

def page4():
    window = tk.Tk()
    window.title("Page 4")

    label = ttk.Label(window, text="This is Page 4")
    label.grid(column=0, row=0)

    button1 = ttk.Button(window, text="Go to Page 1", command=go_to_page1)
    button1.grid(column=1, row=1)

    button2 = ttk.Button(window, text="Go to Page 2", command=go_to_page2)
    button2.grid(column=1, row=2)

    button3 = ttk.Button(window, text="Go to Page 3", command=go_to_page3)
    button3.grid(column=1, row=3)

    button5 = ttk.Button(window, text="Go to Page 5", command=go_to_page5)
    button5.grid(column=1, row=4)

    window.mainloop()

if __name__ == "__main__":
    page4()
```