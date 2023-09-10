def caesar(text, shift, direction):
    new_text = ""
    for letter in text:
        if letter in alphabet:
            letter_position = alphabet.index(letter)
            new_letter = alphabet[letter_position]
            if direction == 'encode':
                for _ in range(0, shift):
                    letter_position += 1
                    if letter_position > len(alphabet) - 1:
                        letter_position = 0
                        new_letter = alphabet[letter_position]
                    new_letter = alphabet[letter_position]
                new_text += new_letter
            elif direction == 'decode':    
                for _ in range(0, shift):
                    letter_position -= 1
                    if letter_position < 0:
                        letter_position = len(alphabet) - 1
                        new_letter = alphabet[letter_position]
                    new_letter = alphabet[letter_position]
                new_text += new_letter
        else:
            new_text += letter
    print(f"The {direction}d text is '{new_text}'")

continue_running = True

while continue_running:
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number: "))
        
    caesar(text=text, shift=shift, direction=direction)
    choice = input("Do you want to continue? Yes or No: \n").lower()
    if choice == 'no':
        continue_running = False
        print("Goodbye.")