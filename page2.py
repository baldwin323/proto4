```python
import tkinter as tk
from tkinter import ttk

def go_to_page1():
    import page1
    page1.create_page1()

def go_to_page3():
    import page3
    page3.create_page3()

def create_page2():
    page2 = tk.Tk()
    page2.title("Page 2")

    label = ttk.Label(page2, text="This is Page 2")
    label.pack(side="top", fill="both", expand=True, padx=20, pady=20)

    button1 = ttk.Button(page2, text="Go to Page 1", command=go_to_page1)
    button1.pack(side="left", fill="both", expand=True, padx=20, pady=20)

    button3 = ttk.Button(page2, text="Go to Page 3", command=go_to_page3)
    button3.pack(side="right", fill="both", expand=True, padx=20, pady=20)

    page2.mainloop()

if __name__ == "__main__":
    create_page2()
```