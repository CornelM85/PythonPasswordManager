import customtkinter as ctk

from menu import MenuFrame

from logins import LoginsFrame

from utility_functions import place_window_in_center


class PasswordManager(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode('dark')

        self.resizable(width=False, height=False)

        self.title('Password Manager')
        self.__title_label = ctk.CTkLabel(self, text='Password Manager', text_color='white',
                                          font=ctk.CTkFont('times', size=30, weight='bold'))
        self.__title_label.grid(row=0, column=0, padx=20, pady=20)

        self.menu_frame = MenuFrame(master=self, fg_color='#242424')
        self.menu_frame.grid(row=1, column=0, padx=40, sticky='n')

        self.logins_frame = LoginsFrame(master=self, fg_color='#242424')
        self.logins_frame.grid(row=1, column=1)

        place_window_in_center(self, height=640, width=1000)


if __name__ == '__main__':
    game = PasswordManager()
    game.mainloop()