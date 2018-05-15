import tkinter as tk
import pygubu
from tkinter import messagebox
from Vigenere import Vigenere as v
from Vernam import Vernam
from Own import Own as o
from Transposition import Transposition as transp

class MyApplication(pygubu.TkApplication):
    key=""
    file_path =""
    plaintext = ""
    cipher = ""
    vernem= 0
    transposition = 0
    vigenere= 0
    own = 0
    k = 0

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

    def on_encrypt(self):
        text_widget = self.builder.get_object('plaintext', self.master)
        plaintext = text_widget.get("1.0", tk.END)
        self.cipher = ""

        if (self.vigenere == 1):
            self.cipher = v.encryptMess(key=self.key, message=plaintext)
            # self.cipher = str(Vigenere.encryptMess(key=self.key, message=self.plaintext))
            print(self.cipher)
            print(len(self.cipher))

        if(self.vernem == 1):
            vernO = Vernam.VernamCipher(plaintext, self.key)
            self.cipher = vernO.giveVernam(plaintext, self.key)

        elif (self.transposition == 1):

            k =0
            for char in self.key:
                self.k += ord(char)
            self.cipher = transp.encMessage(self.k, self.plaintext)
            print("run")

        elif (self.own == 1):
            print("run")
            self.cipher = o.encrypt(self.plaintext, self.key)

        print(self.cipher)
        printwidget = self.builder.get_object('ciphertext', self.master)
        printwidget.delete("1.0", tk.END)
        printwidget.insert(tk.END, self.cipher)

    def on_vernem(self):
        self.vernem = 1
        self.transposition = 0
        self.vigenere = 0
        self.own = 0

    def on_vigenere(self):
        self.vernem = 0
        self.transposition = 0
        self.vigenere = 1
        self.own = 0

    def on_transposition(self):
        self.vernem = 0
        self.transposition = 1
        self.vigenere = 0
        self.own = 0

    def on_own(self):
        self.vernem = 0
        self.transposition = 0
        self.vigenere = 0
        self.own = 1






if __name__ == '__main__':
    root = tk.Tk()
    app = MyApplication(root)
    app.run()