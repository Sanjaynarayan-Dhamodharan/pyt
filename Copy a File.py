# copyfile() = copies contents of a file
# copy() = copy file() + permission mode + destination can be a directory
# copy2() = copy() + copes metadata (file's creation and modification times)

import shutil

shutil.copy2('test.txt','C:\\Users\\Lenovo\\OneDrive\\Documents')# src,dst
