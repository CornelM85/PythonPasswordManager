import customtkinter as ctk
from PIL import Image

from utility_functions import resource_path


class LoginsFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.add_new_btn = ctk.CTkButton(self, text='+ Add new', height=10, font=ctk.CTkFont('times', size=20),
                                         anchor='w', cursor='hand2', command=self.add_login)
        self.add_new_btn.grid(row=0, column=0, sticky='w')

        self.web_sites = ctk.CTkScrollableFrame(self, border_width=2, width=670, height=480)
        self.web_sites.grid(row=1, column=0, pady=20)


    def add_login(self):
        image = ctk.CTkImage(Image.open(resource_path('Images/info.png')), size=(20, 20))
        icon = ctk.CTkLabel(self.web_sites, image=image, width=20, height=10, text='')
        icon.grid(row=0, column=0, padx=(0, 10))
        username = ctk.CTkLabel(self.web_sites, width=180, height=10, text='sadasdasdasdadsa', anchor='w')
        username.grid(row=0, column=1)
        password = ctk.CTkLabel(self.web_sites, width=180, height=10, text='123456789', anchor='e')
        password.grid(row=0, column=2, padx=(0, 10))