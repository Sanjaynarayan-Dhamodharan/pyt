import os
import shutil

path = "sample"

try:
    #os.remove(path)            Delete a file
    #os.rmdir(path)             Delete an empty directory
    #shutil.rmtree(path)        Delete a directory containing files, rmtree means remove tree
except FileNotFoundError:
    print("That file is not found")
except PermissionError:
    print("You do not have the permission to access that file")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path+" was deleted")