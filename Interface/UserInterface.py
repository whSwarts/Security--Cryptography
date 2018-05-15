import tkinter as tk
import pygubu
from tkinter import messagebox

class MyApplication(pygubu.TkApplication):
    key=""
    file_path =""
    plaintext = ""
    cipher = ""

    def _create_ui(self):
        # 1: Create a builder
        self.builder = builder = pygubu.Builder()

        # 2: Load an ui file
        builder.add_from_file('interfaceFile.ui')

        # 3: Create the widget using self.master as parent
        self.mainwindow = builder.get_object('main', self.master)

        # Set main menu
        self.mainmenu = menu = builder.get_object('mainmenu', self.master)
        self.set_menu(menu)

        modebtn = builder.get_object('text_mode_button', self.master)
        modebtn.configure(state=tk.DISABLED)
        # init callbacks
        builder.connect_callbacks(self)

    #function callbacks
    def on_ok_button(self):
        key1 = self.builder.get_variable('key')
        self.key = key1.get()





if __name__ == '__main__':
    root = tk.Tk()
    app = MyApplication(root)
    app.run()