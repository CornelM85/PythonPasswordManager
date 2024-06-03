import customtkinter as ctk
from browser import Browser
from db_connection import ConnectDB
from utility_functions import place_window_in_center
from CTkMessagebox import CTkMessagebox
from Frames.websites_info import WebsitesInfo


class CredentialsWindow(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.ms = master

        self.title('Enter credentials')

        place_window_in_center(master=self.ms, width=270, height=200, window_name=self, multiply=True)

        self.resizable(width=False, height=False)

        self.url_name = ctk.CTkEntry(self, placeholder_text='Url name', width=200)
        self.url_name.grid(row=0, column=0, padx=35, pady=10)

        self.user_field = ctk.CTkEntry(self, placeholder_text='Username/E-mail/Phone', width=200)
        self.user_field.grid(row=1, column=0)

        self.pass_field = ctk.CTkEntry(self, placeholder_text='Password', width=200)
        self.pass_field.grid(row=2, column=0, pady=10)

        self.confirm_pass_field = ctk.CTkEntry(self, placeholder_text='Confirm Password', width=200)
        self.confirm_pass_field.grid(row=3, column=0)

        self.submit = ctk.CTkButton(self, width=60, text='OK', command=self.add_to_db)
        self.submit.grid(row=4, column=0)

    def add_to_db(self):
        browser = Browser()
        url = browser.get_url()
        url_name = self.url_name.get()
        user = self.user_field.get()
        password = self.pass_field.get()
        confirm_password = self.confirm_pass_field.get()

        if user == '' or password == '' or confirm_password == '' or url_name == '':
            self.__message('All the fields must be filled!')

        elif self.__check_field_text(user) is False:
            self.__message('Username/E-mail/Phone field contain spaces!')

        elif self.__check_field_text(password) is False or self.__check_field_text(confirm_password) is False:
            self.__message('The password fields contain spaces!')

        elif password != confirm_password:
            CTkMessagebox(self, title='Alert', width=150, height=50,
                          icon='warning', message='Password fields don\'t match!', option_1='OK')

        else:
            self.destroy()
            self.add_site_info_to_db(url, user, password, url_name)
            WebsitesInfo(self.ms)

    def __check_field_text(self, input_text: str):
        for char in input_text:
            if char == ' ':
                return False

    def __message(self, message_text: str):
        CTkMessagebox(self, title='Alert', width=150, height=50,
                      icon='warning', message=message_text, option_1='OK')

    def add_site_info_to_db(self, url: str, user: str, password: str, url_name: str):
        connection = ConnectDB()
        browser = Browser()
        browser.get_site_icon(url)
        image = browser.set_icon_name(url)
        user_id = self.ms.logins_frame.user_id
        connection.add_website(user_id=user_id, login_name=user, login_password=password, url=url,
                               url_name_displayed=url_name, image_name=image)