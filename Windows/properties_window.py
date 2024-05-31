import customtkinter as ctk
from browser import Browser
from db_connection import ConnectDB


class PropertiesWindow(ctk.CTkToplevel):
    def __init__(self, master, user_id, url_name_displayed, **kwargs):
        super().__init__(master, **kwargs)

        self.overrideredirect(True)

        self.__go_url = ctk.CTkButton(self, text='Go to site', fg_color='transparent', hover_color='green',
                                      command=lambda: self.__go_to_site(user_id, url_name_displayed), width=100, height=10)
        self.__go_url.pack()

        self.__edit = ctk.CTkButton(self, text='Edit', fg_color='transparent', hover_color='green',
                                    width=100, height=10)
        self.__edit.pack()

        self.__delete = ctk.CTkButton(self, text='Delete', fg_color='transparent', hover_color='green',
                                      width=100, height=10)
        self.__delete.pack()

        self.bind('<Leave>', self.__on_leave)

    def __go_to_site(self, user_id, url_name_displayed):
        connection = ConnectDB()
        url = connection.get_website(user_id=user_id, url_name_displayed=url_name_displayed)
        browser = Browser()
        browser.go_to_url(url)

    def __on_leave(self, event):
        if 'ctkbutton' not in str(event.widget):
            self.destroy()


