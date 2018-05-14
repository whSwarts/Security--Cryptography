import tkinter as tk
import pygubu


class MyApplication(pygubu.TkApplication):

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


if __name__ == '__main__':
    root = tk.Tk()
    app = MyApplication(root)
    app.run()