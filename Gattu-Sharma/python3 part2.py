import hashlib

hashed_passwords = [
    "440846ee38fc4b638e05331a614d56eeea95ad6750c6dd9e533131a1fae29b5a",
    "d2483234ba02088409625485f0a24b7bb7f6c7faf06a28835684fe7794776899",
    "eb3c33f8ff30e5e1557518c5df2a890a7d863648b7917fdd534e7ba943970ad1",
    "090e8f83289d3d06f8c6f8e83a9e615c48b44ee3c044300a4784961da604c974",
    "db082a03f68fea13ca83cf7d768c7ef0384e4e609ac87eea409e8913a9c18909",
    "795a9cee92bc0c1f2d776b71eccc261909ff797a061992ad22ce3b4df7593a81",
    "4c852c8fddb0e9ba98e5535a6c16d8377b0d517da7c54b0746dae56003ff5447",
    "b8544d504cdcb4b5f7eb7dcd01f7c31966964f6ff71de02722633c09598cedad",
    "6059f0f10a15b67fe9f6937d491d1a67ee537f392072d91cdde20baf14b9edd5",
    "886ba69537dc098cc4c6982f83c0bbf51054678026e77849461f20f41d973764",
    "a06585033789f6e3fc2bfc0f1b67b004df1b3173dc4fea63544922a1fdc4b925",
    "d88b46d2b9d495b86a474d01adc91c95783b7b2338678d51297eb41278058717",
    "10be1826d8fa5a577057fd4245660911273856c68b0df1247c0f567cd7f166f0",
    "45187995629ba7a0f3e19b2a41ff4d6011e84189fc9c049627a71b31994de004",
    "f6a9e91781d38b95a8f41c9fe58372dcb67fb5ecc81fbe3c90b248665166407a",
    "eb905d194268640143c3dc72e9ef67a298f7ec3fa9b44a6e0ef8d5b774839ee5",
    "7b44baee52f32db3cb9a51447e49f42da23bd03b8d47a2c8eb4ced61069c5aa7",
    "634b71ed4f9491c875447e35bd18bc76ba6140e9554242544cd456f2603e531e",
    "a505518584af8e4b73e5265bdc66000b6001575ab01108a386cb2fc84fb8051a",
    "c0794663fe32ef7e2c1e1adaeb902f43bb94705f706b8fd0197c307f3d87e5bc",
    "663b7aa9bba51240ca78c483162f49af05ba8a7d278ef21ceb0c2b277c9e161a",
    "58e164f7656fc5edb91267c7234825ed83ec85de182860ecc62cdb140944f970",
    "c94a38bf2c04ef8e07c0837b2a317fd784aa4b450b2f25270655df9dbc1560a4",
    "e5b9543e83f21d021d4e04520b662873faa28075941f532a6253566ea325c0ff",
    "9277c3a036551a9408d3218cf390896e353f3bd0b0a9c89c7d8d9cb7e8c2fc8b",
    "523c135b2b6347e070483def95b51c05170d4839d9c875becd2b51ff2e011cd5",
    "46d5fbcc1225a265dac665258ac89c649bc95fce4d14f94e20d767012ae08708",
    "43e944eaf9a1816812eb8a8de5ae73362f7733b5bbeb1b8e330efe9b8131ee32",
    "4f3fdc8f6d0f6180b996f1d767b1cf938c81851264f42ecfb1320ccce7deb149",
    "35171772433cc9ca4e88a72daab436ae71ec21ba4b9030fdc379bcf4b4dfe586"

]

def read_words_from_file(file_path):
    with open(file_path, 'r') as file:
        words = [line.strip() for line in file]
    return words

# Define the file paths for the dictionary and password lists
dictionary_file_path = 'dictionary.txt'
password_file_path = 'password.txt'

# Read words from both files and combine them into potential_passwords
dictionary_words = read_words_from_file(dictionary_file_path)
password_words = read_words_from_file(password_file_path)
potential_passwords = dictionary_words + password_words

import hashlib

def hash_sequence(potential_password, password_hashes):
    hash_functions = [hashlib.md5, hashlib.sha384, hashlib.sha1, hashlib.sha224, hashlib.sha512, hashlib.sha256]

    for prefix in [''] + list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
        hashed_password = prefix + potential_password

        # Apply the entire sequence of hash functions
        for hash_func in hash_functions:
            hashed_password = hash_func(hashed_password.encode()).hexdigest()

        # Compare the final hashed password with the target hashes
        if hashed_password in password_hashes:
            return hashed_password

    return None
results = []
for potential_password in potential_passwords:
    
    # Check if the password generates a matching hash
    result = hash_sequence(potential_password, hashed_passwords)
    
    results.append(result)

for result in results:
    print(result)