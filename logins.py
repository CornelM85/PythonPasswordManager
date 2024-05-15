import customtkinter as ctk
from PIL import Image

from browser import Browser

from utility_functions import resource_path


class LoginsFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.add_new_btn = ctk.CTkButton(self, text='+ Add new', height=10, font=ctk.CTkFont('times', size=20),
                                         anchor='w', cursor='hand2', command=self.add_site_url)
        self.add_new_btn.grid(row=0, column=0, sticky='w')

        self.edit_btn = ctk.CTkButton(self, text='Edit', height=10, font=ctk.CTkFont('times', size=20),
                                      anchor='w', cursor='hand2')
        self.edit_btn.grid(row=0, column=1, sticky='w')

        self.delete_btn = ctk.CTkButton(self, text='Delete', height=10, font=ctk.CTkFont('times', size=20),
                                        anchor='w', cursor='hand2')
        self.delete_btn.grid(row=0, column=2, sticky='w')

        self.web_sites = ctk.CTkScrollableFrame(self, border_width=2, width=670, height=480)
        self.web_sites.grid(row=1, columnspan=12, pady=20)

    def add_site_url(self):
        browser = Browser()
        url = browser.get_url()
        entries = int(len(self.web_sites.children) / 2)
        if url != 'Not a login page!':
            browser.get_site_icon(url)
            image = ctk.CTkImage(Image.open(resource_path(f'Images/{browser.set_icon_name(url)}')), size=(20, 20))
            icon = ctk.CTkLabel(self.web_sites, image=image, width=20, height=10, text='')
            icon.grid(row=entries + 1, column=0, padx=(0, 20))
            url = ctk.CTkLabel(self.web_sites, height=10, width=630, text=url, text_color='#00A2E8',
                               cursor='hand2', font=ctk.CTkFont('times', size=18, underline=True), anchor='w')
            url.grid(row=entries + 1, column=1)
            url.bind('<Button-1>', self.go_to_site)

    def go_to_site(self, event):
        url = event.widget.master.cget('text')
        browser = Browser()
        browser.go_to_url(url)

