def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts the given text using the Caesar Cipher algorithm.
    
    Args:
        text (str): The input text to be encrypted or decrypted.
        shift (int): The shift value (positive for encryption, negative for decryption).
        mode (str): 'encrypt' or 'decrypt'.
    
    Returns:
        str: The resulting encrypted or decrypted text.
    """
    result = ""
    for char in text:
        if char.isalpha():
            # Determine whether to shift forward or backward based on the mode
            if mode == 'encrypt':
                shifted_char = chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))
            elif mode == 'decrypt':
                shifted_char = chr((ord(char.lower()) - ord('a') - shift) % 26 + ord('a'))
            else:
                raise ValueError("Invalid mode. Use 'encrypt' or 'decrypt'.")
            
            # Preserve the original case (uppercase or lowercase)
            if char.isupper():
                result += shifted_char.upper()
            else:
                result += shifted_char
        else:
            # Non-alphabetic characters remain unchanged
            result += char
    
    return result

# Example usage
if __name__ == "__main__":
    user_text = input("Enter the text to encrypt or decrypt: ")
    user_shift = int(input("Enter the shift value (positive for encryption, negative for decryption): "))
    user_mode = input("Enter 'encrypt' or 'decrypt': ").lower()
    
    encrypted_or_decrypted_text = caesar_cipher(user_text, user_shift, user_mode)
    print(f"Result: {encrypted_or_decrypted_text}")
