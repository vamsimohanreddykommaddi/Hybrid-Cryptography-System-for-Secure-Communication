from tkinter import *
from tkinter import filedialog
from functools import partial
from new import hybrid_cipher
from new1 import hybrid_decipher

global filename
button_height = 2
button_width = 25

def browseFiles():
    browseFiles.filename = filedialog.askopenfilename(initialdir="/", title="Select a Text File")
    label_file_explorer.configure(text="File Opened: " + browseFiles.filename)

    pass_label.pack()
    temp_label.pack()
    button_save.pack()
    button_encrypt.pack()
    button_decrypt.pack()

def save():
    with open("keys.txt","w") as keys:
        keys.write('Vigenere Key: '+str(key_entry1.get())+'\n')
        keys.write('Polybius Key: '+str(key_entry2.get()))

def encrypt_file():
    vig_key=str(key_entry1.get())
    pol_key=str(key_entry2.get())
    with open('key1.txt','w') as key1:key1.write(vig_key)
    with open('key2.txt','w') as key2:key2.write(pol_key)
    
    with open(browseFiles.filename, 'r') as file:  original = file.read()
    encrypted = hybrid_cipher(original,vig_key,pol_key)

    with open(browseFiles.filename, 'w') as encrypted_file:    encrypted_file.write(encrypted)

    status_label.configure(text="Your file is Encrypted")
    status_label.pack()

def decrypt_file():
    vig_key = str(key_entry1.get())
    pol_key = str(key_entry2.get())
    with open('key1.txt','r') as key1:k1=key1.read()
    with open('key2.txt','r') as key2:k2=key2.read()

    if(vig_key==k1 and pol_key==k2):
        with open(browseFiles.filename, 'r') as enc_file:  encrypted = enc_file.read()
        decrypted = hybrid_decipher(encrypted,vig_key,pol_key)

        with open(browseFiles.filename, 'w') as dec_file:  dec_file.write(decrypted)

        status_label.configure(text="Your file is Decrypted")
        status_label.pack()
    else:
        status_label.configure(text="Invalid keys")
        status_label.pack()


window = Tk()

window.title('Hybrid Cryptography System Using Vigenere Cipher and Polybius Cipher')
window.geometry("940x740")
window.config(background="skyblue")

main_title = Label(window, text="HYBRID CRYPTOGRAPHY SYSTEM", width=100, height=2, fg="white", bg="skyblue",font =("",30))

key_entry1=StringVar()
key_entry2=StringVar()

submit_para_en = partial(encrypt_file)
submit_para_de = partial(decrypt_file)

credit = Label(window,text = "", bg="skyblue",height=2,  fg = "white", font =("",15))
label_file_explorer = Label(window, text="File Name : ", width=100, height=2, fg="white", bg="skyblue",font =("",20))
pass_label = Label(window, text="Keys for encryption/decryption : ", width=100, height=2, fg="black", bg="skyblue",font =("",20))
temp_label = Label(window, text="", height=3, bg="skyblue")

button_explore = Button(window, text="Browse File", command=browseFiles, width=button_width, height=button_height, font =("",15))

key_label1=Label(window,text="Vigenere Key : ",fg="black").place(x=200,y=350)
entry1 = Entry(window,textvariable=key_entry1,show="*").place(x=300,y=350)

key_label2=Label(window,text="Polybius Key : ",fg="black").place(x=500,y=350)
entry2=Entry(window,textvariable=key_entry2,show='*').place(x=600,y=350)



button_save = Button(window, text="Save Keys", command=save, width=button_width, height=button_height, font =("",15))
button_encrypt = Button(window, text="Encrypt", command=submit_para_en, width=button_width, height=button_height, font =("",15))
button_decrypt = Button(window, text="Decrypt", command=submit_para_de, width=button_width, height=button_height, font =("",15))

status_label = Label(window, text="", width=100, height=4, fg="black", bg="skyblue",font =("",17))

credit.pack()
main_title.pack()
label_file_explorer.pack()
button_explore.pack()
window.mainloop()
