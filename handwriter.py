import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import InputText, Save, rgb, theme
import pywhatkit as kit

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
        kit.text_to_handwriting(text, "C:\\Users\\Diego Luide\\Desktop\\Handwriter.png", [0, 0, 0])

screen = Handwriter()
screen.Start()