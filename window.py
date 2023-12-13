import tkinter
import tkinter.messagebox
import customtkinter
from tiktok import Tiktok

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # tiktok instance
        self.tiktok = Tiktok()

        # configure window
        self.title("TikTok Shop Bot")
        self.geometry(f"{1100}x{580}")

        # position constants
        self.topbar_pady = 20

        # configure grid layout (4x4)
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure((2, 3), weight=0)
        # self.grid_rowconfigure((0, 1, 2), weight=1)

        self.min_followers_entry =customtkinter.CTkEntry(self, placeholder_text="Min Followers", corner_radius=0, width=164, height=41)
        self.min_followers_entry.grid(row=1, column=2, columnspan=2, rowspan=2, pady=self.topbar_pady, padx=(198, 0))
        self.max_followers_entry =customtkinter.CTkEntry(self, placeholder_text="Max Followers", corner_radius=0, width=164, height=41)
        self.max_followers_entry.grid(row=1, column=4, columnspan=2, rowspan=2, pady=self.topbar_pady, padx=(41, 0))
        self.tiktok_shop_checkbox = customtkinter.CTkCheckBox(master=self, text="TikTok Shop")
        self.tiktok_shop_checkbox.grid(row=1, column=6, rowspan=2, padx=(38, 0))
        self.scan_stop_button = customtkinter.CTkButton(self, command=self.scan_stop_button_event, text="Scan", corner_radius=0, width=127, height=41)
        self.scan_stop_button.grid(row=1, column=8, pady=self.topbar_pady, padx=(61, 0))

        # results bar with widgets
        self.resultsbar_frame = customtkinter.CTkFrame(self, width=901, corner_radius=0, border_width=1, border_color="white")
        self.resultsbar_frame.grid(row=5, column=1, rowspan=3, columnspan=9, padx=(100, 0), pady=(39, 0), sticky="nsew")
        self.select_all_checkbox = customtkinter.CTkCheckBox(master=self.resultsbar_frame, text="", corner_radius=0)
        self.select_all_checkbox.grid(row=6, column=1, padx=(20, 0), pady=10)
        self.handle_label = customtkinter.CTkLabel(self.resultsbar_frame, text="Handle")
        self.handle_label.grid(row=6, column=1, padx=(80, 0))
        self.name_label = customtkinter.CTkLabel(self.resultsbar_frame, text="Name")
        self.name_label.grid(row=6, column=4, padx=(163, 0))
        self.followers_label = customtkinter.CTkLabel(self.resultsbar_frame, text="Followers")
        self.followers_label.grid(row=6, column=6, padx=(191, 0))
        self.send_message_all_label = customtkinter.CTkButton(self.resultsbar_frame, command=self.send_message_all_event, text="Send Message")
        self.send_message_all_label.grid(row=6, column=8, padx=(143, 0))

        # results frame
        self.results_frame = customtkinter.CTkScrollableFrame(self, width=901, corner_radius=0, border_width=1, border_color="white")
        self.results_frame.grid(row=8, column=1, columnspan=9, rowspan=16, padx=(100, 0), pady=(0.15, 10), sticky="nsew")

        # footer content
        self.reports_button = customtkinter.CTkButton(self, command=self.reports_button_event, text="Reports")
        self.reports_button.grid(row=26, rowspan=2, column=1, columnspan=2, padx=100)
        self.appearance_switch = customtkinter.CTkSwitch(master=self, text="Light Mode")
        self.appearance_switch.grid(row=26, column=9, padx=10, pady=(0, 20))
        # self.appearance_switch.select(from_variable_callback=self.change_appearance_mode_event)

        # self.appearance_mode_label = customtkinter.CTkLabel(self.topbar_frame, text="Appearance Mode:", anchor="w")
        # self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        # self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.topbar_frame, values=["Light", "Dark", "System"],
        #                                                                command=self.change_appearance_mode_event)
        # self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
 
   
    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def show_results(self, tiktok_users):
        rownumber = 8
        for user in tiktok_users:
            user_id = user["id"]
            self.select_checkbox = customtkinter.CTkCheckBox(master=self.results_frame, text="", corner_radius=0)
            self.select_checkbox.grid(row=rownumber, column=1, padx=(20, 0), pady=5, sticky="w")
            self.handle = customtkinter.CTkLabel(self.results_frame, text=user["unique_id"], anchor="w", justify="left")
            self.handle.grid(row=rownumber, column=1, padx=(80, 0), sticky="w")
            self.name = customtkinter.CTkLabel(self.results_frame, text=user["nickname"], anchor="w", justify="left")
            self.name.grid(row=rownumber, column=4, padx=(80, 0), sticky="w")
            self.followers = customtkinter.CTkLabel(self.results_frame, text=user["follower_count"], anchor="w", justify="left")
            self.followers.grid(row=rownumber, column=6, padx=(75, 0), sticky="w")
            self.send_message_button = customtkinter.CTkButton(self.results_frame, command=self.send_message_all_event, text="Send Message")
            self.send_message_button.grid(row=rownumber, column=8, padx=(170, 0))
            rownumber += 1

    def scan_stop_button_event(self):
        current_text = self.scan_stop_button.cget("text")

        if current_text == "Scan":
            min_followers_value = self.min_followers_entry.get()
            max_followers_value = self.max_followers_entry.get()
            self.scan_stop_button.configure(text="Stop")

            # check if max followers is set
            if max_followers_value == "":
                max_followers_value = 1000000000;
            else:
                int(max_followers_value)
            
            if min_followers_value != "":
                tiktok_users = self.tiktok.run_scan(int(min_followers_value), max_followers_value)
                self.scan_stop_button.configure(text="Scan")
                self.show_results(tiktok_users[:20])

        
        if current_text == "Stop":
            self.scan_stop_button.configure(text="Scan")
    
    def send_message_all_event(self):
        print("clicked send message")
    
    def reports_button_event(self):
        print("cliked report")


# if __name__ == "__main__":
#     app = App()
#     app.mainloop()