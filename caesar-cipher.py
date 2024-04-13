# Greeting function
def greet():
    print("Welcome to the Caesar Cipher Encryption and Decryption Program")
    print("This program will encrypt and decrypt your message using Caesar Cipher")
    print("Let's get started")

# Caesar Cipher function
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o","p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def caesar():
    # User selects whether to encode or decode
    encode_or_decode = input("Would you like to encode or decode a message? (encode/decode): ")

    # User enters message to encode or decode
    message = input("Enter your message: ").lower()

    # User enters shift value
    shift = int(input("Enter the shift value: "))

    # Program encodes or decodes message
    def caesar_cipher(input_message, shift_amount, en_or_de_choice):
        result = ""
        if en_or_de_choice == "encode" or en_or_de_choice == "e":
            for i in range(len(input_message)):
                char = input_message[i]
                if char.isalpha():
                    result += alphabet[(alphabet.index(char) + shift_amount) % 26]
                else:
                    result += char
        elif en_or_de_choice == "decode" or en_or_de_choice == "d":
            for i in range(len(input_message)):
                char = input_message[i]
                if char.isalpha():
                    result += alphabet[(alphabet.index(char) - shift_amount) % 26]
                else:
                    result += char
        return result

    # Prints result
    print(caesar_cipher(message, shift, encode_or_decode))

    # Program asks user if they want to encode or decode another message
    another_message = input("Would you like to encode or decode another message? (yes/no): ")
    if another_message == "yes" or another_message == "y":
        caesar()

if __name__ == "__main__":
    greet()
    caesar()