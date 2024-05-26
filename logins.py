import json

import customtkinter as ctk
from urllib.parse import urlparse
from PIL import Image

from browser import Browser

from utility_functions import resource_path, place_window_in_center
from get_credentials import Credentials
from properties_window import PropertiesWindow
from info_label import InfoLabel

class LoginsFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.icon = None
        self.url = None
        self.user = None
        self.password = None

        self.ms = master

        space = 38 * ' '

        self.add_new_btn = ctk.CTkButton(self, text='+ Add new', height=10, font=ctk.CTkFont('times', size=20),
                                         anchor='w', cursor='hand2', command=self.add_site_url)
        self.add_new_btn.grid(row=0, column=0, sticky='w')

        self.website_name = ctk.CTkLabel(self, height=10, font=ctk.CTkFont('times', size=15),
                                         text=f' | Icon | Website{space}| User{space}{6 * ' '}| Password{space}|',
                                         anchor='w')
        self.website_name.grid(row=1, columnspan=12, pady=(10, 2), sticky='w')

        self.web_sites = ctk.CTkScrollableFrame(self, border_width=2, width=670, height=480)
        self.web_sites.grid(row=2, columnspan=12)

        self.get_db_info()

    def add_site_url(self):
        browser = Browser()
        url = browser.get_url()
        if url != 'Not a login page!' and browser.is_login_field_present(url):
            credentials = Credentials(self.ms)
            credentials.grab_set()

    def add_site_info_to_db(self, url, user, pswd):
        browser = Browser()
        browser.get_site_icon(url)
        image = browser.set_icon_name(url)

        with open('db.json', 'r+') as f:
            db = json.load(f)
            values = db.values()

            for dictionary in values:
                for v in dictionary.values():
                    if v == url:
                        return None

            db[len(db)] = {'image': image, 'url': url, 'user': user, 'password': pswd}
            f.seek(0)
            f.truncate()
            json.dump(db, f, indent=4)

    def get_db_info(self):
        with open('db.json', 'r') as f:
            data = json.load(f)
            values = data.values()

            i = 0
            for dictionary in values:
                for k, v in dictionary.items():
                    if k == 'image':
                        image = ctk.CTkImage(Image.open(resource_path(f'Images/{v}')), size=(15, 15))
                        self.icon = ctk.CTkLabel(self.web_sites, image=image, width=20, height=10, text='')
                        self.icon.grid(row=i, column=0, padx=(0, 18))

                    if k == 'url':
                        self.url = ctk.CTkLabel(self.web_sites, height=10, width=210, text=urlparse(v).hostname,
                                                text_color='#00A2E8', cursor='hand2',
                                                font=ctk.CTkFont('times', size=18, underline=True), anchor='w')
                        self.url.grid(row=i, column=1)
                        self.url.bind('<Button-1>', self.on_click, add='+')
                        self.url.bind('<Enter>', self.on_enter, add='+')
                        self.url.bind('<Leave>', self.on_leave, add='+')

                    if k == 'user':
                        self.user = ctk.CTkLabel(self.web_sites, height=10, width=210, text=f'{len(v) * '$'}',
                                                 font=ctk.CTkFont('times', size=12), anchor='w')
                        self.user.grid(row=i, column=2)

                    if k == 'password':
                        self.password = ctk.CTkLabel(self.web_sites, height=10, width=210, text=f'{len(v) * '*'}',
                                                     font=ctk.CTkFont('times', size=18), anchor='w')
                        self.password.grid(row=i, column=3)

                i += 1

    def on_click(self, event):
        short_url = event.widget.master.cget('text')
        pointer_x = event.widget.master.winfo_pointerx()
        pointer_y = event.widget.master.winfo_pointery()
        properties_window = PropertiesWindow(self.ms, short_url)
        properties_window.geometry('{}x{}+{}+{}'.format(100, 100, pointer_x, pointer_y))

    def on_enter(self, event):
        pointer_pos = event.widget.master.winfo_pointerxy()
        info_window = InfoLabel(self.ms)
        info_window.geometry('{}x{}+{}+{}'.format(90, 25, pointer_pos[0], pointer_pos[1]))

    def on_leave(self, event):
        event.widget.master.unbind(sequence='<Enter>')