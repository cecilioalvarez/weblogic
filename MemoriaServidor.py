import os
connect("weblogic","Weblogic_2016")
domainRuntime()
cd("/ServerRuntimes/AdminServer/JVMRuntime/AdminServer")
print "Maquina Virtual" + get("JavaVMVendor")
print "Memoria Total:" + str(get("HeapSizeCurrent"))
print "Memoria libre :" + str(get("HeapFreeCurrent"))
print "Memoria Usada :" + str(get("HeapSizeCurrent")- get("HeapFreeCurrent"))
