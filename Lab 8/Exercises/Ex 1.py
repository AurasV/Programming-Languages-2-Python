import PySimpleGUI as sg
import os


name = "Frimu Aurel-Viorel"
group = "1211EC"
country = "Romania"
address = "Splaiul Independentei Nr 290"


def gui():
    sg.theme('LightBlue1')
    layout = [
        [sg.Button('Student name', key='_name_'),
         sg.Button('Student Group', key='_group_'),
         sg.Button('Country', key='_country_'),
         sg.Button('Address', key='_address_')],
        [sg.Button('Generate Info', key='_gen info_')],
        [sg.Button('Remove Info', key='_rem info_')]]

    window = sg.Window('My first laboratory application using pysimplegui module', layout)

    while True:
        event, values = window.read()

        match event:
            case '_name_':
                sg.popup(name)
            case '_group_':
                sg.popup(group)
            case '_country_':
                sg.popup(country)
            case '_address_':
                sg.popup(address)
            case '_gen info_':
                try:
                    f = open("informations.txt", "x")
                    f.write(name + "\n" + group + "\n" + country + "\n" + address)
                    sg.popup("informations.txt file was generated with success!")
                    f.close()
                except FileExistsError:
                    sg.popup_error("File already created!")
            case '_rem info_':
                try:
                    os.remove("informations.txt")
                    sg.popup("informations.txt file has been removed with success!")
                except FileNotFoundError:
                    sg.popup_error("Nothing to be done.")
            case None:
                break


if __name__ == '__main__':
    gui()
