```python
import tkinter as tk
from tkinter import ttk

def go_to_page2():
    import page2
    page2.page2()

def page1():
    window = tk.Tk()
    window.title("Page 1")

    current_page = "Page 1"

    label = ttk.Label(window, text=current_page)
    label.grid(column=0, row=0)

    button = ttk.Button(window, text="Go to Page 2", command=go_to_page2)
    button.grid(column=1, row=0)

    window.mainloop()

if __name__ == "__main__":
    page1()
```