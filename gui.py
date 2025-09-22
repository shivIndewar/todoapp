import functions
import FreeSimpleGUI as sg



label1 = sg.Text("Select files to compress")
input_box1 = sg.InputText()
choose_button1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Select destination Folder")
input_box2 = sg.InputText()
choose_button2 = sg.FolderBrowse("Choose")

compress_Button = sg.Button("Compress")


window = sg.Window("File Compressor",
                   [[label1,input_box1,choose_button1],
                          [label2,input_box2,choose_button2],
                          [compress_Button]])

window.read()
print("Hello you are the great python developer")
window.close()
