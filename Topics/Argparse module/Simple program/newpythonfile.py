def decode_Caesar_cipher(s, n):
    alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n) % len(alpha)]
    print('Decoded text: "' + text + '"')


filename = r"C:\Users\gkouvas\OneDrive - Fondation Campus Biotech Geneva\Desktop\hyperskill-dataset-40231214.txt"
opened_file = open(filename)
encoded_text = opened_file.read()  # read the file into a string
for n in range(0, 100):
    decode_Caesar_cipher(encoded_text, n)
opened_file.close()  # always close the files you've opened
