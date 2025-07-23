# -----------------------------
# File Handling Project
# -----------------------------
# Description: Perform file operations - Create, Read, Update, Delete
# Author: Ayush Vishwakarma
# -----------------------------

from pathlib import Path
import os

# for files
def folderfiles():
    path = Path('')
    items = list(path.rglob('*'))
    for i in items:
        print(i)

# for creating a file
def createfile():
    try:
        folderfiles()
        name = input("📁  Enter the file name with extension:")
        
        p = Path(name)

        if not p.exists():

            with open(p,'w') as fs:

                response = input("📝  Do you want to add data to the file? (yes/no):")

                if response == "Yes" or response == "yes":
                    data = input("✍️   Please enter your data: ")
                    fs.write(data)
                    print("✅  File created successfully with data.")
                else:
                    print("📂  Empty file created.")

        else:
            print("⚠️  File already exists.")

    except Exception as err:
        print(f"❌  Error: {err}")   

# for reading a file

def readfile():
    try:
        folderfiles()
        name = input("📖  Enter the file name to read:")
        p = Path(name)

        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()  
                print("\n📄 File Content:\n" + "-"*20)           
                print(data)
                print("-"*20)
                print("✅ File read successfully.")
        else:
            print("⚠️ File does not exist.")

    except Exception as err:
        print(f"❌ Error: {err}")        

# To update the file

def updatefile():
    try:
        folderfiles()
        name = input("✏️ Enter the name of the file to update:")
        p = Path(name)

        if p.exists():
            print("\nChoose an update action:")
            print("1️⃣  Rename file")
            print("2️⃣  Overwrite file content")
            print("3️⃣  Append to file")
 
            res = int(input("🔢  Enter your choice (1/2/3): "))

            if res == 1:
                name2 = input("Enter the new name -:")
                p2 = Path(name2)
                p.rename(p2)
                print("✅  File renamed successfully.")

            elif res == 2:
                with open(p,'w') as fs:
                    data = input("🆕  Enter new data to overwrite: ")
                    fs.write(data)
                    print("✅  File content overwritten.")

            elif res == 3:
                with open(p,'a') as fs:
                    data = input("Enter data to append:")
                    fs.write(" "+data)
                    print("✅  Data appended to file.")
            else:
                print("Invalid action selected!")
        else:
            print("⚠️  File does not exist")
        print("File Updated successfully")        
    except Exception as err:
        print(f"❌  Error: {err}")

# To delete the file

def deletefile():
    try:
        folderfiles()
        name = input("Enter the file name to delete: ")
        p = Path(name)

        if p.exists():
            os.remove(name)
            print("File removed successfully.")
        else:
            print("⚠️  File does not exist.")    
    except Exception as err:
        print(f"❌  Error: {err}")

# Main menu

print("\n📁  File Manager Console")
print("--------------------------")
print("1️⃣  Create a file")
print("2️⃣  Read a file")
print("3️⃣  Update a file")
print("4️⃣  Delete a file")
print("--------------------------")

check = int(input("Please Enter your response :-"))

if check == 1:
    createfile()

elif check == 2:
    readfile()

elif check == 3:
    updatefile()    

elif check == 4:
    deletefile()    

else:
    print("Invalid option selected.")


