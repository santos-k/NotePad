from tkinter import *
from tkinter import filedialog
from tkinter.scrolledtext import *
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox
import os

file_path = ""
# head, tail = os.path.split(file_path)
filename = "Untitled"


def save_file():
    str1 = text.get(1.0, "end-1c")  # get the entire text from text box
    fileptr = open("file.txt", "w")  # open file name in write mode
    fileptr.write(str1)  # write the file
    fileptr.close()  # close the file
    print("Saved")


def save():
    global filename
    global file_path
    if filename == "Untitled":  # if file unsaved
        try:
            files = [('Text Document', '*.txt'), ('All Files', '*.*'), ('Python Files', '*.py')]
            file = asksaveasfile(filetypes=files, defaultextension=files)  # file instance
            new_file_name = file.name  # get file path
            head, tail = os.path.split(
                new_file_name)  # tail store extact file name, where head store path before file name(head, tail is variable can be anything)
            str2 = text.get(1.0, "end-1c")
            file.write(str2)
            file_path = new_file_name
            filename = tail
            root.title(tail + "- NotePad")
            # print(file_path)
            # print(filename)
        except Exception as e:
            messagebox.showinfo("Alert",e)
    else:  # if file has been already saved and file name displayed on title
        str2 = text.get(1.0, "end-1c")
        fileptr = open(file_path, "w")
        fileptr.write(str2)
        fileptr.close()
        # print("Saved")


def open_file():
    global file_path
    global filename
    try:
        filename1 = filedialog.askopenfilename(initialdir="/", title="Open",
                                               filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
        # print(filename) #return D:/hello.txt
        path1, file1 = os.path.split(filename1)
        root.title(file1 + "- NotePad")  # set title
        filename = file1  # update global filename
        file_path = filename1  # update global file path
        openfile = open(filename1, "r")
        # reading text from opened file and displaying to text box
        for i in openfile:
            text.insert(INSERT, i)

    except Exception as e:
        messagebox.showinfo("Alert", e)


def Exit_Save():
    str = text.get(1.0, "end-1c")
    if str == "":
        root.destroy()
    elif str > "":
        try:
            save()
            root.destroy()
        except:
            pass


def about_msg():
    messagebox.showinfo("About", "Python Notepad 1.0\nAll rights are reserved.")


def feature_soon():
    messagebox.showinfo("Information", "Feature adding soon...\nThanks for using NotePad!!")


def on_close():
    str = text.get(1.0, "end-1c")
    # print(str)
    if filename == "Untitled" and str == "":
        root.destroy()
    elif filename == "Untitled" and str != "":
        if messagebox.askyesno("NotePad", "Do you wan to save changed to Untitled?"):
            save()
            root.destroy()
        else:
            root.destroy()
    else:
        root.destroy()
    # elif filename != "Untitled" and str != "":


root = Tk()
root.geometry("800x500")
root.iconbitmap("Notepad.ico")
root.title(filename + "- NotePad")

menubar = Menu(root)
# file, edit, format, view, help

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=feature_soon)
filemenu.add_command(label="New Window", command=feature_soon)
filemenu.add_command(label="Open...", command=open_file)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Save As...", command=save)
filemenu.add_separator()
filemenu.add_command(label="Page Setup...", state=DISABLED)
filemenu.add_command(label="Print...", state=DISABLED)
filemenu.add_separator()
# filemenu.add_command(label="Exit",command=lambda :exit())
filemenu.add_command(label="Exit", command=Exit_Save)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Copy", state=DISABLED)
editmenu.add_separator()
editmenu.add_command(label="Paste", state=DISABLED)
editmenu.add_command(label="Delete", state=DISABLED)
editmenu.add_separator()
editmenu.add_command(label="Search with Bing...", state=DISABLED)
editmenu.add_command(label="Find...", state=DISABLED)
editmenu.add_command(label="Find Next", state=DISABLED)
editmenu.add_command(label="Find Previous", state=DISABLED)
editmenu.add_command(label="Replace...", state=DISABLED)
editmenu.add_command(label="GoTo...", state=DISABLED)
editmenu.add_separator()
editmenu.add_command(label="Select All", state=DISABLED)
editmenu.add_command(label="Date/Time", state=DISABLED)

formatmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Format", menu=formatmenu)
formatmenu.add_command(label="Word Wrap", command=feature_soon)
formatmenu.add_command(label="Font...", command=feature_soon)

viewmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="View", menu=viewmenu)
viewmenu.add_command(label="Zoom", command=feature_soon)
viewmenu.add_checkbutton(label="Status Bar")

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="View Help", command=feature_soon)
helpmenu.add_command(label="Send Feedback", command=feature_soon)
helpmenu.add_separator()
helpmenu.add_command(label="About Notepad", command=about_msg)
root.config(menu=menubar)

# text = Text(root)
# text.pack(fill='both', padx=5, pady=5)

text = ScrolledText(root, undo=True)
# text['font'] = ('Arial Black', '15')
text.pack(expand=True, fill='both', padx=5, pady=5)

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
