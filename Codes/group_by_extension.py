import os
import shutil
slash = "\\"
file_types = {

            "Text": [".doc", ".rtf", ".txt", ".wps", ".docx", ".md"],
            "Data": [".csv", ".pps", ".ppt", ".pptx", ".xml"],
            "Music": [".mp3", ".m4a", ".m4a",  ".m4p", ".mp3", "ogg"],
            "Video": [".3gp", ".avi", ".flv", ".m4v", ".mov", ".mp4", ".wmv"],
            "notes": [".pdf"],
            "Spreadsheet": [".xlr", ".xls", ".xlsx"],
            "apps": [".apk", ".app", ".exe", ".jar"],
            "Web": [".css", ".htm", ".html", ".js", ".php", ".xhtml"],
            "Compressed": [".rar", ".zip"],
            "Programmes": [".c", ".class", ".cpp", ".cs", ".java", ".py"],
            "Misc": [".ics", ".msi", ".torrent"],
            "images": [".jpeg", ".png", ".jpg", ".bmp"]
        }


class GroupByExtension:
    def __init__(self, path, files):
        self.path = path
        self.files = files

    def grpbyext(self, path, files):
        for file in files:
            # ext = os.path.splitext(file)[1]
            fflag = 0
            if os.path.isfile(file):
                if("." in file):
                    extension_name = file[file.index("."):]
                    for file_type, extensions in file_types.items():
                        if extension_name in extensions:
                            fflag = 1
                            folder_name = file_type
                            newpath = path + slash + folder_name
                            print(file, "moved to", newpath)
                            break
                    if (fflag == 0):
                        folder_name = "Other"
                        newpath = path + slash + folder_name
                        print(file, "moved to", newpath)
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                shutil.move(path + slash + file, newpath + slash + file)
