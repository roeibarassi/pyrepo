import os ,sys
import hashlib

def md5sum(filename):
    hash = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(128 * hash.block_size), b""):
            hash.update(chunk)
    return hash.hexdigest()


def checkDup(detailedFilesList):
    newList = detailedFilesList
    resultList = []
    for i in range(0, len(newList) - 1):
        for j in range(i+1,len(newList)):
            if newList[i][1] == newList[j][1]:
                resultList.append(newList[i][0])
    return resultList

##Main
def main():
    searchDir = 'c:\\temp\\logs'
    filesList = []
    if os.path.exists(searchDir):
        for path, dirs, files in os.walk(searchDir):
            for filename in files:
                filesList.append([os.path.join(path, filename) ,  md5sum(os.path.join(path, filename))])
        print checkDup(filesList)
    else:
        print "Folder not exists"

if __name__ == "__main__":
    main()