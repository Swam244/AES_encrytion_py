import sys
import pyAesCrypt
import os
PATH = '{}'.format(sys.argv[1])
ORIGINAL_NAMES = []
allfiles = []
for root, subfiles, files in os.walk(PATH):
    for names in files:
        allfiles.append(os.path.join(root,names))
        # print(allfiles)


try:

    for file in allfiles:
        if names.endswith('.aes') is True:
            print(os.path.basename(file) + " --- The_File_is_Already_Encrypted")
        else:
            print("Encrypting...." +os.path.basename(file))
            pyAesCrypt.encryptFile('{}'.format((file)),
                                   '{}'.format((file)+(".aes")),
                                   passw='{}'.format('242004'),
                                   bufferSize=(64 * 1024))
            os.remove((file))

except ValueError:
    print("THE FILES CANNOT BE ENCRYPTED DUE TO SOME REASON......")