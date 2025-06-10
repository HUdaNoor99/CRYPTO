```
# For comments on this function look at "Crypto Warmup 2" challenge
def decryptor(key, ciphertext):
    plaintext = ""
    for c in ciphertext:
        newChar = ord(c) - key
        if newChar < ord("a"):
            newChar = newChar + 26
        plaintext += chr(newChar)
    return plaintext

ciphertext = "payzgmuujurjigkygxiovnkxlcgihubb"
# For each valid key value
for i in range(1, 26):
    plaintext = decryptor(i, ciphertext)
    print("key is:", i, "text is:", plaintext)
```


Kita perlu mendekripsinya, dan yang kita tahu enkripsinya adalah sandi Caesar .
Jadi setelah mencarinya di Google, saya menemukan bahwa ROT13 yang kita bahas sebelumnya
adalah kasus sandi Caesar yang bersifat pribadi ketika kuncinya adalah 13.

Dalam sandi Caesar, kuncinya bisa antara 0 hingga 25 dan untuk setiap huruf kita mengganti setiap huruf dengan huruf ke-kunci setelahnya.
Dalam representasi yang lebih formal, enkripsinya adalah:
Enkripsi

x - huruf yang ingin kita enkripsi
n - kunci
En(x) - ciphertext untuk n dan x

Dan dekripsi hanyalah kebalikan dari operasi ini: Jadi saya menulis skrip python untuk mencoba setiap nilai kunci yang valid untuk ciphertext yang kami dapatkan:
Dekripsi
