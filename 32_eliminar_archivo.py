#Archivo python

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
  
print("Para borrar carpetas mirar codigo")
#os.rmdir("myfolder") solo borrará carpetas vacias.