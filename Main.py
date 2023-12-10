from Cryptodome.Random import get_random_bytes
from Cryptodome.Protocol.KDF import PBKDF2
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad,unpad
import os
import time 

# Original Rcon table for AES key expansion

##  generating a key 

key_128=b'mysecretpassword' # 128bit key 
key_192=b'mysecretpasswordisabdull' # 192bit key 
key_256=b'mysecretpasswordisabdullahalamou' # 256bit key 





print("\n\n\t\tAES-128 bit \n\n")
message=b"Abdullah Saleh Alamoudi"
cipher=AES.new(key_128,AES.MODE_CBC)
start_time=time.time()
ciphered_data =cipher.encrypt(pad(message,AES.block_size))
end_time=time.time()
print("\n\n The time for AES-128 :",end_time-start_time)




# print("\n\n\t\tAES-192 bit \n\n")
# message=b"Abdullah Saleh Alamoudi"
# cipher=AES.new(key_192,AES.MODE_CBC)
# start_time=time.time()
# ciphered_data =cipher.encrypt(pad(message,AES.block_size))
# end_time=time.time()
# print("\n\nThe time for AES-192 :",end_time-start_time)




# print("\n\n\t\tAES-256 bit \n\n")
# message=b"Abdullah Saleh Alamoudi"
# cipher=AES.new(key_256,AES.MODE_CBC)
# start_time=time.time()
# ciphered_data =cipher.encrypt(pad(message,AES.block_size))
# end_time=time.time()
# print("\n\n The time for AES-256 :",end_time-start_time)