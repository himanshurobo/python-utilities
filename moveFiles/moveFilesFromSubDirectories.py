import os
import shutil
#code copies from sub-directory

sourceFolder = './srcDir/'
destFolder = './destDir/'
extension = '.jpg'


def checkDir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


checkDir(destFolder)
for root, dirs, files in os.walk(sourceFolder):
     for file in files:
        with open(os.path.join(root, file), "r") as auto:
            # print root
            if (file.endswith(extension)):
                # print file
                old_destination = root +'/'+file
                new_destination = destFolder + file
                print (old_destination)
                print (new_destination)
                shutil.copy(old_destination,new_destination)