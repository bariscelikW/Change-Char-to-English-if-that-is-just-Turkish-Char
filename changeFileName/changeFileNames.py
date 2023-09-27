import os

# don't forget write your directory path !!!
path = "C:\\Users\\baris\\Desktop\\python\\changeFileName\\data"
dirList = os.listdir(path)

print("Files and directories in '", path, "' :")
print(dirList)

# to compare all file names in your path's file 
for fileName in dirList:
    # we created newFileName for changing the names of files 
    newFileName = fileName
    for c in fileName:
        #c is a letter, and we compared if Turkish char or not
        if c == 'ı':
            newFileName = newFileName.replace("ı", "i" )
        elif c == 'ğ':
            newFileName = newFileName.replace("ğ", "g" )
        elif c == 'ü':
            newFileName = newFileName.replace("ü", "u" )
        elif c == 'ş':
            newFileName = newFileName.replace("ş", "s" )
        elif c == 'ö':
            newFileName = newFileName.replace("ö", "o" )
        elif c == 'ç':
            newFileName = newFileName.replace("ç", "c" )
        elif c == 'Ğ':
            newFileName = newFileName.replace("Ğ", "G" )
        elif c == 'Ü':
            newFileName = newFileName.replace("Ü", "U" )
        elif c == 'Ş':
            newFileName = newFileName.replace("Ş", "S")
        elif c == 'İ':
            newFileName = newFileName.replace("İ", "I" )
        elif c == 'Ö':
            newFileName = newFileName.replace("Ö", "O" )
        elif c == 'Ç':
            newFileName = newFileName.replace("Ç", "C" )
    #title() function capitalizes the first letter of words
    newFileName = newFileName.title()
    #we get files path for changing path
    oldFilePath = os.path.join(path, fileName)
    newFilePath = os.path.join(path, newFileName)
    # we renamed our files
    os.rename(oldFilePath, newFilePath)
    
#if you are not encountered issues, that sentence will be printed
print("File names have been changed.")
