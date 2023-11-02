def anagrams(kata1,kata2):
    kata1 = kata1.replace(" " , " ").lower()
    kata2 = kata2.replace(" " , " ").lower()

    sort_kata1 = sorted(kata1)
    sort_kata2 = sorted(kata2)
    
    return sort_kata1 == sort_kata2

kata1 = input("masukan kata pertama: ")
kata2 = input("masukan kata kedua: ")

if anagrams(kata1,kata2):
    print(f"{kata1} dan {kata2} adalah anagram.")
else:
    print(f"{kata1} dan {kata2} bukan anagram.")



