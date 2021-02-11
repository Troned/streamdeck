import eel
import os

eel.init(".")

@eel.expose()
def buttonPressed(id, path):
    print(f"{id} {path}")
    dir = os.listdir(path)
    print(dir)
    if str(id) in dir:
        print(id)
        eel.changePath(f"{path}{id}/")
    
    elif id == 12 and path[-3] == "/":
        eel.changePath(f"{path[:-2]}")
    
    else:
        try:
            file = open(f"{path}{id}.py")
        except:
            pass
        else:
            exec(file.read())


eel.start('index.html', size=(1000, 600))