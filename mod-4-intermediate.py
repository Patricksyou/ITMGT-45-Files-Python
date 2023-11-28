'''Module 3: Individual Programming Assignment 1

Thinking Like a Programmer

This assignment covers your intermediate proficiency with Python.
'''

def shift_letter(letter, shift):
    '''Shift Letter. 
    4 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    letter_uppercase = letter.upper()
    shifting_number = shift % 26
    ordinance_of_letter = ord(letter_uppercase)

    if ordinance_of_letter ==  32:
        return(" ")
    
    elif(ordinance_of_letter + shifting_number > 90):
        ordinance_of_letter = ordinance_of_letter + shifting_number - 26
        return chr(ordinance_of_letter)
    
    elif(ordinance_of_letter + shifting_number < 91):
        ordinance_of_letter = ordinance_of_letter + shifting_number
        return chr(ordinance_of_letter)

def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    6 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    message_to_translate = message
    x = ""

    for i in message_to_translate:
        x = x + shift_letter(i, shift)
        
    return x

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    4 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    letter = letter.upper()
    letter_shift = letter.upper()
    letter = ord(letter) - 65
    letter_shift = ord(letter_shift) - 65
    translated_letter = letter + letter_shift
        
    if translated_letter >= 26:
        translated_letter = translated_letter - 26
        return chr(translated_letter + 65)

    elif letter == 32:
         return(" ")

    else:
        translated_letter = translated_letter
        return chr(translated_letter + 65)
    
    
def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    6 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    length_of_key = len(key)
    shiftedmessage = ""
    message = message.upper()
    key = key.upper()
    
    for i in range(len(message)):
        if message[i] == " ": 
            shiftedmessage += " "
            
        else:
            shiftedmessage = shiftedmessage + chr( ((ord(message[i]) + ord(key[i % length_of_key])) % 26) + 65 )
            
    return shiftedmessage