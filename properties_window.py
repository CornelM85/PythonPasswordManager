import time

import customtkinter as ctk


class PropertiesWindow(ctk.CTkToplevel):
    def __init__(self, master, command, **kwargs):
        super().__init__(master, **kwargs)

        self.overrideredirect(True)

        self.go_to_site = ctk.CTkButton(self, text='Go to site', fg_color='transparent', hover_color='green',
                                        command=command, width=100, height=10)
        self.go_to_site.pack()

