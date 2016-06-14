from java.io import FileInputStream
 
propInputStream = FileInputStream("misscripts/parametros3.properties")
configProps = Properties()
configProps.load(propInputStream)
 
domainName=configProps.get("domain.name")
adminURL=configProps.get("admin.url")
adminUserName=configProps.get("admin.userName")
adminPassword=configProps.get("admin.password")
realmName=configProps.get("security.realmName")
 
totalGroups_to_Create=configProps.get("total.groups")
totalUsers_to_Create=configProps.get("total.username")
 
connect(adminUserName, adminPassword, adminURL)
serverConfig()
authenticatorPath= '/SecurityConfiguration/' + domainName + '/Realms/' + realmName + '/AuthenticationProviders/DefaultAuthenticator'
print authenticatorPath
cd(authenticatorPath)
print ' '
print ' '
 
print 'Creating Groups . . .'
i=1
while (i <= int(totalGroups_to_Create)) :
    groupName = configProps.get("create.group.name."+ str(i))
    groupDescription = configProps.get("create.group.description."+ str(i))
    try:
        cmo.createGroup(groupName , groupDescription)
        print '-----------Group Created With Name : ' , groupName
    except:
        print '*************** Check If The Group With the Name : ' , groupName ,' already Exists...'
    i = i + 1
print ' '
print ' '
 
print 'Creating Users . . .'
x=1
while (x <= int(totalUsers_to_Create)):
    userName = configProps.get("create.user.name."+ str(x))
    userPassword = configProps.get("create.user.password."+ str(x))
    userDescription = configProps.get("create.user.description."+ str(x))
    try:
        print userName, ','  ,userPassword, ',',  userDescription
        cmo.createUser(userName , userPassword , userName)
        print '-----------User Created With Name : ' , userName
    except :
        print '*************** Check If the User With the Name : ' , userName ,' already Exists...'
    x = x + 1
print ' '
print ' '
 
print 'Adding Group Membership of the Users:'
for y in 1,2:
   grpName = configProps.get("create.group.name."+ str(y))
   groupMembers= configProps.get("create.group.name."+ str(y) + ".members")
   usrName=''
   for member in groupMembers:
        if member == ",":
            cmo.addMemberToGroup(grpName,usrName)
            print 'USER:' , usrName , 'Added to GROUP: ' , grpName
            usrName=''
        else:
            usrName=usrName+member
print ' '
#print ' '