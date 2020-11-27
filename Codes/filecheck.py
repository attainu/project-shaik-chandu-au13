import os
from group_by_date import Bydate
from group_by_extension import GroupByExtension
from sort_by_size import OrganizeBySize

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
            files = os.listdir(path)
            group = GroupByExtension(path, files)
            group.grpbyext()
        elif choice == 2:
            path = input("enter the path")
            files = os.listdir(path)
            groupbydate = Bydate(path, files)
            groupbydate.bydate(path, files)
        elif choice == 3:
            path = input("enter the path")
            sort = OrganizeBySize(path)
            sort.size(path)
        elif choice == 4:
            break
        else:
            print("INVALID CHOICE")
