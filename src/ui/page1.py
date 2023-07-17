import tkinter as tk
from src.ui import ui_components, styles, layout

class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=styles.background_color)

        # Header
        self.header = ui_components.Header(self, text="Page 1")
        self.header.pack(side="top", fill="x")

        # Main content
        self.main_content = tk.Frame(self, bg=styles.background_color)
        self.main_content.pack(side="top", fill="both", expand=True)
        layout.configure_grid(self.main_content)

        # Footer
        self.footer = ui_components.Footer(self)
        self.footer.pack(side="bottom", fill="x")

        self.populate_main_content()

    def populate_main_content(self):
        label = tk.Label(self.main_content, text="This is Page 1", font=styles.large_font, bg=styles.background_color)
        label.grid(row=0, column=0, padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    Page1(root, None).pack(side="top", fill="both", expand=True)
    root.mainloop()