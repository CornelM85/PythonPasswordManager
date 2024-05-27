import customtkinter as ctk

from utility_functions import place_window_in_center


class MasterLoginWindow(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.ms = master

        self.title('Enter Credentials')

        place_window_in_center(master=self.ms, width=270, height=140, window_name=self, multiply=True)

        self.resizable(width=False, height=False)

        self.user_field = ctk.CTkEntry(self, placeholder_text='Username', width=200)
        self.user_field.grid(row=0, column=0, padx=35, pady=10)

        self.pass_field = ctk.CTkEntry(self, placeholder_text='Password', width=200)
        self.pass_field.grid(row=1, column=0)

        self.submit = ctk.CTkButton(self, width=60, text='OK', command=self.__submit)
        self.submit.grid(row=2, column=0, pady=10)

    def __submit(self):
        user = self.user_field.get()
        password = self.pass_field.get()
        if user == 'User' and password == '1234':
            self.ms.master_login_frame.is_login(user)
            self.destroy()

