import tkinter as tk
from src.ui import ui_components, styles, layout

class Page4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=styles.background_color)

        header = ui_components.Header(self, text="Page 4")
        header.pack(side="top", fill="x")

        main_content = ui_components.MainContent(self)
        main_content.pack(side="top", fill="both", expand=True)

        footer = ui_components.Footer(self)
        footer.pack(side="bottom", fill="x")

        self.layout_settings()

    def layout_settings(self):
        layout.configure(self)

    def update_content(self, content):
        self.main_content.update(content)

if __name__ == "__main__":
    root = tk.Tk()
    page = Page4(root, None)
    page.pack(side="top", fill="both", expand=True)
    root.mainloop()