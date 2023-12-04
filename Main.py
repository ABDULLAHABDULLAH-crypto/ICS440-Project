
from Cryptodome.Random import get_random_bytes
from Cryptodome.Protocol.KDF import PBKDF2
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad,unpad

##  generating a key 
# simple_key=get_random_bytes(32);
# print(simple_key)
salt=b'\x80(%C\xb8%\xda\xa2zj\x1a\x9b\xa2\xb1\xdaN\xf1\xe0Z\x93\xd23\xeb!\xd3\x9b\x9e\xa7\xd9]$v'
password="mypassword"
## the below code will generate encryption key 
key=PBKDF2(password,salt,dkLen=32)


message=b"Abdullah Saleh Alamoudi"
cipher=AES.new(key,AES.MODE_CBC)
ciphered_data =cipher.encrypt(pad(message,AES.block_size))


## the code below will save the encryption text as bytes into a file 
# with open('encrypted.bin','wb') as f:
#     f.write(cipher.iv)
#     f.write(ciphered_data)

## the code below will decrypt the file ,and print the message
# with open('encrypted.bin','rb') as f:
#     iv=f.read(16)
#     decrypt_data=f.read()

# cipher=AES.new(key,AES.MODE_CBC,iv=iv)
# print(unpad(cipher.decrypt(decrypt_data),AES.block_size))
