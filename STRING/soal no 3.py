def hapus_spasi_lebih(string):
    kata =string.split()
    string_normal = ' '.join(kata)
    return string_normal

input_string= input("masukan kalimat:")
output_string= hapus_spasi_lebih(input_string)
print(output_string)
