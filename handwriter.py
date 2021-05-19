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

        sg.popup('The archive has been saved in desktop.')

    #Creation variable, all handwriter process
    def Start(self):
        text = self.values['textinput']    

        #Convert text to image handwriter and save on desktop
        if "linux" or "darwin" in sys.platform:
            desktop_path = f"/home/{getpass.getuser()}/Desktop/"
        else:
            desktop_path = f"C:\\Users\\{getpass.getuser()}\\Desktop\\"
            
        file_name = f"handwriter_{time.ctime().split(' ')[3].replace}.png"
        
        if os.path.isdir(desktop_path):
            kit.text_to_handwriting(
                text,
                os.path.join(desktop_path, file_name),
                [0, 0, 0]
            )
        else:
            kit.text_to_handwriting(
                text,
                os.path.join(os.getcwd(), file_name),
                [0, 0, 0]
            )

if __name__ == "__main__":
    screen = Handwriter()
    screen.Start()
