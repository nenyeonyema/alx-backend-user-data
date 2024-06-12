import base64

# Sample string
sample_string = "Hello, World!"

# Convert the string to bytes
sample_bytes = sample_string.encode('utf-8')
print(sample_bytes)

# Encode the bytes using Base64
base64_bytes = base64.b64encode(sample_bytes)
print(base64_bytes)

# Convert the Base64 bytes back to a string
base64_string = base64_bytes.decode('utf-8')

print(base64_string)  # Outputs: SGVsbG8sIFdvcmxkIQ==

