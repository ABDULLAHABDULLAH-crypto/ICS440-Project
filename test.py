import secrets
import time
from AES_version import AESVersion
from custom_AES import CustomAES


def generate_random_bytes(num_bytes: int) -> bytes:
    return secrets.token_bytes(num_bytes)


plaintext = generate_random_bytes(16 * 10)

# Define keys for each AES version
key_128 = generate_random_bytes(16)
key_192 = generate_random_bytes(24)
key_256 = generate_random_bytes(32)
key_320 = generate_random_bytes(40)
key_384 = generate_random_bytes(48)
key_512 = generate_random_bytes(64)

# Initialize AES objects for each version
aes_versions = {
    AESVersion.AES_128: (CustomAES(AESVersion.AES_128), key_128),
    AESVersion.AES_192: (CustomAES(AESVersion.AES_192), key_192),
    AESVersion.AES_256: (CustomAES(AESVersion.AES_256), key_256),
    AESVersion.AES_320: (CustomAES(AESVersion.AES_320), key_320),
    AESVersion.AES_384: (CustomAES(AESVersion.AES_384), key_384),
    AESVersion.AES_512: (CustomAES(AESVersion.AES_512), key_512),
}

# Dictionary to store execution times
execution_times = {}

# Measure execution time for each AES version
for version, (aes, key) in aes_versions.items():
    start_time = time.time()
    encrypted = aes.encrypt(plaintext, key)
    end_time = time.time()
    execution_times[version] = end_time - start_time
    print(f"{version.name} encrypted text: {encrypted}")

# Compare and print execution times
for version, exec_time in execution_times.items():
    print(f"Execution time for {version.name}: {exec_time:.9f} seconds")

# Determine the fastest AES version
fastest_version = min(execution_times, key=execution_times.get)
print(
    f"The fastest AES version is {fastest_version.name}"
    f" with an execution time of {execution_times[fastest_version]:.6f} seconds.")
