import customtkinter as ctk
from utility_functions import place_window_in_center
from db_connection import ConnectDB
from .field_update_window import FieldUpdateWindow


class EditInfoWindow(ctk.CTkToplevel):
    def __init__(self, master, user_id, url_name_displayed, **kwargs):
        super().__init__(master, **kwargs)

        self.__user_id = user_id
        self.__url_name_displayed = url_name_displayed

        self.__connection = ConnectDB()

        self.ms = master

        self.title('Edit Information')

        place_window_in_center(master=self.ms, width=270, height=160, window_name=self, multiply=True)

        self.resizable(width=False, height=False)

        self.url_field = ctk.CTkLabel(self, width=150, height=10, text='',
                                      font=ctk.CTkFont('times', size=18), anchor='w')
        self.url_field.grid(row=0, column=0, pady=10, padx=30)

        self.url_field_button = ctk.CTkButton(self, text='Edit', width=30, fg_color='transparent', hover_color='green',
                                              command=self.__new_url_name_displayed)
        self.url_field_button.grid(row=0, column=1, sticky='e')

        self.user_field = ctk.CTkLabel(self, width=150, height=10, text='',
                                       font=ctk.CTkFont('times', size=18), anchor='w')
        self.user_field.grid(row=1, column=0)

        self.user_field_button = ctk.CTkButton(self, text='Edit', width=30, fg_color='transparent', hover_color='green',
                                               command=self.__new_login_name)
        self.user_field_button.grid(row=1, column=1, sticky='e')

        self.pass_field = ctk.CTkLabel(self, width=150, height=10, text='',
                                       font=ctk.CTkFont('times', size=18), anchor='w')
        self.pass_field.grid(row=2, column=0, pady=10)

        self.pass_field_button = ctk.CTkButton(self, text='Edit', width=30, fg_color='transparent', hover_color='green',
                                               command=self.__new_login_password)
        self.pass_field_button.grid(row=2, column=1, sticky='e')

        self.submit = ctk.CTkButton(self, width=100, text='OK', command=self.__submit)
        self.submit.grid(row=4, columnspan=2, sticky='e')

        self.__get_data()

    def __submit(self):
        pass

    def __get_data(self):
        credentials = self.__connection.get_website_credentials(user_id=self.__user_id,
                                                                url_name_displayed=self.__url_name_displayed)

        self.url_field.configure(text=self.__url_name_displayed)
        self.user_field.configure(text=credentials[0])
        self.pass_field.configure(text=credentials[1])

    def __new_url_name_displayed(self):
        field_update = FieldUpdateWindow(self, user_id=self.__user_id, url_name_displayed=self.__url_name_displayed,
                                         field_update='url')
        field_update.grab_set()

    def __new_login_name(self):
        field_update = FieldUpdateWindow(self, user_id=self.__user_id, url_name_displayed=self.__url_name_displayed,
                                         field_update='user')
        field_update.grab_set()

    def __new_login_password(self):
        field_update = FieldUpdateWindow(self, user_id=self.__user_id, url_name_displayed=self.__url_name_displayed,
                                         field_update='password')
        field_update.grab_set()

