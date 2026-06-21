"""
Caesar Cipher Implementation
A Python script to encrypt and decrypt text using the classic Caesar Cipher algorithm.
Supports both lowercase and uppercase character transformations while preserving spacing.
"""

def caesar(text: str, shift: int, encrypt: bool = True) -> str:
    """
    Core function to handle both encryption and decryption using a Caesar Cipher.

    Parameters:
    text (str): The input text to be processed.
    shift (int): The number of positions to shift the alphabet (must be between 1 and 25).
    encrypt (bool): True to encrypt the text, False to decrypt it. Default is True.

    Returns:
    str: The resulting encrypted or decrypted text.
    """
    # Validate that the shift value is an integer
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    # Validate that the shift value falls within the valid alphabet range
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # If decrypting, reverse the direction of the alphabet shift
    if not encrypt:
        shift = -shift
    
    # Create the shifted version of the alphabet
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    
    # Create a translation table that maps both lowercase and uppercase letters
    translation_table = str.maketrans(
        alphabet + alphabet.upper(), 
        shifted_alphabet + shifted_alphabet.upper()
    )
    
    # Translate the input text using the mapping table
    processed_text = text.translate(translation_table)
    return processed_text


def encrypt(text: str, shift: int) -> str:
    """Helper function to encrypt text using the Caesar Cipher."""
    return caesar(text, shift, encrypt=True)
    
    
def decrypt(text: str, shift: int) -> str:
    """Helper function to decrypt text using the Caesar Cipher."""
    return caesar(text, shift, encrypt=False)


# Demonstration block (Runs only when executing this file directly)
if __name__ == "__main__":
    original_text = 'freeCodeCamp'
    shift_value = 3
    
    print("--- Caesar Cipher Demo ---")
    print(f"Original Text:  {original_text}")
    
    # Encrypt
    encrypted_text = encrypt(original_text, shift_value)
    print(f"Encrypted Text: {encrypted_text}")
    
    # Decrypt
    decrypted_text = decrypt(encrypted_text, shift_value)
    print(f"Decrypted Text: {decrypted_text}")
