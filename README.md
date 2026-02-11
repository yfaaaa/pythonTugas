/Analisis1 = OUTPUT: Traceback (most recent call last): File "c:\OOP Python\game_rpg.py", line 12, in hero1 = Hero("Layla", 500) TypeError: Hero.init() missing 1 required positional argument: 'attack_power'

ini muncul karena di dalam objek hero cuma ada 2 nilai. Di dalam init butuh 3 nilai dan init kurang 1 argumen posisi yang diperlukan: 'attack_power' dan kalau kita tambahkan 1 nilai dia tidak akan error

/Analisis2 = Parameter lawan harus berupa objek utuh karena objek tersebut memiliki atribut dan method, Jika hanya berupa string nama, maka program tidak dapat mengakses atau mengubah keadaan lawan.

/Analisis3 = Traceback (most recent call last): File "c:\OOP Python\game_rpg.py", line 48, in eudora.info() ~~~~~^^ File "c:\OOP Python\game_rpg.py", line 8, in info print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}") ^^^^^^^^^ AttributeError: 'Mage' object has no attribute 'name' error ini muncul karena tidak memiliki atribut name, padahal method info mencoba mengakses self.name. Karena pada class Mage atribut name tidak dideklarasikan dengan benar. Meskipun saat membuat objek kita mengirim nama Eudora, nilai tersebut tidak otomatis menjadi atribut.

/Analisis4 = 1. percobaan hacking: aman tidak ada indikasi error 2. Uji Validasi: File "c:\OOP Python\game_rpg.py", line 14 nilai_baru < 0: ^ SyntaxError: invalid syntax karena setter berfungsi sebagai pengontrol perubahan nilai atribut.

/Analisis5 = 1. Melanggar Kontrak: karena class hero belum lengkap sehingga python melarang membuat objek. Program akan mengalami error saat dijalankan 2. Mencetak Cetakan: kerangka dasar bagi class turunan

/Analisis6 = 1. Uji Skalabilitas : karena class Healer memiliki method serang dengan nama yang sama seperti yang dimiliki oleh class Hero dan class turunan lainnya. 2. Konsistensi penamaan : --- PERANG DIMULAI --- Traceback (most recent call last): File "c:\OOP Python\game_rpg.py", line 72, in penyerang.serang(target) ~~~~~^^^^^^^^ File "c:\OOP Python\game_rpg.py", line 42, in serang print(f"{self.nama} (Mage) menembakkan Fireball! \U0001f525") ~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "C:\Users\LOQ 10\AppData\Local\Programs\Python\Python313\Lib\encodings\cp1252.py", line 19, in encode return codecs.charmap_encode(input,self.errors,encoding_table)[0] ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ UnicodeEncodeError: 'charmap' codec can't encode character '\U0001f525' in position 36: character maps to ini terjadi karena method tembak_panah tidak dideklarasikan olleh class
