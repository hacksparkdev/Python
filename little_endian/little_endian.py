def string_to_little_endian(s):
# Convert the string to its byte respresentation
    bytes_representation = s.encode('ascii')

    # display the bytes in little-endian format
    return bytes_representation

# Usage
string = 'bfyei'

little_endian_bytes = string_to_little_endian(string)
print(little_endian_bytes)


