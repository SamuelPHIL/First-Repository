#!/usr/bin/env python3

import shutil

def check_disk_usage(disk, min_absolute, min_percent):
    """Returns true if there's enough free disk space, and false otherwise."""
    du = shutil.disk_usage(disk)
    percent_free = 100*du.free/du.total #calculate the percent of free space
    gigabytes_free = du.free/2**30 #calculate how many free gigabytes
    if percent_free < min_percent or gigabytes_free < min_absolute:
       return False
    return True

if not check_disk_usage("/", 2*2**30, 10):#check for at least 2GB and 10% free
    print("ERROR: Not enough disk space!")
    return 1
print("Everything ok.")
return 0
    

