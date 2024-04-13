# Greeting function
def greet():
    print("Welcome to the Caesar Cipher Encryption and Decryption Program")
    print("This program will encrypt and decrypt your message using Caesar Cipher")
    print("Let's get started")

def caesar():
    # User selects whether to encode or decode
    encode_or_decode = input("Would you like to encode or decode a message? (encode/decode): ")

    # User enters message to encode or decode
    message = input("Enter your message: ").lower()

    # User enters shift value
    shift = int(input("Enter the shift value: "))

    # Program encodes or decodes message
    def caesar_cipher(message, shift, encode_or_decode):
        result = ""
        if encode_or_decode == "encode" or encode_or_decode == "e":
            for i in range(len(message)):
                char = message[i]
                if char.isalpha():
                    result += chr((ord(char) + shift - 97) % 26 + 97)
                else:
                    result += char
        elif encode_or_decode == "decode" or encode_or_decode == "d":
            for i in range(len(message)):
                char = message[i]
                if char.isalpha():
                    result += chr((ord(char) - shift - 97) % 26 + 97)
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