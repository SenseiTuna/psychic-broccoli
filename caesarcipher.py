alfabe = ['a', 'b', 'c','ç','d', 'e', 'f', 'g','ğ', 'h','ı','i', 'j', 'k', 'l', 'm', 'n', 'o','ö', 'p', 'q', 'r', 's','ş', 't', 'u', 'ü','v', 'w', 'x', 'y', 'z']
sifreDesifre = input("Şifrelemek için 'encode' deşifre etmek için 'decode' yazın:\n").lower()
mesaj = input("Mesajı (boşluksuz şekilde) giriniz :\n").lower()
kaydirmamiktari = int(input("Kaç harf kaydırmak istiyorsunuz? :\n"))

def encode(mesaj,kaydirmamiktari):
    sifrelimesaj=""
    for i in mesaj:
        if alfabe.index(i)+kaydirmamiktari>31:
            yeniharf=((alfabe.index(i)+kaydirmamiktari)%31)-1
            sifrelimesaj+=alfabe[yeniharf]
        else:
            yeniharf=alfabe.index(i)+kaydirmamiktari
            sifrelimesaj+=alfabe[yeniharf]
    print(f"Şifrelenmiş mesajınız: {sifrelimesaj}")
def decode(mesaj,kaydirmamiktari):
    sifrelimesaj=""
    for i in mesaj:
        if alfabe.index(i)-kaydirmamiktari<0:
            yeniharf=((alfabe.index(i)-kaydirmamiktari)%31)+1
            sifrelimesaj+=alfabe[yeniharf]
        else:
            yeniharf=alfabe.index(i)-kaydirmamiktari
            sifrelimesaj+=alfabe[yeniharf]
    print(f"Deşifre edilmiş mesajınız: {sifrelimesaj}")
if sifreDesifre=="encode":
    encode(mesaj,kaydirmamiktari)
elif sifreDesifre=="decode":
    decode(mesaj,kaydirmamiktari)
else:
    print("Yanlış bir şifreleme/deşifreleme seçeneği girdiniz!")