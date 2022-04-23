#~ IMPORTS ~#
import os

#~ CLASS ~#
class Sorter:
    def __init__(self,argpath):
        self.path = argpath
        if not self.path:
            self.path = os.path.dirname(os.path.abspath(__file__))

    def getpath(self):
        return self.path

    def sortfiles(self):
        files = os.listdir(self.path)
        for f in files:
            flist = f.split(".")
            try:
                extension = flist[len(flist) - 1]
                if extension = "gz":
                    extension = "tar.gz"
                if not os.path.exists(f"{self.path}/{extension}"):
                    os.makedirs(f"{self.path}/{extension}")
                os.replace(f"{self.path}/{f}", f"{self.path}/{extension}/{f}") 
            except:
                pass
