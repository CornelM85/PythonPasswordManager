import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

from db_connection import ConnectDB

from utility_functions import place_window_in_center


class MasterRegisterWindow(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.ms = master

        self.title('Enter Information')

        place_window_in_center(master=self.ms, width=270, height=200, window_name=self, multiply=True)

        self.resizable(width=False, height=False)

        self.user_field = ctk.CTkEntry(self, placeholder_text='Username', width=200)
        self.user_field.grid(row=0, column=0, padx=35, pady=10)

        self.email_field = ctk.CTkEntry(self, placeholder_text='Email', width=200)
        self.email_field.grid(row=1, column=0)

        self.pass_field = ctk.CTkEntry(self, placeholder_text='Password', width=200)
        self.pass_field.grid(row=2, column=0, pady=10)

        self.confirm_pass_field = ctk.CTkEntry(self, placeholder_text='Confirm Password', width=200)
        self.confirm_pass_field.grid(row=3, column=0)

        self.submit = ctk.CTkButton(self, width=60, text='OK', command=self.__submit)
        self.submit.grid(row=4, column=0, pady=10)

    def __submit(self):
        user = self.user_field.get()
        password = self.pass_field.get()
        confirm_password = self.confirm_pass_field.get()
        email = self.email_field.get()

        if user == '' or password == '' or confirm_password == '' or email == '':
            self.__message('All the fields must be filled!')

        elif self.__check_field_text(user) is False:
            self.__message('Username field contain spaces!')

        elif self.__check_valid_email() is False:
            self.__message('Not a correct email address!')

        elif self.__check_field_text(email) is False:
            self.__message('Email field contain spaces!')

        elif self.__check_field_text(password) is False or self.__check_field_text(confirm_password) is False:
            self.__message('The password fields contain spaces!')

        elif password != confirm_password:
            CTkMessagebox(self, title='Alert', width=150, height=50,
                          icon='warning', message='Password fields don\'t match!', option_1='OK')

        else:
            connection = ConnectDB()
            connection.add_user(username=user, password=password, email=email)
            self.destroy()

    def __check_field_text(self, input_text):
        for char in input_text:
            if char == ' ':
                return False

    def __message(self, message_text):
        CTkMessagebox(self, title='Alert', width=150, height=50,
                      icon='warning', message=message_text, option_1='OK')

    def __check_valid_email(self):
        email = self.email_field.get()
        if email.count('@') == 1:
            return True
        else:
            return False
