serverConfig()

print 'lookup DefaultAuthenticator' 

password = 'weblogic1'

atnr=cmo.getSecurityConfiguration().getDefaultRealm().lookupAuthenticationProvider('DefaultAuthenticator')

print 'create group App-MHS-Users'
group = 'MiGrupo'
atnr.createGroup(group,group)

users = ['user1','user2']
for user in users:        
  print 'create user: ',user
  atnr.createUser(user,password,user)
  atnr.addMemberToGroup(group,user)


print 'create group App-MHS-Admin'
group = 'App-MHS-Admin'
atnr.createGroup(group,group)

users = ['admin1','admin2']
for user in users:        
  print 'create user: ',user
  atnr.createUser(user,password,user)
  atnr.addMemberToGroup(group,user)


print 'create group App-MHS-SB'
group = 'App-MHS-SB'
atnr.createGroup(group,group)

users = ['sbuser1','sbuser2']
for user in users:        
  print 'create user: ',user
  atnr.createUser(user,password,user)
  atnr.addMemberToGroup(group,user)
