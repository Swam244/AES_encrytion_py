import pyAesCrypt
import os
import sys

condition_list = []
PATH = '{}'.format(sys.argv[1])
allfiles = []
for root, subfiles, files in os.walk(PATH):
    for names in files:
        allfiles.append(os.path.join(root,names))
	# print(allfiles)



for file in allfiles:
    if file.endswith('.aes') is True :
        # condition_list.append(os.path.basename(file))
        print("Decrypting.....{}".format(os.path.basename(file)))
        pyAesCrypt.decryptFile('{}'.format((file)),
                               '{}'.format((file).replace('.aes','')),
                               '{}'.format('242004'),
                               bufferSize=(64 * 1024))
        os.remove((file))

    else:
        print('{} -- '.format(file)+"Not Encrypted")

# if len(condition_list)>0:
#     print("...DECRYPTION_COMPLETE...")
# if len(condition_list)==0 or None:
#     print("\nTHE FILES ARE NOT ENCRYPTED....")


