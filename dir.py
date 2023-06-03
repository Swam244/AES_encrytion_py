import os
allfiles = []
i = input("Enter Address: ")
for root, subfiles, files in os.walk(str(i)):
	for names in files:
		allfiles.append(os.path.join(root,names))
print('\n',allfiles)
for i in allfiles:
    print(i)
os.system("PAUSE")


