import os
import shutil
#code copies from sub-directory

sourceFolder = './SegmentationClass'
destFolder = './SegmentationClass_folder/'
extension = '.png'
matchName = 'imageDownload_2020-10-28_folderImage'


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
                splitName = file.split(matchName)[-1]
                splitName = splitName.split('_')[0]
                print(file,splitName)
                old_destination = root +'/'+file
                new_destination = destFolder + splitName
                checkDir(new_destination)
                new_destination = new_destination + '/' + file
                print (old_destination)
                print (new_destination)
                shutil.copy(old_destination,new_destination)
                # os.rename(old_destination,new_destination)


#  nohup python src/models/train.py -c data/config.json &
