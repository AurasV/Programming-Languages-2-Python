import PySimpleGUI as sg
import io
import os
from PIL import Image
import configparser

config = configparser.ConfigParser()
config.read("config/image_extension.ini")

val1_1 = config['ALL']['first']
val1_2 = config['ALL']['second']
val2_1 = config['JPEG']['first']
val2_2 = config['JPEG']['second']
val3_1 = config['PNG']['first']
val3_2 = config['PNG']['second']

file_types = [(val1_1, val1_2), (val2_1, val2_2), (val3_1, val3_2)]


def gui():
    sg.theme('DarkBlue')
    layout = [
        [sg.Image(key='_image_')],
        [sg.Text("Image File:"),
         sg.Input(key='_file_'),
         sg.FileBrowse(file_types=file_types),
         sg.Button("Load Image", key='_load_image_')
         ],
    ]
    window = sg.Window("Viewer of an album of images", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "_load_image_":
            filename = values["_file_"]
            if os.path.exists(filename):
                image = Image.open(values["_file_"])
                image.thumbnail((600, 600))
                image_in_bytes = io.BytesIO()
                image.save(image_in_bytes, format="PNG")
                window["_image_"].update(data=image_in_bytes.getvalue())
    window.close()


if __name__ == '__main__':
    gui()
