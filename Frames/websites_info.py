import customtkinter as ctk
from PIL import Image
from db_connection import ConnectDB
from Windows.properties_window import PropertiesWindow
from utility_functions import resource_path


class WebsitesInfo(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.ms = master

        connection = ConnectDB()
        web_list = connection.get_all_websites(str(self.ms.logins_frame.user_id))
        for i, website in enumerate(web_list):
            image = ctk.CTkImage(Image.open(resource_path(f'Images/{website[3]}')), size=(15, 15))
            icon = ctk.CTkLabel(self.ms.logins_frame.web_sites, image=image, width=20, height=10, text='')
            icon.grid(row=i, column=0, padx=(0, 18))

            url = ctk.CTkLabel(self.ms.logins_frame.web_sites, height=10, width=210, text=website[2],
                               text_color='#00A2E8', cursor='hand2',
                               font=ctk.CTkFont('times', size=18, underline=True), anchor='w')
            url.grid(row=i, column=1)
            url.bind('<Button-1>', self.on_click, add='+')

            user = ctk.CTkLabel(self.ms.logins_frame.web_sites, height=10, width=210, text=f'{len(website[0]) * '$'}',
                                font=ctk.CTkFont('times', size=12), anchor='w')
            user.grid(row=i, column=2)

            password = ctk.CTkLabel(self.ms.logins_frame.web_sites, height=10, width=210, text=f'{len(website[1]) * '*'}',
                                    font=ctk.CTkFont('times', size=18), anchor='w')
            password.grid(row=i, column=3)

    def on_click(self, event):
        user_id = self.ms.logins_frame.user_id
        url_text_displayed = event.widget.master.cget('text')
        pointer_x = event.widget.master.winfo_pointerx()
        pointer_y = event.widget.master.winfo_pointery()
        properties_window = PropertiesWindow(self.ms, user_id=user_id, url_name_displayed=url_text_displayed)
        properties_window.geometry('{}x{}+{}+{}'.format(100, 65, pointer_x, pointer_y))

