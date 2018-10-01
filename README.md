# AES Encryption

# Group Members :
1. Aditya Prasad - AP45485
2. Calvin Liu - CL37896
3. Prajit Malhan - PSM744

# How to run:
run `python3 AES.py --keysize <128 or 256> --keyfile <key> --inputfile <input> -- outputfile <output> --mode <encrypt or decrypt>`

# Command line arguments:
1. `--keysize`: the keysize, either 128 or 256
2. `--keyfile`: they file containing the key, either 128 or 256 bits.
    To generate 16-byte key, run `head -c 16 < /dev/urandom > key`.
    To generate 32-byte key, run `head -c 32 < /dev/urandom > key`.
3. `--inputfile`: the file to be encrypted or decrypted.
4. `--outputfile`: the file where the encrypted/decrypted message will be saved.
5. `--mode`: "encrypt" or "decrypt"

# Notes:
1. Code formatted with autopep8 to meet python standards
    `autopep8 --in-line AES.py`
