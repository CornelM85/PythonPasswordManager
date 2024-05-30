import customtkinter as ctk

from master_login_window import MasterLoginWindow
from master_register_window import MasterRegisterWindow


class MasterLogin(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.ms = master

        self.__greetings_label = ctk.CTkLabel(self, height=10, text=f'Hello, ', font=ctk.CTkFont('times', size=18))

        self.__name_label = ctk.CTkLabel(self, height=10, text='',
                                         font=ctk.CTkFont('times', size=18), text_color='coral')

        self.__sign_in = ctk.CTkButton(self, height=10, text='Sign In', font=ctk.CTkFont('times', size=18),
                                       fg_color='transparent', command=self.__on_click)
        self.__sign_in.grid(row=0, column=0)

        self.__register = ctk.CTkButton(self, height=10, text='Register', font=ctk.CTkFont('times', size=18),
                                        fg_color='transparent', command=self.__is_logout)
        self.__register.grid(row=0, column=1)

    def __on_click(self):
        master_login_window = MasterLoginWindow(self.master)
        master_login_window.grab_set()

    def is_login(self, username):
        self.__sign_in.destroy()

        self.__greetings_label.grid(row=0, column=0)

        self.__name_label.configure(text=username)
        self.__name_label.grid(row=0, column=1, padx=(0, 20))

        self.__register.configure(text='Logout')
        self.__register.grid(column=2)

    def __is_logout(self):
        if self.__register.cget('text') == 'Logout':
            self.__greetings_label.forget()
            self.__name_label.forget()

            self.ms.logins_frame.user_id = None

            self.__sign_in = ctk.CTkButton(self, height=10, text='Sign In', font=ctk.CTkFont('times', size=18),
                                           fg_color='transparent', command=self.__on_click)
            self.__sign_in.grid(row=0, column=0)

            self.__register.configure(text='Register')
            self.__register.grid(column=1)

        else:
            register_window = MasterRegisterWindow(self.master)
            register_window.grab_set()