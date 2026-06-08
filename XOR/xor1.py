def repeatKey(ciphertext, key):
    repeats = len(ciphertext)//len(key)
    remainder = len(ciphertext) % len(key)
    repeatedKey = ""
    for x in range(repeats):
        repeatedKey += key
    repeatedKey += key[:remainder]
    return repeatedKey


def bruteforce_XOR(ciphertext, known_plaintext):
    b_ct = bytes.fromhex(ciphertext)
    key = "00"
    while 1==1:
        repeatedKey = repeatKey(ciphertext, key)
        b_rk = bytes.fromhex(repeatedKey)
        index = 0
        m = ""
        for byte in b_ct:
            m += chr(byte ^ b_rk[index])
            index += 1
        if m[:len(known_plaintext)] == known_plaintext:
            return m, key
        key = int(key, 16)+1
        key = hex(key)
        key = key[2:]
        if len(key) % 2 != 0:
            key = "0" + key
    return m, key


def main():
    ct = "754933765535356a4535755d397c692e61743361742072672072713664713661743361743c"
    known_pt = "forestyctf{"
    message, key = bruteforce_XOR(ct, known_pt)
    print(f'plaintext: {message} key: {key}')

main()
