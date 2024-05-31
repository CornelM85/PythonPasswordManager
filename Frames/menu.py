import customtkinter as ctk


class MenuFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.logins_btn = ctk.CTkButton(self, text='Logins', height=10, font=ctk.CTkFont('times', size=20),
                                        fg_color='transparent', anchor='w', cursor='hand2', hover=False)
        self.logins_btn.grid(row=0, column=0)

        self.payments_btn = ctk.CTkButton(self, text='Payments', height=10, font=ctk.CTkFont('times', size=20),
                                          fg_color='transparent', anchor='w', cursor='hand2', hover=False)
        self.payments_btn.grid(row=1, column=0)

        self.__on_hover(self.logins_btn)
        self.__on_hover(self.payments_btn)

    def __on_enter(self, event):
        """
        Changing the text button color on hover_on
        """
        if event.widget.master.cget('text') == 'Logins':
            self.logins_btn.configure(text_color='grey')

        else:
            self.payments_btn.configure(text_color='grey')

    def __on_leave(self, event):
        """
        Changing the text button color on hover_out
        """
        if event.widget.master.cget('text') == 'Logins':
            self.logins_btn.configure(text_color='white')

        else:
            self.payments_btn.configure(text_color='white')

    def __on_hover(self, btn_name):
        """
        Combining the hover_on and hover_out functions in one
        """
        btn_name.bind('<Enter>', self.__on_enter, add='+')
        btn_name.bind('<Leave>', self.__on_leave, add='+')
