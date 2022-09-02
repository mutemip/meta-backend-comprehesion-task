import importlib
import filechanges

def changes():
    try:
        importlib.reload(filechanges)
        filechanges.print_changes()
    except:
        pass

for i in range(3):
    changes()
    input("Hit enter to reload....")