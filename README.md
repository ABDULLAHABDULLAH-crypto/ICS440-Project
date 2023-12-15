
## Customized AES Encryption Project

### Introduction
This project consists of Python scripts that implement and test various versions of the Advanced Encryption Standard (AES) algorithm. It is designed to demonstrate custom AES encryption and decryption processes with different key sizes.

### Requirements
- Python 3.x
- Numpy (for `custom_AES.py`)

### File Descriptions
1. **AES_version.py**
   - Enumerates different versions of the AES algorithm.
   - Defines key length (`Nk`), number of rounds (`Nr`), and round constants (`Rcon`) for each version.

2. **custom_AES.py**
   - Implements the AES encryption and decryption processes.
   - Utilizes the `AESVersion` enumeration from `AES_version.py`.
   - Includes key expansion and all steps of the AES algorithm.
   - Depends on Numpy for certain operations.

3. **test.py**
   - A test script for the AES functionality.
   - Generates random bytes for plaintext and keys.
   - Tests encryption and decryption with different key sizes.
   - Demonstrates the usage of functions/classes from `custom_AES.py`.

### Usage
1. Ensure Python 3.x and Numpy are installed.
2. Run `test.py` to see the encryption and decryption in action with different AES versions and key sizes.
3. To use custom AES in other projects, import the necessary functions/classes from `custom_AES.py`.

### Additional Notes
- This implementation is for educational purposes and may not be suitable for production environments.
- Ensure understanding of the AES algorithm and its parameters before modification.
