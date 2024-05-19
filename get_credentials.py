import customtkinter as ctk
from browser import Browser


class Credentials(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.ms = master

        self.geometry('200x200')
        self.user_field = ctk.CTkEntry(self, placeholder_text='Username/E-mail/Phone')
        self.user_field.grid(row=0, column=0)
        self.pass_field = ctk.CTkEntry(self, placeholder_text='Password')
        self.pass_field.grid(row=1, column=0)
        self.submit = ctk.CTkButton(self, width=20, text='OK', command=self.add_to_db)
        self.submit.grid(row=2, column=0)

    def add_to_db(self):
        browser = Browser()
        url = browser.get_url()
        user = self.user_field.get()
        pswd = self.pass_field.get()
        if user != '' and pswd != '':
            self.destroy()
            self.ms.logins_frame.add_site_info_to_db(url, user, pswd)
            self.ms.logins_frame.get_db_info()

