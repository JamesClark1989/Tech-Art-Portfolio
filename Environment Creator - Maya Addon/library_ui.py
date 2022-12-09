import sys
# Append library path to import the ControllerLibrary
sys.path.append(r'C:\Users\james\Desktop\Ubisoft Interview\Environment Creator')

import environment_creator
from maya import cmds
from PySide2 import QtWidgets, QtCore, QtGui
import pprint

class AssetImporterUI(QtWidgets.QDialog):

    """
    The ControllerLibraryUI is a dialog that lets us save and import controllers
    """

    def __init__(self):
        super(AssetImporterUI, self).__init__()

        self.setWindowTitle('Object Importer')

        # The library variable points to an instance of our controller library
        self.library = environment_creator.AssetLibrary()

        # Everytime we create an instance we'll automatically build our UI and populate it
        self.buildUI()
        self.populate()

    def buildUI(self):
        """This method builds the UI"""
        print("Building UI")
        layout = QtWidgets.QVBoxLayout(self)

        # Load
        loadWidget = QtWidgets.QWidget()
        loadLayout = QtWidgets.QHBoxLayout(loadWidget)
        layout.addWidget(loadWidget)

        self.loadNameField = QtWidgets.QLineEdit()
        loadLayout.addWidget(self.loadNameField)

        loadBtn = QtWidgets.QPushButton('Load New Library')
        loadBtn.clicked.connect(self.open)
        loadLayout.addWidget(loadBtn)

        # Save
        saveWidget = QtWidgets.QWidget()
        saveLayout = QtWidgets.QHBoxLayout(saveWidget)
        layout.addWidget(saveWidget)

        self.saveNameField = QtWidgets.QLineEdit()
        saveLayout.addWidget(self.saveNameField)

        saveBtn = QtWidgets.QPushButton('Save To Current Library')
        saveBtn.clicked.connect(self.save)
        saveLayout.addWidget(saveBtn)

        # Parameters for our thumbnail size
        size = 80
        buffer = 12

        # This will create a grid list widget to display our controller thumbnails
        self.listWidget = QtWidgets.QListWidget()
        self.listWidget.setViewMode(QtWidgets.QListWidget.IconMode)
        self.listWidget.setIconSize(QtCore.QSize(size,size))
        self.listWidget.setResizeMode(QtWidgets.QListWidget.Adjust)
        self.listWidget.setGridSize(QtCore.QSize(size+buffer, size+buffer))
        layout.addWidget(self.listWidget)

        # This is our child widget that holds all the buttons
        btnWidget = QtWidgets.QWidget()
        btnLayout = QtWidgets.QHBoxLayout(btnWidget)
        layout.addWidget(btnWidget)
        
        importBtn = QtWidgets.QPushButton('Import!')
        importBtn.clicked.connect(self.load)
        btnLayout.addWidget(importBtn)

        refreshBtn = QtWidgets.QPushButton('Refresh')
        refreshBtn.clicked.connect(self.populate)
        btnLayout.addWidget(refreshBtn)

        closeBtn = QtWidgets.QPushButton('Close')
        closeBtn.clicked.connect(self.close)
        btnLayout.addWidget(closeBtn)



    def populate(self):
        """This clears the list widget and then repopulates with contents from our library"""

        self.listWidget.clear()

        if self.loadNameField.text().strip() == "":
            self.library.find()
        else:
            self.library.find(self.loadNameField.text())

        #self.library.find()
        

        # name,info is key,value
        for name, info in self.library.items():
            print(name, info)
            item = QtWidgets.QListWidgetItem(name)
            self.listWidget.addItem(item)

            screenshot = info.get('screenshot')
            if screenshot:
                icon = QtGui.QIcon(screenshot)
                item.setIcon(icon)

            item.setToolTip(pprint.pformat(info))
    
    def open(self):
        """This changes the current working folder"""
        name = self.loadNameField.text()
        if not name.strip():
            cmds.warning("You must give a name!")
            return

        self.library.updateDirectory(name)

        print("OK")

        self.populate()

    def load(self):
        """This loads the currently selected controller"""
        currentItem = self.listWidget.currentItem()

        if not currentItem:
            return

        name = currentItem.text()
        self.library.load(name)

    def save(self):
        """This saves the controller with the given file name"""
        name = self.saveNameField.text()
        if not name.strip():
            cmds.warning("You must give a name!")
            return

        self.library.save(name)
        self.populate()
        self.saveNameField.setText('')

def showUI():
    ui = AssetImporterUI()
    ui.show()
    return ui
    
ui = showUI()
