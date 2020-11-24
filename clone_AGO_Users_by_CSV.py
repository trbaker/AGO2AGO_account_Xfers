# the script clones content from user A to user B. it draws user data from a CSV
# this script will error if user is not found (typically a NoneType error.)

#imports
from arcgis import GIS
import csv

# Use AGO admin logins on both source and target organizations
source = GIS("https://xxxx.maps.arcgis.com", "adminuser1", "adminpass1")
target = GIS("https://xxxx.maps.arcgis.com", "adminuser2", "adminpass2")

# variables
itemTypes=''


file = csv.reader(open('data/xfers.csv'), delimiter=',')
for line in file:
    targetUser=line[1].strip()
    sourceUser=line[0].strip()
    print(' ')
    print('user xfer: ', sourceUser, ' to ', targetUser)
    sourceUserObj = source.users.get(username=sourceUser)
    # root folder
    print(' Root folder:')
    itemsInRoot = sourceUserObj.items()
    #print(str(itemsInRoot))
    for k in itemsInRoot:
        clItem = source.content.get(k.id)
        run = target.content.clone_items([clItem],
                                        search_existing_items=False,
                                        owner=targetUser
                                     )
        print("   " + clItem.title + " " + clItem.type )
    #subfolders and data
    for folder in sourceUserObj.folders:
        print(' ' + folder['title'])
        # clone folder name
        target.content.create_folder(folder=folder['title'], owner=targetUser)
        #targetUserObj.items(folder['title'])
        itemsInFolders = sourceUserObj.items(folder=folder['title'])
        for i in itemsInFolders:
            #print("i loop:     " +i.title + " " + i.type)
            clItem = source.content.get(i.id)
            try:
                run=target.content.clone_items([clItem],
                                        folder=folder['title'],
                                        search_existing_items=False,
                                        owner=targetUser
                                        )
                print("        " + clItem.title + " " + clItem.type )
            except:
                print("     ---" , 'Error on cloning: ', i.title)
                pass

print(' ')
print('Script complete.')