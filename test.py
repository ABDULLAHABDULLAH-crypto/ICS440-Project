import secrets
import time
from AES_version import AESVersion
from custom_AES import CustomAES


def generate_random_bytes(num_bytes: int) -> bytes:
    return secrets.token_bytes(num_bytes)

# Define a plaintext to use for encryption
plaintext = generate_random_bytes(16 * 100)

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

# Number of iterations for each encryption
num_iterations = 10

# Dictionary to store cumulative execution times
cumulative_execution_times = {version: 0 for version in aes_versions}

# Measure execution time for each AES version
for version, (aes, key) in aes_versions.items():
    for _ in range(num_iterations):
        start_time = time.time()
        encrypted = aes.encrypt(plaintext, key)
        end_time = time.time()
        cumulative_execution_times[version] += end_time - start_time

# Calculate and print average execution times
for version, total_time in cumulative_execution_times.items():
    average_time = total_time / num_iterations
    print(f"Average execution time for {version.name}: {average_time:.6f} seconds")

# Determine the fastest AES version on average
fastest_version = min(cumulative_execution_times, key=cumulative_execution_times.get)
average_fastest_time = cumulative_execution_times[fastest_version] / num_iterations
print(f"The fastest AES version on average is {fastest_version.name} with an execution time of {average_fastest_time:.6f} seconds.")
