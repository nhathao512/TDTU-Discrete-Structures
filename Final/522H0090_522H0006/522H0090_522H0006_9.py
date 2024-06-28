import rsa # import library

# Generation public key and private key
(public_key, private_key) = rsa.newkeys(2048)

#print public key
print("public key: {}\n".format(public_key))
print("private key: {}\n".format(private_key))

# plain text
message = "Hello, I'm doing my final report for the discrete structures course"

#encrypt
encrypted_message = rsa.encrypt(message.encode(), public_key)

print("encrypt text: {}\n".format(encrypted_message))

#decrypt
decrypted_message = rsa.decrypt(encrypted_message, private_key).decode()

# print decrypted message
print("decrypt message: {}\n".format(decrypted_message))

# message authentication
print('plain text = decrypt text: {}'.format(message == decrypted_message))


