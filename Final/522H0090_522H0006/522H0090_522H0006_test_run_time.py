import rsa
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import time
import matplotlib.pyplot as plt

# Function to encrypt data using RSA
def rsa_encrypt(data, rsa_public_key):
    max_length = rsa_public_key.n.bit_length() // 8 - 11
    if len(data) > max_length:
        raise OverflowError(f"{len(data)} bytes needed for message, but there is only space for {max_length}")
    return rsa.encrypt(data, rsa_public_key)

# Function to decrypt data using RSA
def rsa_decrypt(encrypted_data, rsa_private_key):
    return rsa.decrypt(encrypted_data, rsa_private_key)

# Function to encrypt data using AES and RSA
def hybrid_encrypt(data, rsa_public_key):
    aes_key = get_random_bytes(32)  # AES 256-bit key
    cipher_aes = AES.new(aes_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)
    encrypted_aes_key = rsa.encrypt(aes_key, rsa_public_key)
    return {
        'ciphertext': base64.b64encode(ciphertext).decode('utf-8'),
        'tag': base64.b64encode(tag).decode('utf-8'),
        'nonce': base64.b64encode(cipher_aes.nonce).decode('utf-8'),
        'encrypted_aes_key': base64.b64encode(encrypted_aes_key).decode('utf-8')
    }

# Function to decrypt data using AES and RSA
def hybrid_decrypt(enc_data, rsa_private_key):
    encrypted_aes_key = base64.b64decode(enc_data['encrypted_aes_key'])
    aes_key = rsa.decrypt(encrypted_aes_key, rsa_private_key)
    nonce = base64.b64decode(enc_data['nonce'])
    ciphertext = base64.b64decode(enc_data['ciphertext'])
    tag = base64.b64decode(enc_data['tag'])
    cipher_aes = AES.new(aes_key, AES.MODE_EAX, nonce=nonce)
    data = cipher_aes.decrypt_and_verify(ciphertext, tag)
    return data

# Function to measure time for RSA and Hybrid encryption/decryption
def measure_time(key_size, iterations=100):
    print(f"Testing with key size: {key_size} bits")
    (public_key, private_key) = rsa.newkeys(key_size)
    message = "Hello, I'm doing my final report for the discrete structures course" * 10  # Larger message
    message_bytes = message.encode()

    rsa_total_time = 0
    hybrid_total_time = 0

    for _ in range(iterations):
        start_time = time.time()
        # Encrypt each part of the message that is within the size limit
        encrypted_message_rsa = []
        max_length = key_size // 8 - 11
        for i in range(0, len(message_bytes), max_length):
            encrypted_message_rsa.append(rsa_encrypt(message_bytes[i:i + max_length], public_key))
        decrypted_message_rsa = b''.join(rsa_decrypt(part, private_key) for part in encrypted_message_rsa).decode()
        rsa_total_time += time.time() - start_time

        start_time = time.time()
        encrypted_data_hybrid = hybrid_encrypt(message_bytes, public_key)
        decrypted_message_hybrid = hybrid_decrypt(encrypted_data_hybrid, private_key).decode()
        hybrid_total_time += time.time() - start_time

        assert message == decrypted_message_rsa
        assert message == decrypted_message_hybrid

    rsa_total_time /= iterations
    hybrid_total_time /= iterations

    return rsa_total_time, hybrid_total_time

# Test with different key sizes
key_sizes = [2048, 3072, 4096]
results = []

for key_size in key_sizes:
    result = measure_time(key_size)
    results.append((key_size, *result))

# Print results
print("Key Size | RSA Total Time (s) | Hybrid Total Time (s)")
for key_size, rsa_total, hybrid_total in results:
    print(f"{key_size:8} | {rsa_total:17.6f} | {hybrid_total:18.6f}")

# Plot results
rsa_times = [result[1] for result in results]
hybrid_times = [result[2] for result in results]

plt.figure(figsize=(10, 6))
plt.plot(key_sizes, rsa_times, label='RSA', marker='o')
plt.plot(key_sizes, hybrid_times, label='Hybrid (AES + RSA)', marker='o')
plt.xlabel('Key Size (bits)')
plt.ylabel('Total Time (seconds)')
plt.title('Runtime Comparison of RSA and Hybrid (AES + RSA)')
plt.legend()
plt.grid(True)
plt.savefig('runtime_comparison.png')
plt.show()
