import os
allfiles = []
for root, subfiles, files in os.walk("E:\\Data_\\Visual_Basic\\"):
	for names in files:
		allfiles.append(os.path.join(root,names))
print('\n',allfiles)
for i in allfiles:
    print(i)
os.system("PAUSE")


