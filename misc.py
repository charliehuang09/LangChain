import os
def getFiles(path):
    paths = []
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)):
            paths.append(os.path.join(path, filename))
        else:
            paths = paths + getFiles(os.path.join(path, filename))
            # paths.append(getFiles(os.path.join(path, filename)))
    return paths