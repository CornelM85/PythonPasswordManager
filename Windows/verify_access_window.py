import customtkinter as ctk
from Windows.edit_info_window import EditInfoWindow
from browser import Browser
from db_connection import ConnectDB
from utility_functions import place_window_in_center


class VerifyAccessWindow(ctk.CTkToplevel):
    def __init__(self, master, user_id, url_name_displayed, action=('go_to_url' or 'edit' or 'delete'), **kwargs):
        super().__init__(master, **kwargs)

        self.ms = master

        self.__connection = ConnectDB()

        self.__user_id = user_id

        self.__url_name_displayed = url_name_displayed

        self.__action = action

        self.connection = ConnectDB()

        self.title('Enter Credentials')

        place_window_in_center(master=self.ms, width=270, height=140, window_name=self, multiply=True)

        self.resizable(width=False, height=False)

        self.__user_field = ctk.CTkEntry(self, placeholder_text='Username', width=200)
        self.__user_field.grid(row=0, column=0, padx=35, pady=10)

        self.__pass_field = ctk.CTkEntry(self, placeholder_text='Password', width=200)
        self.__pass_field.grid(row=1, column=0)

        self.__submit_button = ctk.CTkButton(self, width=60, text='OK', command=self.__submit)
        self.__submit_button.grid(row=2, column=0, pady=10)

    def __submit(self):
        user = self.__user_field.get()
        password = self.__pass_field.get()
        if len(self.connection.check_credentials(username=user, password=password)) == 1:
            self.destroy()

            if self.__action == 'go_to_url':
                url = self.__connection.get_website(user_id=self.__user_id,
                                                    url_name_displayed=self.__url_name_displayed)
                credentials = self.__connection.get_website_credentials(user_id=self.__user_id,
                                                                        url_name_displayed=self.__url_name_displayed)
                browser = Browser()
                browser.go_to_url(url, credentials[0], credentials[1])

            elif self.__action == 'edit':
                EditInfoWindow(self.ms, user_id=self.__user_id, url_name_displayed=self.__url_name_displayed)

            elif self.__action == 'delete':
                self.__connection.delete_website(user_id=self.__user_id, url_name_displayed=self.__url_name_displayed)
                self.ms.logins_frame.refresh(on_login=False)

            else:
                NameError(f'{self.__action} is not a valid parameter!')

