import PySimpleGUI as sg
from zip_extractor import extract_archive

sg.theme("Black")

lable1 = sg.Text("Select archive                   ")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="archive")

lable2 = sg.Text("Select destination directory")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")
output_lable = sg.Text(key="output", text_color="green")

window = sg.Window("Archive Extractor", 
                   layout=[[lable1, input1, choose_button1],
                           [lable2, input2, choose_button2],
                           [extract_button, output_lable]])

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
            break
    
    archive_path = values["archive"]
    folder = values["folder"]
    extract_archive(archive_path, folder)
    window["output"].update(value="Extraction completed")
    
window.close()