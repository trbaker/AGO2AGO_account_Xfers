
# Use admin logins on both organizations
gis = GIS("https://education.maps.arcgis.com", "tbaker", "naish101")

from arcgis import GIS
itemTypes=''
targetUser='Esri_GeoInquiry_Grade4'

print("List user items by folder (F) or file type (T)?")
val = input("F or T: ")

targetUserObj = gis.users.get(username=targetUser)
items = gis.content.search("owner:"+targetUser,
                                item_type='*',
                                sort_field="Title",
                                max_items=500)

# ################## List items by file type ##############################
if val is "T":
    for j in items:
        if j.type:
            if not (j.type in itemTypes):
                itemTypes=j.type + ', ' + itemTypes
    #print(itemTypes.split(','))
    itemList=itemTypes.split(',')  #converts string to list
    itemList = [x.strip(' ') for x in itemList]  #removes white space within list elements
    itemList = list(filter(None, itemList))    # removes any empty list elements
    itemList=sorted(itemList)       # sorts the list by alpha, caps first
    #print(itemList)

    for t in itemList:
        print(' ')
        print(t, '*********************************')
        items2 = gis.content.search("owner:"+targetUser,
                                   item_type=t,
                                   sort_field="Title",
                                   max_items=500)
        for s in items2:
            print('  ',s.title)

# ################## List items by folder ##############################
elif val is "F":
    # FOLDERS view
    for folder in targetUserObj.folders:
        print(' ')
        print(folder['title'], " ::: ", folder['id'], "  *********************************")
        #targetUserObj.items(folder['title'])
        itemsInFolders = targetUserObj.items(folder=folder['title'])
        #print(len(itemsInFolders))
        for i in itemsInFolders:
            print("      " +i.title+" ::: "+i.id)

# ##################      ERROR        ##############################
else:
    print("It appears you do not know your f from your t.")

