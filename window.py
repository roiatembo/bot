import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("TikTok Shop Bot")
        self.geometry(f"{1100}x{580}")

        # position constants
        self.topbar_pady = 20

        # configure grid layout (4x4)
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure((2, 3), weight=0)
        # self.grid_rowconfigure((0, 1, 2), weight=1)

        # create topbar frame with widgets
        # self.topbar_frame = customtkinter.CTkFrame(self, width=1100, corner_radius=0, height=30)
        # self.topbar_frame.grid(row=0, column=0, sticky="ew")
        # self.topbar_frame.grid_rowconfigure(0, weight=1)
        self.min_followers_entry =customtkinter.CTkEntry(self, placeholder_text="Min Followers", corner_radius=0, width=164, height=41)
        self.min_followers_entry.grid(row=1, column=2, columnspan=2, rowspan=2, pady=self.topbar_pady, padx=(198, 0))
        self.max_followers_entry =customtkinter.CTkEntry(self, placeholder_text="Max Followers", corner_radius=0, width=164, height=41)
        self.max_followers_entry.grid(row=1, column=4, columnspan=2, rowspan=2, pady=self.topbar_pady, padx=(41, 0))
        self.tiktok_shop_checkbox = customtkinter.CTkCheckBox(master=self, text="TikTok Shop")
        self.tiktok_shop_checkbox.grid(row=1, column=6, rowspan=2, padx=(38, 0))
        self.scan_stop_button = customtkinter.CTkButton(self, command=self.scan_stop_button_event, text="Scan", corner_radius=0, width=127, height=41)
        self.scan_stop_button.grid(row=1, column=8, pady=self.topbar_pady, padx=(61, 0))

        # results bar with widgets
        self.resultsbar_frame = customtkinter.CTkFrame(self, width=901, corner_radius=0)
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
        self.results_frame = customtkinter.CTkFrame(self, width=901, corner_radius=0)
        self.results_frame.grid(row=8, column=1, columnspan=9, rowspan=16, padx=(100, 0), pady=(0.15, 10), sticky="nsew")

        # footer content
        self.reports_button = customtkinter.CTkButton(self, command=self.reports_button_event, text="Reports")
        self.reports_button.grid(row=26, rowspan=2, column=1, columnspan=2, padx=100)
        self.appearance_switch = customtkinter.CTkSwitch(master=self, text="Light Mode")
        self.appearance_switch.grid(row=26, column=9, padx=10, pady=(0, 20))
        self.appearance_switch.select(from_variable_callback=self.change_appearance_mode_event)

        # self.appearance_mode_label = customtkinter.CTkLabel(self.topbar_frame, text="Appearance Mode:", anchor="w")
        # self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        # self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.topbar_frame, values=["Light", "Dark", "System"],
        #                                                                command=self.change_appearance_mode_event)
        # self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        # self.scaling_label = customtkinter.CTkLabel(self.topbar_frame, text="UI Scaling:", anchor="w")
        # self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        # self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.topbar_frame, values=["80%", "90%", "100%", "110%", "120%"],
        #                                                        command=self.change_scaling_event)
        # self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        # self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        # self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        # self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        # self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        

        # # set default values
        # # self.appearance_mode_optionemenu.set("Dark")
        # # self.scaling_optionemenu.set("100%")
        # self.textbox.insert("0.0", "CTkTextbox\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def scan_stop_button_event(self):
        print("sidebar_button click")
    
    def send_message_all_event(self):
        print("clicked send message")
    
    def reports_button_event(self):
        print("cliked report")


if __name__ == "__main__":
    app = App()
    app.mainloop()