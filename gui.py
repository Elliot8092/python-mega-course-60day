# Modules
import time
import PySimpleGUI as gui

# Local Module
from modules import functions

lable = gui.Text("Type in a to-do")
input_box = gui.InputText(tooltip="Enter todo")
add_button = gui.Button("Add")

window = gui.Window('My To-Do app', layout=[[lable, input_box, add_button]])
window.read()
window.close()
