import tkinter as tk
from src.ui import ui_components, styles, layout

class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=styles.background_color)

        self.header = ui_components.Header(self, text="Page 2")
        self.header.pack(side="top", fill="x")

        self.main_content = ui_components.MainContent(self)
        self.main_content.pack(side="top", fill="both", expand=True)

        self.footer = ui_components.Footer(self)
        self.footer.pack(side="bottom", fill="x")

        self.layout_settings = layout.LayoutSettings(self)
        self.layout_settings.apply_to_all()

    def update_content(self, content):
        self.main_content.update(content)

if __name__ == "__main__":
    root = tk.Tk()
    Page2(root).pack(side="top", fill="both", expand=True)
    root.mainloop()