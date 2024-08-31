def endian_representations(word):
    # Convert the string to its byte representation
    bytes_representation = word.encode('ascii')
    
    # Little-endian and big-endian representations are the same for individual bytes
    little_endian = bytes_representation
    big_endian = bytes_representation[::-1]  # Reverse for demonstration, but it's the same in this case
    
    return little_endian, big_endian

# Example usage
word = "ohllh"
little_endian, big_endian = endian_representations(word)
print(f"Little-endian representation: {little_endian}")
print(f"Big-endian representation: {big_endian}")

