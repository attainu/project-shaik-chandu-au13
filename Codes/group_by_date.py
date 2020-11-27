import os
import shutil
import time
from datetime import datetime


class Bydate:
    def __init__(self, path, files):
        self.path = path
        self.files = files

    def bydate(self, path, files):
        lis = os.listdir(path)
        lis.sort(key=lambda x: os.stat(os.path.join(path, x)).st_mtime)

        files = [file for file in os.listdir(
            path) if os.path.isfile(os.path.join(path, file))]
        os.chdir(path)

        for file in files:

            # Get the last modified time and the creation time

            modified_time_string = time.ctime(
                os.path.getmtime(os.path.join(path, file)))

            modified_datetime_obj = datetime.strptime(modified_time_string,
            '%a %b %d %H:%M:%S %Y')

            modified_date = str(modified_datetime_obj.day) + '-' + str(
            modified_datetime_obj.month) + '-'
            +str(modified_datetime_obj.year)

            if(os.path.isdir(modified_date)):
                shutil.move(os.path.join(path, file), modified_date)
            else:
                os.makedirs(modified_date)
                shutil.move(os.path.join(path, file), modified_date)
