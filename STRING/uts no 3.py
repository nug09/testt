def is_palindrome(sentence):
    sentence = sentence.replace(' ', '').lower()

    if sentence == sentence[::-1]:
        return True
    else:
        return False
kalimat = input('masukkan kalimat: ')

if is_palindrome(kalimat):
    print('iinin adalah kalimat palindrom.')
else:
    print('ini bukan kalimat palindrom.')