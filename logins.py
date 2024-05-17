import json
import customtkinter as ctk
from urllib.parse import urlparse
from PIL import Image

from browser import Browser

from utility_functions import resource_path


class LoginsFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        space = 30 * ' '

        self.add_new_btn = ctk.CTkButton(self, text='+ Add new', height=10, font=ctk.CTkFont('times', size=20),
                                         anchor='w', cursor='hand2', command=self.add_site_url)
        self.add_new_btn.grid(row=0, column=0, sticky='w')

        self.edit_btn = ctk.CTkButton(self, text='Edit', height=10, font=ctk.CTkFont('times', size=20),
                                      anchor='w', cursor='hand2')
        self.edit_btn.grid(row=0, column=1, sticky='w')

        self.delete_btn = ctk.CTkButton(self, text='Delete', height=10, font=ctk.CTkFont('times', size=20),
                                        anchor='w', cursor='hand2')
        self.delete_btn.grid(row=0, column=2, sticky='w')

        self.website_name = ctk.CTkLabel(self, height=10, font=ctk.CTkFont('times', size=15),
                                         text=f' | Icon | Website{space}|', anchor='w')
        self.website_name.grid(row=1, columnspan=12, pady=(10, 2), sticky='w')

        self.web_sites = ctk.CTkScrollableFrame(self, border_width=2, width=670, height=480)
        self.web_sites.grid(row=2, columnspan=12)

        self.get_db_info()

    def add_site_url(self):
        browser = Browser()
        url = browser.get_url()
        if url != 'Not a login page!' and browser.is_login_field_present(url):
            ctk.CTkEntry(self, placeholder_text='Username/E-mail/Phone')
            ctk.CTkEntry(self, placeholder_text='Password')
            self.add_site_info_to_db(url)
        self.get_db_info()

    def go_to_site(self, event):
        with open('db.json', 'r') as f:
            data = json.load(f)
            values = data.values()
            for dictionary in values:
                for k, v in dictionary.items():
                    if k == 'url' and event.widget.master.cget('text') in v:
                        url = v

        browser = Browser()
        browser.go_to_url(url)

    def add_site_info_to_db(self, url):
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

            db[len(db)] = {'url': url, 'image': image}
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
                        icon = ctk.CTkLabel(self.web_sites, image=image, width=20, height=10, text='')
                        icon.grid(row=i, column=0, padx=(0, 15))

                    if k == 'url':
                        url = ctk.CTkLabel(self.web_sites, height=10, width=630, text=urlparse(v).hostname,
                                           text_color='#00A2E8',
                                           cursor='hand2', font=ctk.CTkFont('times', size=18, underline=True),
                                           anchor='w')
                        url.grid(row=i, column=1)
                        url.bind('<Button-1>', self.go_to_site)
                i += 1
