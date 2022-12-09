from maya import cmds
import os
import json
import pprint

USERAPPDIR = cmds.internalVar(userAppDir=True)
print(USERAPPDIR)

DIR = r'C:\Users\james\Desktop\Ubisoft Interview\Environment Creator\Objects'

DIRECTORY = os.path.join(DIR, "controllerLibrary")

def createDirectory(directory=DIRECTORY):
    """

    Function:
        if the dir does not exist we create it.
    
    Args:
     directory(str): The directory to create
    
    """
    if not os.path.exists(directory):
        os.mkdir(directory)

class AssetLibrary(dict):

    # Info is a dictionary by default
    def save(self,name,directory=DIRECTORY, screenshot=True, **info):

        createDirectory(directory)

        path = os.path.join(directory, f'{name}.ma')

        infoFile = os.path.join(directory, f'{name}.json')

        info['name'] = name
        info['path'] = path

        cmds.file(rename=path)

        if cmds.ls(selection=True):
            cmds.file(force=True, type='mayaAscii', exportSelected=True)
        else:
            cmds.file(save=True, type='mayaAscii', force=True)

        if screenshot:
            info['screenshot'] = self.saveScreenshot(name,directory=directory)

        with open(infoFile, 'w') as f:
            # Indent everything by 4 spaces
            json.dump(info, f, indent=4)

        self[name] = info

    def updateDirectory(self, directory):
        self.clear()
        print("CALL")
        new_directory = directory
        self.find(directory = new_directory)
        
    def find(self, directory=DIRECTORY):

        self.clear()

        if not os.path.exists(directory):
            print("DOESNT")
            return
        
        files=os.listdir(directory)
        print("DIR")
        print(directory)
        
        mayaFiles = [f for f in files if f.endswith('.ma')]

        for ma in mayaFiles:
            name, ext = os.path.splitext(ma)
            path = os.path.join(directory,ma)

            infoFile = f'{name}.json'
            if infoFile in files:
                infoFile = os.path.join(directory, infoFile)

                with open(infoFile, 'r') as f:
                    info = json.load(f)
                    #pprint.pprint(info)
            else:
                info = {}
                print("No info found")

            screenshot = f"{name}.jpg"
            if screenshot in files:
                info['screenshot'] = os.path.join(directory,name)

            info['name'] = name
            info['path'] = path
            
            # Because the class inherits a dictionary, we can access it as a dictionary
            self[name] = info

        #pprint.pprint(self)


    def load(self, name):
        path = self[name]['path']
        print("____")
        print(path)
        # i is short for import but python reserves that keyword
        cmds.file(path, i=True, usingNamespaces=False)

    def saveScreenshot(self,name,directory=DIRECTORY):
        path = os.path.join(directory,f"{name}.jpg")

        cmds.viewFit()
        # This setAttr changes image format to jpeg. 8 is the value for jpeg in the image format list
        cmds.setAttr('defaultRenderGlobals.imageFormat', 8)

        cmds.playblast(completeFilename = path, forceOverwrite=True, format='image', width=200, height=200, showOrnaments=False, startTime=1, endTime=1, viewer=False)

        return path


#lib = AssetLibrary()
#lib.save('testicles')
#lib.find()
#lib.load('testicles')
