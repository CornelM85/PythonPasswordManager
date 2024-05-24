import json

import customtkinter as ctk

from browser import Browser


class PropertiesWindow(ctk.CTkToplevel):
    def __init__(self, master, short_url, **kwargs):
        super().__init__(master, **kwargs)

        self.overrideredirect(True)

        self.__go_url = ctk.CTkButton(self, text='Go to site', fg_color='transparent', hover_color='green',
                                      command=lambda: self.__go_to_site(short_url=short_url), width=100, height=10)
        self.__go_url.pack()

        self.__edit = ctk.CTkButton(self, text='Edit', fg_color='transparent', hover_color='green',
                                    width=100, height=10)
        self.__edit.pack()

        self.__delete = ctk.CTkButton(self, text='Delete', fg_color='transparent', hover_color='green',
                                      width=100, height=10)
        self.__delete.pack()

        self.bind('<Leave>', self.__on_leave)

    def __go_to_site(self, short_url):
        with open('db.json', 'r') as f:
            data = json.load(f)
            values = data.values()
            for dictionary in values:
                for k, v in dictionary.items():
                    if k == 'url' and short_url in v:
                        url = v

        browser = Browser()
        browser.go_to_url(url)

    def __on_leave(self, event):
        if 'ctkbutton' not in str(event.widget):
            self.destroy()


