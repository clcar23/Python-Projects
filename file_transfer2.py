#this will show how to move new/updated files only from folder to folder
import os
import shutil
from datetime import datetime, timedelta
import os.path
from datetime import time

#create a function that checks the time the file was modified
# and moves it if it meets the criteria
def updatedFiles():
    if recent_update_files <= past_24hrs:
        shutil.move(recent_update_files, destination)
    else:
        print("No recent updates to files.")

#create the source object
source = "/Users/clcar/OneDrive/Desktop/Folder_Source/"

#create the destination object
destination = r"\Users\clcar\OneDrive\Desktop\Folder_Destination"

#getting the current time for comparison
cur_time = datetime.now()
print("current time" + str(cur_time))

#changing the time until the past 24 hours
past_24hrs = cur_time - timedelta(hours = 24)


#getting the modification date of the files
mod_date_in_sec = os.path.getmtime("/Users/clcar/OneDrive/Desktop/Folder_Source/")

#converting the time from seconds into days
recent_update_files = datetime.fromtimestamp(mod_date_in_sec)

#executing the function
updatedFiles()




