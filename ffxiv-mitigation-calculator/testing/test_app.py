from customtkinter import *
from PIL import Image, ImageTk

class App(CTk):
    '''
    Main app class for CTk.
    '''

    def __init__(self):
        super().__init__()
        self.geometry('1280x720')
        set_appearance_mode("light")
        self.title('FFXIV Mitigation Calculator')

        '''
        Create app structure.
        '''

        self.main_title()
        self.select_job()

        # Create button to calculate

        # get font
        button_1 = CTkFont(family="Lexend Deca",size=20)
        fire_emoji=ImageTk.PhotoImage(
            Image.open("ffxiv-mitigation-calculator/resources/images/fire_emoji.png").resize((15,15)))

        btn=CTkButton(master=self,
            text='Calculate',
            corner_radius=5,
            fg_color="#7cbdd9",
            hover_color="#c7eeff",
            text_color="#000",
            image=fire_emoji,
            font=button_1,
            command=self.calculate_value)
        btn.place(relx=0.2,rely=0.9,anchor='center')
        



    def main_title(self):

        '''
        Creates main title at the top of the program. 
        '''

        # get font for heading
        heading_1 = CTkFont(family="Lexend Deca",size=30)

        title=CTkLabel(master=self,text="FFXIV Mitigation Calculator",font=heading_1)
        title.place(relx=0.5,rely=0.1,anchor='center')

    def select_job(self):

        '''
        Creates dropdown to select the job. Once selected, it will show the user
        said job's corresponding cooldowns.
        '''

        job_dropdown=CTkComboBox(master=self,
                                values=["Paladin","Warrior","Dark Knight","Gunbreaker",
                                                   "White Mage","Scholar","Astrologian","Sage",
                                                   "Monk","Dragoon","Ninja","Samurai","Reaper","Viper",
                                                   "Bard","Machinist","Dancer",
                                                   "Black Mage","Summoner","Red Mage","Pictomancer"],
                                fg_color="#7cbdd9",
                                border_color="#5a8ba1",
                                button_color="#5a8ba1")
        job_dropdown.place(relx=0.2,rely=0.2,anchor="center")

    def calculate_value(self):

        '''
        Creates button to execute calculations once previous options are selected.
        '''

        print('test success')


    '''
    # user input to save sheet for future loading
    def getSheetName():
        nameInput=Label(window,text='Enter sheet name:')
        nameInput.pack()
    '''

app=App()
app.mainloop()
