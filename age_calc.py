import PySimpleGUI as sg
from datetime import datetime
from time import time, sleep

sg.theme('Dark Blue 3')

layout = [[sg.Text("Please enter the day (e.g. 1): "), sg.InputText()],
          [sg.Text("Please enter the month (e.g. 2): "), sg.InputText()],
          [sg.Text("Please enter the year (e.g. 2003): "), sg.InputText()],
          [sg.Text("Calculated Age: "), sg.Input(key="result")],
          [sg.Button('Age')]]


def get_age(day, month, year):
    date_s = day+month+year
    date = datetime(year=int(date_s[2:6]), month=int(
        date_s[1]), day=int(date_s[0]))
    today = date.today()
    age = today.year - date.year - \
        ((today.month, today.day) < (date.month, date.day))
    return age


#day = "2"
#month = "3"
#year = "2002"
#result = get_age(day, month, year)


window = sg.Window("Calculator", layout, no_titlebar=False, location=(
    0, 0), size=(800, 600))

while True:
    event, values = window.read()
    if event == "Age":
        x = get_age(str(values[0]), str(values[1]), str(values[2]))
        print("Test: " + str(x))
        window['result'].update(x)
    elif event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
