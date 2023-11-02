while True: 
    try :
        year = int(input("masukan tahun antara 1900 - 2020 "))
        if 1900 <= year <= 2020:
            break 
        else:
            print("tahun harus di antara  1900 - 2020 silahkan coba lagi.")
    except ValueError:
        print("input yang ada masukan bukan angka. silahkan coba lagi")

def kabisat(year): 
    if (year % 4 == 0):
        return True
    else:
        return False
    
if kabisat(year):
    print(f'{year} merupakan tahun kabisat .')
else:
    print(f"{year} bukan merupakan tahun kabisat.")
