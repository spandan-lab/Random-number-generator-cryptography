from Crypto.Cipher import AES
from Crypto import Random

messagetext = ("255044462d312e350a25d0d4c5d80a34").decode("hex")
iv = ("09080706050403020100A2B2C2D2E2F2").lower().decode("hex")
ciphertext = ("d06bf9d0dab8e8ef880660d2af65aa82")


with open('keys.txt') as f:
    keys = f.readlines()

for k in keys:
    k = k[:-1]
    key = k.decode("hex")
    cipher = AES.new(key,AES.MODE_CBC,iv)
    message = cipher.encrypt(messagetext)
    if message.encode("hex")[0:32] == ciphertext:
        print("The key is found: ", k)
        exit(0)

print("No key match found!")
