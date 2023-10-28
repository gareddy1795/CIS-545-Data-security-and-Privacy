PART 1

The script uses a simple XOR cipher with a candidate key to decrypt the ciphertext.
It iterates through all possible keys (0 to 255) to find the correct one that results in a readable ASCII text.
The provided ciphertext should be base64-encoded.

PART 2 

Download an English dictionary file named dictionary.txt.
Download a list of common passwords named common_passwords.txt.
Provide Hashed Passwords:

Modify the password_hashe list in the script to include the target hash values you want to recover.
Run the Script:

Execute the script using Python: python password_recovery.py.

The script uses a combination of hashing algorithms (MD5, SHA-384, SHA-1, SHA-224, SHA-512, SHA-256) and prefixes to generate candidate passwords.
It then hashes these candidates and compares them to the provided hash values.
If a match is found, it reports the original password.