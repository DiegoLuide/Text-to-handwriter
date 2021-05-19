import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import InputText, Save, rgb, theme
import pywhatkit as kit

import sys, os, getpass, time

class Handwriter:
    def __init__(self):
        
        sg.theme('DarkAmber')

        layout = [
            [sg.Text('Write below the text you want convert to handwriting:')],
            [sg.Multiline(key='textinput')],
            [sg.Button('Confirm')]
        ] 

        window = sg.Window('Handwriter').layout(layout)

        #Capture variables of window
        self.event, self.values = window.Read()

        sg.popup('The archive has been saved in desktop or program directory. Please wait the main window of program close automatically.')
        
    # Return desktop directory in portuguese and english language name on linux and windows systems
    def getDesktopDirCompatible(self):
        if "linux" in sys.platform:
            if os.path.isdir(f"/home/{getpass.getuser()}/Desktop/"):
                return f"/home/{getpass.getuser()}/Desktop/"
            elif os.path.isdir(f"/home/{getpass.getuser()}/Área de trabalho/"):
                return f"/home/{getpass.getuser()}/Área de trabalho/"
        else:
            if os.path.isdir(f"C:\\Users\\{getpass.getuser()}\\Desktop\\"):
                return f"C:\\Users\\{getpass.getuser()}\\Desktop\\"
            elif os.path.isdir(f"C:\\Users\\{getpass.getuser()}\\Área de trabalho\\"):
                return f"C:\\Users\\{getpass.getuser()}\\Área de trabalho\\"
        return None

    #Creation variable, all handwriter process
    def Start(self):
        text = self.values['textinput']    

        #Convert text to image handwriter and save on desktop
        archive_path = self.getDesktopDirCompatible() if self.getDesktopDirCompatible() is not None else os.getcwd()
        file_name = f"handwriter_{time.ctime().split(' ')[3].replace(':','')}.png"
        
        kit.text_to_handwriting(
            text,
            os.path.join(archive_path, file_name),
            [0, 0, 0]
        )
        print(f"Saved archive on {archive_path}")

if __name__ == "__main__":
    screen = Handwriter()
    screen.Start()
