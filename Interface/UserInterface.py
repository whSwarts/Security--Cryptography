#!/bin/python
"""
Hello World, but with more meat.
"""

import wx
import os
import Vernam as Vern

class SecurityGUI(wx.Frame):
    """
    A Frame that says Hello World
    """

    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(SecurityGUI, self).__init__(*args, **kw)

        # create a panel in the frame
        pnl = wx.Panel(self)
        self.CreateToolBar()
        # # and put some text with a larger bold font on it
        # st = wx.StaticText(pnl, label="Hello World!", pos=(25,25))
        # font = st.GetFont()
        # font.PointSize += 10
        # font = font.Bold()
        # st.SetFont(font)

        # create a menu bar
        self.makeMenuBar()

        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("Willem Swarts - 24223468\t\tStephan Fourie - studentNo")


    def CreateToolBar(self):
        tools = wx.ToolBar()
        vernItem = tools.AddRadioTool(label="Vernam Method", toolId=1)
        self.SetToolBar(tools)
        self.Bind(wx.EVT_RADIOBUTTON)

    def makeMenuBar(self):


        # Make a file menu with Hello and Exit items
        fileMenu = wx.Menu()
        # The "\t..." syntax defines an accelerator key that also triggers
        # the same event
        helloItem = fileMenu.Append(-1, "Open\tCtrl-H",
                "Select a file to open")
        fileMenu.AppendSeparator()
        # When using a stock ID we don't need to specify the menu item's
        # label
        exitItem = fileMenu.Append(wx.ID_EXIT)

        # Now a help menu for the about item
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        # Make the menu bar and add the two menus to it. The '&' defines
        # that the next letter is the "mnemonic" for the menu item. On the
        # platforms that support it those letters are underlined and can be
        # triggered from the keyboard.
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.OnOpenfile, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)


    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)


    def OnOpenfile(self, event):
        """Say hello to the user."""
        dialog = wx.FileDialog(self, message="choose a file",
                      defaultDir=os.getcwd(),
                      defaultFile="",
                      style=wx.FD_OPEN| wx.FD_MULTIPLE| wx.FD_CHANGE_DIR)
        # dialog.ShowFullScreen()
        if dialog.ShowModal() == wx.ID_OK:
            paths = dialog.GetPaths()
            print
        dialog.Destroy()

    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox("This is a wxPython Hello World sample",
                      "About Hello World 2",
                      wx.OK|wx.ICON_INFORMATION)


if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = SecurityGUI(None, title='Security project')
    frm.Show()
    app.MainLoop()