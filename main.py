import tkinter as tk
from page1 import go_to_page1
from page2 import go_to_page2
from page3 import go_to_page3
from page4 import go_to_page4
from page5 import go_to_page5

def main():
    root = tk.Tk()
    root.title("Main Page")

    button1 = tk.Button(root, text="Go to Page 1", command=go_to_page1)
    button1.pack()

    button2 = tk.Button(root, text="Go to Page 2", command=go_to_page2)
    button2.pack()

    button3 = tk.Button(root, text="Go to Page 3", command=go_to_page3)
    button3.pack()

    button4 = tk.Button(root, text="Go to Page 4", command=go_to_page4)
    button4.pack()

    button5 = tk.Button(root, text="Go to Page 5", command=go_to_page5)
    button5.pack()

    root.mainloop()

if __name__ == "__main__":
    main()