import customtkinter as ctk
from Windows.verify_access_window import VerifyAccessWindow


class PropertiesWindow(ctk.CTkToplevel):
    def __init__(self, master, user_id, url_name_displayed, **kwargs):
        super().__init__(master, **kwargs)

        self.overrideredirect(True)

        self.ms = master

        self.__user_id = user_id

        self.__url_name_displayed = url_name_displayed

        self.__go_url_button = ctk.CTkButton(self, text='Go to site', fg_color='transparent', hover_color='green',
                                             command=self.__go_to_site, width=100, height=10)
        self.__go_url_button.pack()

        self.__edit_button = ctk.CTkButton(self, text='Edit', fg_color='transparent', hover_color='green',
                                           width=100, height=10, command=self.__edit)
        self.__edit_button.pack()

        self.__delete_button = ctk.CTkButton(self, text='Delete', fg_color='transparent', hover_color='green',
                                             width=100, height=10, command=self.__delete)
        self.__delete_button.pack()

        self.bind('<Leave>', self.__on_leave)

    def __go_to_site(self):
        VerifyAccessWindow(self.ms, user_id=self.__user_id, url_name_displayed=self.__url_name_displayed, action='go_to_url')

    def __delete(self):
        VerifyAccessWindow(self.ms, user_id=self.__user_id, url_name_displayed=self.__url_name_displayed, action='delete')

    def __edit(self):
        VerifyAccessWindow(self.ms, user_id=self.__user_id, url_name_displayed=self.__url_name_displayed, action='edit')

    def __on_leave(self, event):
        if 'ctkbutton' not in str(event.widget):
            self.destroy()


