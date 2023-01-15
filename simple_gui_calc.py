import PySimpleGUI as sg

sg.theme('Dark Blue 3')

layout = [[sg.Text("Please enter the first number: "), sg.InputText()],
          [sg.Text("Please enter the second number: "), sg.InputText()],
          [sg.Text("Result: "), sg.Input(key="result")],
          [sg.Button('Sum'), sg.Button('Multiply'), sg.Button('Divide'), sg.Button('Substract')]]


def sum_calc(x: int, y: int):
    print(x+y)
    return x + y


def multiply(x: int, y: int):
    return x * y


def substract(x: int, y: int):
    return x-y


def divide(x: int, y: int):
    return x/y


window = sg.Window("Calculator", layout)
while True:
    event, values = window.read()
    if event == "Sum":
        x = sum_calc(int(values[0]), int(values[1]))
        window['result'].update(x)
    elif event == "Multiply":
        x = multiply(int(values[0]), int(values[1]))
        window['result'].update(x)
    elif event == 'Divide':
        x = divide(int(values[0]), int(values[1]))
        window['result'].update(x)
    elif event == "Substract":
        x = substract(int(values[0]), int(values[1]))
        window['result'].update(x)
    elif event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
