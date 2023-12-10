AES Encryption Implementations
This repository contains a series of Python scripts implementing the Advanced Encryption Standard (AES) encryption algorithm with various key lengths. The scripts cover standard AES key lengths (128 bits) as well as extended key lengths (320, 384, and 512 bits).

Files
AES_base.py: A base implementation of AES.
AES-128.py: Implementation of AES with a 128-bit key.
AES-320.py: Extended AES implementation with a 320-bit key.
AES-384.py: Extended AES implementation with a 384-bit key.
AES-512.py: Extended AES implementation with a 512-bit key.
Requirements
Python 3.x
Numpy library (for some scripts)
Usage
To run any of these scripts, ensure you have Python installed on your system. Some scripts require the Numpy library, which can be installed using pip:

bash
Copy code
pip install numpy
Run a script with:

bash
Copy code
python <script_name>.py
Replace <script_name> with the name of the script you want to run (e.g., AES-128).

Script Details
AES_base.py
This script provides a base AES implementation. It includes fundamental functions used across other AES scripts.

AES-128.py
Implements AES encryption with a standard 128-bit key. This script demonstrates the traditional AES encryption process.

AES-320.py
A custom implementation of AES with a 320-bit key. This non-standard extension includes modifications to the key expansion process and the number of encryption rounds.

AES-384.py
Similar to AES-320.py, but for a 384-bit key. The script includes adjustments to handle the larger key size and additional encryption rounds.

AES-512.py
An experimental implementation of AES with a 512-bit key. It features further adaptations to the AES algorithm to accommodate the extended key size.

Notes
The extended key implementations (320, 384, and 512 bits) are experimental and not part of the AES standard. They are provided for educational purposes and should not be used for security-critical applications.
Ensure you understand the basics of AES before experimenting with the extended key implementations.
License
Specify the license under which these scripts are released.

Contact
Provide your contact information or links to your social media/GitHub profile.
