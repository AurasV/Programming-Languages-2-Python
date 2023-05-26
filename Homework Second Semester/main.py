import PySimpleGUI as sg
import pyttsx3


def gui():
    engine = pyttsx3.init()
    sg.theme('dark2')
    result = []
    layout = [
        [sg.Input(key='_in_')],
        [
            sg.Button('1', key='1'),
            sg.Button('2', key='2'),
            sg.Button('3', key='3')
        ],
        [
            sg.Button('4', key='4'),
            sg.Button('5', key='5'),
            sg.Button('6', key='6')
        ],
        [
            sg.Button('7', key='7'),
            sg.Button('8', key='8'),
            sg.Button('9', key='9')
        ],
        [
            sg.Button('+', key='+'),
            sg.Button('-', key='-'),
            sg.Button('*', key='*')
        ],
        [
            sg.Button('/', key='/'),
            sg.Button('=', key='='),
            sg.Button('C', key='C')
        ],
        [
            sg.Button('PLAY', key='P'),
            sg.Button('0', key='0')
        ],
    ]
    window = sg.Window('Calculator', layout)

    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break

        elif event in '0123456789':
            result.append(event)
            window['_in_'].update(''.join(result))
        elif event in '-+/*':
            if result and result[-1].isdigit():
                result.append(event)
                window['_in_'].update(''.join(result))
        elif event == '=':
            if result:
                new_result = str(eval(''.join(result)))
                window['_in_'].update(new_result)
                result = [new_result]
        elif event == 'C':
            result = []
            window['_in_'].update('')
        elif event == 'P':
            audio = window['_in_'].get()
            new_audio = audio.replace('*', ' multiplied by ')
            new_audio = new_audio.replace('/', ' divided by ')
            new_audio = new_audio.replace('-', ' minus ')
            engine.say(new_audio)
            engine.runAndWait()


if __name__ == '__main__':
    gui()
