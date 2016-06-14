import os
connect("weblogic", "Weblogic_2016")

lista = cmo.getAppDeployments()

for aplicacion in lista:
    print undeploy(aplicacion.getName())
