import string

# clear the message of all spaces and newlines
def clear_message(message):
    """Clear the message of all spaces and newlines"""
    message = message.replace(' ', '')
    message = message.replace('\n', '')
    message = message.replace('\r', '')
    return message

# read message from txt
def read_txt(path):
    """Read a message from a text file"""
    with open(path, 'r') as f:
        message = ""
        for line in f:
            message += line.rstrip('\n')
        message= clear_message(message)
    return message

# caculate the index of coincidence of a message
def count_ic(message):
    """Count the Index of Coincidence (IC) for a given message"""
    message = message.lower().replace(" ", "")
    freqs = {char: message.count(char) for char in string.ascii_lowercase}
    n = len(message)
    ic = sum([freqs[char] * (freqs[char] - 1) for char in freqs]) / (n * (n - 1))
    return ic

# split message into n parts by character
def split_message(message, n):
    """Split a message into n parts by character"""
    parts = []
    for i in range(n):
        parts.append(message[i::n])
    return parts

def find_key_lenth(message):
    """Find the key length of a message"""
    ic_list = []
    for i in range(1, 10):
        sp_message = split_message(message, i)
        average_ic = 0
        for msg in sp_message:
            average_ic += count_ic(msg)
        ic_list.append(average_ic / i)
    """print the key length and the corresponding IC"""
    possible_key_length = []
    for i in range(len(ic_list)):
        if ic_list[i] >= ic_list[max(i - 1, 0)] and ic_list[i] >= ic_list[min(i + 1, len(ic_list) - 1)] and ic_list[i] > 0.06:
            possible_key_length.append(i + 1)
        print("Key length: %d, IC: %f" % (i + 1, ic_list[i]))
    return possible_key_length

def find_single_key(message):
    """Find the key of a message"""
    message = message.lower()
    true_freq = [0.08167, 0.01492, 0.02782, 0.04253, 0.012702, 0.02228, 0.02015, 0.06094, 0.06966,
            0.00153, 0.00772, 0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987,
            0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150, 0.01974, 0.00074]
    freqs = {char: message.count(char)/len(message) for char in string.ascii_lowercase}

    #print frequency of each letter
    # print(freqs)

    key = 0
    min_diff = float('inf')
    for i in range(26):
        diff = 0
        for j in range(26):
            diff += (freqs[chr((j + i) % 26 + ord('a'))] - true_freq[j])**2
        if diff < min_diff:
            min_diff = diff
            key = i
    return chr(key + ord('a'))

def find_key(message, key_lenth):
    """Find the key of a message"""
    sp_message = split_message(message, key_lenth)
    key = ""
    for msg in sp_message:

        key+= find_single_key(msg)
    return key

def decrypt(message, key):
    """Decrypt a message with a given key"""
    message = message.lower()
    key = key.lower()
    decrypted_message = ""
    for i in range(len(message)):
        decrypted_message += chr((ord(message[i]) - ord(key[i % len(key)])) % 26 + ord('a'))
    return decrypted_message

if __name__ == '__main__':
    # get message1 from txt
    print("Message 1:")
    message = read_txt('message1.txt')
    # get message from stdin
    # message = input("Enter a message: ")
    message = clear_message(message)
    # save clean message to txt
    with open('message1_clean.txt', 'w') as f:
        f.write(message)
    # print(message)
    # print(split_message(message, 2))
    # print(count_ic(message))
    print("Possible key lenth:",find_key_lenth(message))
    key_lenth = input("Enter the key length: ")
    key = find_key(message, int(key_lenth))
    print("Key: %s" % key)
    decrypt_message = decrypt(message, key)
    print("Decrypted message: %s" % decrypt_message)
    # save output to txt
    with open('109704011_msg1.txt', 'w') as f:
        f.write(decrypt_message)


    # get message2 from txt
    print("\nMessage 2:")
    message = read_txt('message2.txt')
    message = clear_message(message)
    print("Possible key lenth:", find_key_lenth(message))
    key_lenth = input("Enter the key length: ")
    key = find_key(message, int(key_lenth))
    print("Key: %s" % key)
    decrypt_message = decrypt(message, key)
    print("Decrypted message: %s" % decrypt_message)
    # save output to txt
    with open('109704011_msg2.txt', 'w') as f:
        f.write(decrypt_message)

    # get message from stdin
    message = input("\nEnter a message: ")
    message = clear_message(message)
    # save clean message to txt
    with open('message2_clean.txt', 'w') as f:
        f.write(message)
    print("Possible key lenth:", find_key_lenth(message))
    key_lenth = input("Enter the key length: ")
    key = find_key(message, int(key_lenth))
    print("Key: %s" % key)
    decrypt_message = decrypt(message, key)
    print("Decrypted message: %s" % decrypt_message)

