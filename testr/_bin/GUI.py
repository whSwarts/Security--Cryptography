import tkinter as tk
import pygubu
import Own as o, Transposition as transp, Vernam, Vigenere as v, convert_bytes as conv
from tkinter import filedialog
from PIL import ImageTk, Image


# from ConvertionFile import convert_bytes as conv

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
        self.set_title("Security project of S. Fourie and W. Swarts")

        # Set main menu
        self.mainmenu = menu = builder.get_object('mainmenu', self.master)
        self.set_menu(menu)


        # init callbacks
        builder.connect_callbacks(self)
        # self.master.protocol("WM_DELETE_WINDOW", self.on_close_program())

    #function callbacks
    def on_ok_button(self):
        key1 = self.builder.get_variable('key')
        self.key = key1.get()

    def on_encrypt(self):
        text_widget = self.builder.get_object('plaintext', self.master)
        self.plaintext = text_widget.get("1.0", tk.END)
        print(self.plaintext + "\t" + self.key)
        self.cipher = ""

        if (self.vigenere == 1):
            self.cipher = v.encryptMess(key=self.key, message=self.plaintext)
            # self.cipher = str(Vigenere.encryptMess(key=self.key, message=self.plaintext))
            print(self.cipher)
            print(len(self.cipher))

        if(self.vernem == 1):
            vernO = Vernam.VernamCipher(self.plaintext, self.key)
            self.cipher = vernO.giveVernam(self.plaintext, self.key)

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

    def on_open_file(self):
        self.file_path = filedialog.askopenfile()
        self.file_path
        list = self.file_path.readlines()
        for char in list:
            self.plaintext += char
        print(self.plaintext)

        text_widget = self.builder.get_object('plaintext', self.master)
        text_widget.delete("1.0", tk.END)
        text_widget.insert(tk.END, self.plaintext)
        self.file_path.close()

    def on_save_file(self):
        self.file_path = filedialog.asksaveasfilename()
        file = open(self.file_path, 'w')
        file.write(self.cipher)
        file.close()

    def on_save_button(self):
        self.on_save_file()

    def on_close_program(self):
        self.mainwindow.destroy()

    def on_import_image(self):
        self.file_path = filedialog.askopenfilename(title = "select an image to open")
        self.plaintext = conv.convertFileToString(self.file_path)
        if (self.vigenere == 1):
            self.cipher = v.encryptMess(key=self.key, message=self.plaintext)
            # self.cipher = str(Vigenere.encryptMess(key=self.key, message=self.plaintext))
            print(self.cipher)
            print(len(self.cipher))

        if(self.vernem == 1):
            vernO = Vernam.VernamCipher(self.plaintext, self.key)
            self.cipher = vernO.giveVernam(self.plaintext, self.key)

        elif (self.transposition == 1):

            k =0
            for char in self.key:
                self.k += ord(char)
            self.cipher = transp.encMessage(self.k, self.plaintext)
            print("run")

        elif (self.own == 1):
            print("run")
            self.cipher = o.encrypt(self.plaintext, self.key)
            with open('enc.enc', 'w') as file:
                file.write(str(self.cipher))
            self.plaintext = self.on_decrypt()
        conv.convertStringToFile(self.plaintext, "jpg")

    def on_decrypt(self):
        print("clicked")
        if (self.vigenere == 1):
            self.plaintext = v.decryptMess(key=self.key, message=self.cipher)
            # self.cipher = str(Vigenere.encryptMess(key=self.key, message=self.plaintext))
            print(self.cipher)
            print(len(self.cipher))
            print(self.plaintext)

        if(self.vernem == 1):
            vernO = Vernam.VernamCipher(self.cipher, self.key)
            self.plaintext = vernO.decryptVern(self.plaintext, self.key)
            print(self.plaintext)

        elif (self.transposition == 1):

            k =0
            for char in self.key:
                self.k += ord(char)
            self.plaintext = transp.decMessage(self.k, self.cipher)
            print("run")
            print(self.plaintext)

        elif (self.own == 1):
            print("run")
            self.plaintext = o.decrypt(self.cipher, self.key)
            print(self.plaintext)

        instxt = self.builder.get_object('plaintext', self.master)
        instxt.delete("1.0", tk.END)
        instxt.insert(tk.END, self.plaintext)

if __name__ == '__main__':
    root = tk.Tk()
    app = MyApplication(root)
    app.run()
