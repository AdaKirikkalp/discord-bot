import random

def sifre_uret():
    karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    sifre = ""
    for x in range(10):
        sifre += random.choice(karakterler)
    #şifreyi değer olarak kullanabilmek için return ile geri döndürelim
    return sifre
