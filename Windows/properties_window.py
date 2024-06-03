import customtkinter as ctk
from browser import Browser
from db_connection import ConnectDB


class PropertiesWindow(ctk.CTkToplevel):
    def __init__(self, master, user_id, url_name_displayed, **kwargs):
        super().__init__(master, **kwargs)

        self.overrideredirect(True)

        self.ms = master

        self.__connection = ConnectDB()

        self.__user_id = user_id

        self.__url_name_displayed = url_name_displayed

        self.__go_url = ctk.CTkButton(self, text='Go to site', fg_color='transparent', hover_color='green',
                                      command=self.__go_to_site, width=100, height=10)
        self.__go_url.pack()

        self.__edit = ctk.CTkButton(self, text='Edit', fg_color='transparent', hover_color='green',
                                    width=100, height=10)
        self.__edit.pack()

        self.__delete = ctk.CTkButton(self, text='Delete', fg_color='transparent', hover_color='green',
                                      width=100, height=10, command=self.__delete)
        self.__delete.pack()

        self.bind('<Leave>', self.__on_leave)

    def __go_to_site(self):
        url = self.__connection.get_website(user_id=self.__user_id, url_name_displayed=self.__url_name_displayed)
        credentials = self.__connection.get_website_credentials(user_id=self.__user_id,
                                                         url_name_displayed=self.__url_name_displayed)
        browser = Browser()
        browser.go_to_url(url, credentials[0], credentials[1])

    def __on_leave(self, event):
        if 'ctkbutton' not in str(event.widget):
            self.destroy()

    def __delete(self):
        self.__connection.delete_website(user_id=self.__user_id, url_name_displayed=self.__url_name_displayed)
        self.ms.logins_frame.refresh()
