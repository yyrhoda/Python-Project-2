'''
Rhoda Yayra Kuworde
10973048
BMEN
'''


import PySimpleGUI as sg
import qrcode
import os

layout = [
    [sg.Input(key="-WEB ADDRESS-", size = (25,1))],
    [sg.Image(key="-IMAGE-", size=(300,300))],
    [sg.Button("Generate QR Code")]
]


window = sg.Window('QR Code Generator', layout,background_color='#45818e')


def generate_qr_code(Link):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(Link)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color='white')
    file_name = "qr_code" + ".png"
    path = os.path.join(os.getcwd(), file_name)
    img.save(path)
    return path

while True:
    event, values = window.read()
    if event == 'Exit' or event== sg.WINDOW_CLOSED:
        break
    if event == "Generate QR Code":
        web_address = values["-WEB ADDRESS-"]
        qr_code_image_path = generate_qr_code(web_address)
        window["-IMAGE-"].update(filename=qr_code_image_path)
        window.close()