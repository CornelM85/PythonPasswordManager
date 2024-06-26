import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from Frames.websites_info import WebsitesInfo
from browser import Browser
from Windows.website_credentials_window import CredentialsWindow
from Windows.master_login_window import MasterLoginWindow
from db_connection import ConnectDB


class LoginsFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.user_id = None

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

    def add_site_url(self):
        browser = Browser()
        url = browser.get_url()

        if self.__is_url_in_db(url):
            CTkMessagebox(self, title='Alert', width=500, height=50, icon='warning',
                          message='You already have this website info stored in database!', option_1='OK')

        elif self.ms.master_login_frame.get_username() == '':
            master_login_window = MasterLoginWindow(self.ms)
            master_login_window.grab_set()

        elif url != 'Not a login page!' and browser.is_login_field_present(url):
            credentials = CredentialsWindow(self.ms)
            credentials.grab_set()

    def refresh(self, on_login=True):
        self.web_sites.destroy()
        self.web_sites = ctk.CTkScrollableFrame(self, border_width=2, width=670, height=480)
        self.web_sites.grid(row=2, columnspan=12)
        if on_login is False:
            WebsitesInfo(self.ms)

    def __is_url_in_db(self, url: str):
        connection = ConnectDB()
        results = connection.is_url(user_id=self.user_id)
        for result in results:
            if url == result[0]:
                return True