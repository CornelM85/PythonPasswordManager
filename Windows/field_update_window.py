import customtkinter as ctk
from utility_functions import place_window_in_center
from db_connection import ConnectDB


class FieldUpdateWindow(ctk.CTkToplevel):
    def __init__(self, master, user_id, url_name_displayed, field_update=('url' or 'user' or 'password'), **kwargs):
        super().__init__(master, **kwargs)

        self.__user_id = user_id
        self.__url_name_displayed = url_name_displayed
        self.__field_update = field_update

        self.__set_height = 80

        self.ms = master

        self.title('Add New Value')

        self.resizable(width=False, height=False)

        self.new_value = ctk.CTkEntry(self, placeholder_text='New Value', width=200, height=10)
        self.new_value.grid(row=0, column=0, pady=10, padx=35)

        self.__submit_button = ctk.CTkButton(self, width=60, text='OK', command=self.__submit)
        self.__submit_button.grid(row=1, column=0)

        if self.__field_update == 'password':
            self.__set_height = 110
            self.confirm_new_value = ctk.CTkEntry(self, placeholder_text='Confirm New Value', width=200, height=10)
            self.confirm_new_value.grid(row=1, column=0)
            self.__submit_button.grid(row=2, column=0, pady=10)

        place_window_in_center(master=self.ms, width=270, height=self.__set_height, window_name=self, multiply=True)

    def __submit(self):
        value = self.new_value.get()
        if value != '':
            connection = ConnectDB()

            if self.__field_update == 'url':
                connection.update_website_url_name_displayed(user_id=self.__user_id,
                                                             url_name_displayed=self.__url_name_displayed,
                                                             new_value=value)
                self.ms.url_field.configure(text=value)

            elif self.__field_update == 'user':
                connection.update_website_login_name(user_id=self.__user_id,
                                                     url_name_displayed=self.__url_name_displayed,
                                                     new_value=value)
                self.ms.user_field.configure(text=value)

            elif (self.__field_update == 'password' and
                  self.new_value.cget('text') == self.confirm_new_value.cget('text')):
                connection.update_website_login_password(user_id=self.__user_id,
                                                         url_name_displayed=self.__url_name_displayed,
                                                         new_value=value)
                self.ms.pass_field.configure(text=value)

            else:
                pass

            self.destroy()

