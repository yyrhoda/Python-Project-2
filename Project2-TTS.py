'''
Rhoda Yayra Kuworde
10973048
BMEN
'''

import PySimpleGUI as sg
import pyttsx3

TTS_Engine = pyttsx3.init()
Type_voices = TTS_Engine.getProperty('voices')



layout = [    [sg.Text('Select the type of voice:',text_color='#000000', background_color='pink'),sg.Radio('Male', 'RADIO1', default=True, key='male', background_color='pink'),sg.Radio('Female', 'RADIO1', key='female', background_color='pink')],
     [sg.Text('Enter text to speak:',text_color='#000000', background_color='pink')],
          
    [sg.InputText(key='input'),sg.Button('Speak',button_color='green')],
   
    
]

window = sg.Window('TEXT TO SPEECH APP', layout,background_color='blue')

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Speak':
        text = values['input']
        if values['male']:
            TTS_Engine.setProperty('voice', Type_voices[1].id)
        elif values['female']:
           TTS_Engine.setProperty('voice', Type_voices[0].id) 
    
        TTS_Engine.say(text)
        TTS_Engine.runAndWait()

window.close()