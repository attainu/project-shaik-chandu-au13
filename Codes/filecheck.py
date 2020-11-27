import os
from group_by_date import Bydate
from group_by_extension import GroupByExtension
from group_by_size import *


# group = GroupByExtension(path, files)

if __name__ == "__main__":
    print("*************** FILE ORGANIZER *************")
    while True:
        print("""
        press 1 to group the files by their extensions
        press 2 to group the files by their last modified date
        press 3 to organize files by their size
        press 4 to exit""")

        choice = int(input("Enter your choice"))

        if choice == 1:
            path = input("enter the path")
            group = GroupByExtension(path)
            group.grpbyext(path)
        elif choice == 2:
            path = input("enter the path")
            files = os.listdir(path)
            groupbydate = Bydate(path, files)
            groupbydate.bydate(path, files)
        elif choice == 3:
            DIRECTORY_PATH = input("enter the path")
            SIZEORGANISER(DIRECTORY_PATH)
        elif choice == 4:
            break
        else:
            print("INVALID CHOICE")
