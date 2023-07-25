import tkinter as tk
from src.ui import ui_components, styles, layout

class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=styles.background_color)

        header = ui_components.Header(self, text="Page 3")
        header.pack(side="top", fill="x")

        main_content = ui_components.MainContent(self)
        main_content.pack(side="top", fill="both", expand=True)

        footer = ui_components.Footer(self)
        footer.pack(side="bottom", fill="x")

        back_button = ui_components.Button(self, text="Back",
                                           command=lambda: controller.show_frame("Page2"))
        back_button.pack()

        next_button = ui_components.Button(self, text="Next",
                                           command=lambda: controller.show_frame("Page4"))
        next_button.pack()

if __name__ == "__main__":
    app = layout.SampleApp()
    app.mainloop()