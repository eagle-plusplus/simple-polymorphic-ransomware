from cryptography.fernet import Fernet

# Define a function to encrypt the code payload
def encrypt_payload(payload):
    # Generate a unique encryption key
    key = Fernet.generate_key()
    cipher = Fernet(key)
    encrypted_payload = cipher.encrypt(payload)
    return key, encrypted_payload

# Encrypt a file
def encrypt_file(input_file_path, output_file_path):
    # Read the file as bytes
    with open(input_file_path, 'rb') as file:
        file_data = file.read()

    # Encrypt the file data
    key, encrypted_data = encrypt_payload(file_data)

    # Write the encrypted data to the output file
    with open(output_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    # Return the key (this key is essential to decrypt the file later)
    return key

# Example usage
input_file_path = 'payload.py'          # The path to the file you want to encrypt
output_file_path = 'payload.txt'  # The path where encrypted file will be saved

key = encrypt_file(input_file_path, output_file_path)
print("Encryption key:", key.decode())  # Print key; ensure you save this securely for decryption
