from cryptography.fernet import Fernet

''' 

* step 1: get key to unlock files
* step 2: get the encrypted text in file
* step 3: use key to decrypt text in file
* step 4: save the decrypted text in file

'''

import os
files = os.listdir()
enc_files = []

with open("enc_key",'rb') as key_file:
    key = key_file.read()
    #print(f"key: {key}")


for file in files:
    if file not in ["env","enc_key","encrypt.py","scripts","__pycache__","decrypt.py","images","app.py","bye.py"]:
        f = Fernet(key)
        with open(file,"r") as myfile:
            encrypted_txt = bytes(myfile.read(),"utf-8")
            #print(f"{file} text: {encrypted_txt}")
            myfile.close()

        with open(file,"wb") as myfile:
            #print("\n\n\n")
            decrypted_txt = f.decrypt(encrypted_txt)
            #print("\n\n\n",decrypted_txt)
            myfile.write(decrypted_txt)
    








        
