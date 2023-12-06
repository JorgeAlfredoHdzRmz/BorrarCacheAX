import os
from tkinter.messagebox import showwarning
import subprocess
import time

#Localizar la carpeta del usuario donde se van a borrar los archivos
appdata = os.path.expanduser('~') + '\\AppData\\Local'
ax = "Ax32.exe" #Nombre del programa a cerrar

try:
    subprocess.call(f"taskkill /f /im {ax}", shell=True) #Se ejecuta la siguiente linea de CMD para cerrar el ERP Microsoft Dynamics AX 2012 R2/R3

    #Como en la carpeta donde se va a eliminar la caché, no hay mas archivos importantes, realizamos distinción entre carpetas y archivos para que elimine los archivos.
    for archivo in os.listdir(appdata):
        ruta_archivo = os.path.join(appdata, archivo)
        
        if os.path.isfile(ruta_archivo):
            os.remove(ruta_archivo)

    print("Archivos eliminados exitosamente en la carpeta:", appdata)

    time.sleep(5)#Esperamos 5 segundos
    subprocess.Popen(ax, shell=True) #Volvemos a abrir el ERP Microsoft Dynamics AX 2012 R2/R3

except Exception as e: #Cuando haya alguna excepcion o error, se mostrará en pantalla
    showwarning(title="Advertencia", message=e)