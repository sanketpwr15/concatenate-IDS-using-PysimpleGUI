import PySimpleGUI as sg

# Define the layout of the window
layout = [
    [sg.Text("Enter the IDS:")],
    [sg.Multiline(key='-INPUT-', size=(40, 10))],
    [sg.Button("Concatenate"), sg.Button("clear")],
    [sg.Output(size=(40, 10), key='-OUTPUT-')],
    [sg.Button("COPY"),sg.Button("CLOSE")]
]

# Create the window
window = sg.Window("Concatenate - Sanket Pawar", layout)

# Event loop
while True:
    event, values = window.read()

    # Close the window
    if event == sg.WINDOW_CLOSED or event == "CLOSE":
        break
    #Clear the window
    if event == "clear":
        window['-INPUT-'].update('')
    #copy the values
    if event == "COPY":
        sg.clipboard_set(concatenated_text)   

# Concatenate the entered lines with a single quote
    text = values['-INPUT-']
    concatenated_text = "','".join(text.splitlines())
    print(concatenated_text)

# Close the window
window.close()
