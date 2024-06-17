from pathlib import Path
from datetime import datetime,timedelta


filePathToCheck = Path("D:\\ISTAD\\Python")
target = Path("C:\\Users\\ROG\\Desktop\\homework8\\backUpFile")
stats = filePathToCheck.stat()

def checkDays(filePathToCheck)->None:
    checkFiles = []
    checkDay = int(input("Days: "))
    if filePathToCheck.exists():
        for entry in filePathToCheck.iterdir():
            if entry.is_file():
                createDate = stats.st_birthtime
                createDateTime = datetime.fromtimestamp(createDate)
                dayCreated = datetime.now() - createDateTime
                if dayCreated >= timedelta(days=checkDay):
                    formatDay = f"Day: {dayCreated.days}"
                    formatFileName = f"File:{entry.name}"
                    checkFiles.append([formatFileName,formatDay])
                    try:
                        with open(entry, "rb") as copyBinary:
                            data = copyBinary.read()
                        with open(target / entry.name, "wb") as pasteBinary:
                            pasteBinary.write(data)
                        print(f"Copied: {entry.name} to {target}")
                    except Exception as e:
                        print(f"Failed to copy {entry.name}: {e}")
                else:
                    print("Dont have older file !")
    else:
        print("File doesnt exist")
    id = 1
    for check in checkFiles:
        print(f"{id}: {check}")
        id+=1
        
def deleteFile(filePathToCheck) -> None:
    fileName = input("Delete File: ")
    filePath = filePathToCheck / fileName
    if filePath.exists() and filePath.is_file():
        ask = input(f"Delete this '{fileName}' ? [Y/N]: ").lower()
        if ask == "yes" or ask == 'y':
            try:
                filePath.unlink()
                print(f"File '{fileName}' has been delete !")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Cancel delete file")
    else:
        print(f"File '{fileName}' isnt exist '{filePathToCheck}' !")

def searchFile(filePathToCheck) -> None:
    checkFiles = []
    checkName = input("Check Name: ")
    if filePathToCheck.exists():
        for entry in filePathToCheck.iterdir():
            if entry.is_file() and checkName in entry.name:
                    checkFiles.append(entry.name)
    for file in checkFiles:
        print(f"File: {file}")
                    

searchFile(filePathToCheck)