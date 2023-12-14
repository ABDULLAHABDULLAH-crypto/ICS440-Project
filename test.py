import time
from Cryptodome.Cipher import AES
import custom_AES, AES_128, AES_320, AES_384, AES_512

def measure_execution_time(function, *args, **kwargs):
    start_time = time.time()
    function(*args, **kwargs)
    end_time = time.time()
    return end_time - start_time

plaintext = b"\x00\x04\x12\x14\x12\x04\x12\x00\x0C\x00\x13\x11\x08\x23\x19\x19"
key_128 = b"\x24\x75\xA2\xB3\x34\x75\x56\x88\x31\xE2\x12\x00\x13\xAA\x54\x87"
key_320 = b"\x24\x75\xA2\xB3\x34\x75\x56\x88\x31\xE2\x12\x00\x13\xAA\x54\x87\x13\xAA\x54\x87\x24\x75\xA2\xB3\x34\x75\x56\x88\x31\xE2\x12\x00\x13\xAA\x54\x87\x13\xAA\x54\x87"
key_384 = b"\x24\x75\xA2\xB3\x34\x75\x56\x88\x31\xE2\x12\x00\x13\xAA\x54\x87\x13\xAA\x54\x87\x24\x75\xA2\xB3\x34\x75\x56\x88\x31\xE2\x12\x00\x13\xAA\x54\x87\x13\xAA\x54\x87\x13\xAA\x54\x87\x13\xAA\x54\x87"
key_512 = b"\x24\x75\xA2\xB3\x34\x75\x56\x88\x31\xE2\x12\x00\x13\xAA\x54\x87\x24\x75\xA2\xB3\x34\x75\x56\x88\x31\xE2\x12\x00\x13\xAA\x54\x87\x24\x75\xA2\xB3\x34\x75\x56\x88\x31\xE2\x12\x00\x13\xAA\x54\x87\x24\x75\xA2\xB3\x34\x75\x56\x88\x31\xE2\x12\x00\x13\xAA\x54\x87"

time_128_standard = measure_execution_time(AES.new(key_128, AES.MODE_ECB).encrypt, plaintext)
time_128_custom = measure_execution_time(AES_base.encrypt, plaintext, key_128, AES_128.Nk, AES_128.Nr, AES_128.Rcon)
time_320 = measure_execution_time(AES_base.encrypt, plaintext, key_320, AES_320.Nk, AES_320.Nr, AES_320.Rcon)
time_384 = measure_execution_time(AES_base.encrypt, plaintext, key_384, AES_384.Nk, AES_384.Nr, AES_384.Rcon)
time_512 = measure_execution_time(AES_base.encrypt, plaintext, key_512, AES_512.Nk, AES_512.Nr, AES_512.Rcon)

print(f"Standard AES-128 Execution Time: {time_128_standard} seconds")
print(f"Custom AES-128 Execution Time: {time_128_custom} seconds")
print(f"AES-320 Execution Time: {time_320} seconds")
print(f"AES-384 Execution Time: {time_384} seconds")
print(f"AES-512 Execution Time: {time_512} seconds")
