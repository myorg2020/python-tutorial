import os

# print(os.path) # To see from which python path locally this is being called
# print(dir(os)) # To see which all functions/methods are part of this module

# print(os.getcwd()) # To check present working directory
# os.mkdir('test') # To create a folder with name as 'test'
# os.rmdir('test') # To remove the fodler test

# print(os.path.exists('test')) # Returns True if folder test exists otherwise will return false

# # Using this way by adding a condition we can check if that folder exists or not, and create if not
# if os.path.exists('test'):
#     print("folder tests exists")
# else:
#     print(f"folder test has been created: {os.mkdir('test')}")

# open('file.txt','a').close() # This way will create a file named file.txt with append permission, if file exists it won't recreate and won't give any Error

os.chdir('/Users/amiteshranjan/python-tutorial')
print(f"current path is: {os.chdir('/Users/amiteshranjan/python-tutorial')}")
if os.path.exists('test'):
    print("Folder with name test Already exists")
else:
    print("Folder with name test has been created")
    os.mkdir('test')