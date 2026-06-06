def main():
    # Redefining the xorban and enc lists from output.txt
    xorban = [1, 243, 128, 75, 251, 28, 249, 9, 231, 152, 154, 2, 237, 
              223, 175, 17, 5, 150, 118, 14, 173, 151, 242, 240, 176, 10, 209, 29, 236, 
              208, 222, 177, 183, 91, 162, 8, 12, 103, 221, 30, 119, 184]
    
    enc = [105, 151, 16, 163, 222, 136, 163, 145, 135, 13, 51, 169, 148, 
           6, 30, 199, 97, 249, 137, 22, 252, 105, 81, 107, 36, 229, 175, 164, 192, 
           79, 81, 6, 117, 179, 186, 198, 48, 24, 201, 170, 10, 178]

    # Deduce the key from xorban
    key = [xorban[0]]
    for i in range(1, len(xorban)):
        key.append(xorban[i] ^ xorban[i-1])

    # Decrypt enc using the deduced key to get the flag
    flag = ''.join(chr(enc[i] ^ key[i]) for i in range(len(enc)))

    print(flag)

if __name__ == "__main__":
    main()
