import customtkinter as ctk


class InfoLabel(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.wm_attributes('-alpha', 0.4)
        self.overrideredirect(True)

        self.__info_text = ctk.CTkLabel(self, text='Click for menu', text_color='white')
        self.__info_text.grid(row=0, column=0, padx=5)

        self.after(1000, self.destroy)
