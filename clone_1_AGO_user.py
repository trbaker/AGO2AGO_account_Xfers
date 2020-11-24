from arcgis import GIS

# Use admin logins on both organizations
source = GIS("https://xxxxxx.maps.arcgis.com", "", "")
target = GIS("https://xxxxxx.maps.arcgis.com", "", "")

itemTypes=''
sourceUser='xxxx'
targetUser='xxxx'

sourceUserObj = source.users.get(username=sourceUser)
for folder in sourceUserObj.folders:
    print(' ')
    print(folder['title'], " -- ", folder['id'], "  ")
    # clone folder name
    target.content.create_folder(folder=folder['title'], owner=targetUser)
    #targetUserObj.items(folder['title'])
    itemsInFolders = sourceUserObj.items(folder=folder['title'])
    #print(len(itemsInFolders))
    for i in itemsInFolders:
        print("     " +i.title + i.type)
        clItem = source.content.get(i.id)
        try:
            target.content.clone_items([clItem],
                                    search_existing_items=False,
                                    owner=targetUser
                                    )
        except:
            print("     ---" , 'Error on cloning: ', i.title)
            pass

print(' ')
print('Script complete.')