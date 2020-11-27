import os
import os.path


class OrganizeBySize:
    def __init__(self, path):
        self.path = path

    def size(self, path):
        size = 0
        fsizedicr = {'Megabytes': float(
            1)/(1024*1024)}
        for (path, dirs, files) in os.walk(path):
            for file in files:
                filename = os.path.join(path, file)
                size += os.path.getsize(filename)
        for key in fsizedicr:
            if(key == "Megabytes"):
                print("Folder Size: " + str(round(fsizedicr[key]*size, 2)) + "MB")
