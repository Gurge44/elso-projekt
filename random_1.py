import random
import string

alphabet = list(string.ascii_letters)  # Az angol abc betűi
stop = False

while True:  # Addig ismétlődik a bemenet kérése, amíg nem helyes
    try:
        choice = int(input("Generálási mód kiválasztása:\n  Írj be egy pozitív egész számot 1-4-ig\n    1: ki.txt generálása véletlen számokkal\n    2: ki.txt generálása véletlen karakterekkel\n    3: ki.txt formátumának ellenőrzése - véletlen számokkal\n    4: ki.txt formátumának ellenőrzése - véletlen karakterekkel\n"))
        if 1 <= choice <= 4:  # Ha érvényes a beírt szám, a program kilép a ciklusból és halad tovább
            break
        else:
            print("A szám legyen nagyobb, vagy egyenlő, mint 1, és kisebb, vagy egyenlő, mint 4")
    except ValueError:  # Ha a felhasználó nem számot írt be
        print("Egy egész számot írj be.")
    except KeyboardInterrupt:  # CTRL + C
        stop = True
        break
    except:  # Más hiba
        print("Hiba történt. Próbálkozz újra.")


if not stop:  # A program leáll, ha a felhasználó lenyomta a CTRL + C billentyűket
    match choice:  # A generálási mód kiválasztása
        case 1:
            while True:  # Addig ismétlődik a bemenet kérése, amíg nem helyes
                try:
                    amount = int(input("Hány darab szám legyen generálva? "))
                    limits = input("Alsó és felső határ:\n  Formátum: [alsó határ] [felső határ]\n  Példa: 32 97\n")
                    lower_limit = int(limits.split(" ")[0])  # Az alsó és felső határok meghatározása a bekért string szétválasztásával
                    upper_limit = int(limits.split(" ")[1])
                    break  # Ha az adatok bekérése hiba nélkül megtörtént, a program továbbhalad
                except ValueError:  # Ha a felhasználó nem számot írt be
                    print("Kérlek számokat írj be a kért formátumban.")
                except KeyboardInterrupt:  # CTRL + C
                    stop = True
                    break
                except:  # Rossz formátum
                    print("Érvénytelen. Próbálkozz újra.")

            if not stop:  # A program leáll, ha a felhasználó lenyomta a CTRL + C billentyűket
                numbers = []
                for i in range(amount):
                    x = random.randint(lower_limit, upper_limit)
                    numbers.append(x)  # Egy listához hozzáadjuk a kért mennyiségű véletlen számot
                
                with open("ki.txt", "w", encoding="utf-8") as f:  # A lista elemeit kiírjuk a ki.txt fájlba
                    for i in range(len(numbers)):
                        if i == 0:
                            f.write(str(numbers[i]))
                        else:
                            f.write(";" + str(numbers[i]))  # A számokat ;-vel választjuk el, de csak ha ez nem az első elem

        case 2:
            while True:  # Addig ismétlődik a bemenet kérése, amíg nem helyes
                try:
                    amount = int(input("Hány darab szövegrész legyen generálva? "))
                    break  # Ha az adatok bekérése hiba nélkül megtörtént, a program továbbhalad
                except ValueError:  # Ha a felhasználó nem számot írt be
                    print("Egy egész számot írj be.")
                except KeyboardInterrupt:  # CTRL + C
                    stop = True
                    break
                except:  # Más hiba
                    print("Hiba történt. Próbálkozz újra.")
            
            if not stop:  # A program leáll, ha a felhasználó lenyomta a CTRL + C billentyűket
                final_output = ""
                for i in range(amount):
                    output = ""
                    y = random.randint(1, 20)  # A szövegrész hossza
                    for j in range(y):
                        x = random.randint(0, len(alphabet) - 1)  # Véletlen karakter kiválasztása az angol abc-ből
                        output += str(alphabet[x])
                    if i == 0:
                        final_output += output
                    else:
                        final_output += ";" + output  # A szövegrészeket ;-vel választjuk el, de csak ha ez nem az első elem
                
                with open("ki.txt", "w", encoding="utf-8") as f:  # Az összes szövegrész kiírjuk a ki.txt fájlba
                    f.write(final_output)
        
        case 3:
            while True:  # Addig ismétlődik a bemenet kérése, amíg nem helyes
                try:
                    amount = int(input("Hány darab szám van generálva? "))
                    limits = input("Alsó és felső határ:\n  Formátum: [alsó határ] [felső határ]\n  Példa: 32 97\n")
                    lower_limit = int(limits.split(" ")[0])  # Az alsó és felső határok meghatározása a bekért string szétválasztásával
                    upper_limit = int(limits.split(" ")[1])
                    break  # Ha az adatok bekérése hiba nélkül megtörtént, a program továbbhalad
                except ValueError:  # Ha a felhasználó nem számot írt be
                    print("Kérlek számokat írj be a kért formátumban.")
                except KeyboardInterrupt:  # CTRL + C
                    stop = True
                    break
                except:  # Rossz formátum
                    print("Érvénytelen. Próbálkozz újra.")
            
            if not stop:  # A program leáll, ha a felhasználó lenyomta a CTRL + C billentyűket
                try:
                    with open("ki.txt", "r", encoding="utf-8") as f:
                        toCheck = f.readline()
                except:
                    print("A ki.txt fájl nem elérhető, vagy nem létezik")
                    stop = True
                if not stop:  # Ha a fájl nem létezik, a program leáll
                    check = toCheck.split(";")
                    isGood = True
                    if len(check) != amount:  # Ha a számok mennyisége nem egyezik, a fájl formátuma hibás
                        isGood = False
                    i = 0
                    line = list(check)
                    for x in line:
                        try:
                            x = int(x)
                        except:  # Ha az egyik elem nem (egész) szám, a fájl formátuma hibás
                            isGood = False
                            break
                        if x > upper_limit or x < lower_limit:  # Ha a szám a megadott határokon kívülre esik, a fájl formátuma hibás
                            isGood = False
                            break
                    
                    if isGood:
                        print("A fájl formátuma helyes.")
                    else:
                        print("A fájl formátuma helytelen.")
        
        case 4:
            while True:  # Addig ismétlődik a bemenet kérése, amíg nem helyes
                try:
                    amount = int(input("Hány darab írásjegy van generálva? "))
                    break  # Ha az adatok bekérése hiba nélkül megtörtént, a program továbbhalad
                except ValueError:  # Ha a felhasználó nem számot írt be
                    print("Egy egész számot írj be.")
                except KeyboardInterrupt:  # CTRL + C
                    stop = True
                    break
                except:  # Más hiba
                    print("Hiba történt. Próbálkozz újra.")

            if not stop:  # A program leáll, ha a felhasználó lenyomta a CTRL + C billentyűket
                try:
                    with open("ki.txt", "r", encoding="utf-8") as f:
                        toCheck = f.readline()
                except:
                    print("A ki.txt fájl nem elérhető, vagy nem létezik")
                    stop = True
                
                if not stop:  # Ha a fájl nem létezik, a program leáll
                    check = toCheck.split(";")
                    isGood = True
                    if len(check) != amount:  # Ha a szövegrészek mennyisége nem egyezik, a fájl formátuma hibás
                        isGood = False
                    i = 0
                    while True:
                        try:
                            line = check[i]
                            if len(line) > 20 or len(line) < 1:  # Ha a szövegrész hossza nem 1 és 20 közötti, a fájl formátuma hibás
                                isGood = False
                                break
                            line = list(line)
                            for x in line:
                                if x not in alphabet:  # Ha a szövegrész tartalmaz egy karakter, ami nem része az angol abc-nek, a fájl formátuma hibás
                                    isGood = False
                                    break
                            i += 1
                        except:  # A végigolvasás addig tart, amíg a program List Index Out Of Range Exception-t nem kap, azaz amíg érvényes indexekkel halad
                            break
                    
                    if isGood:
                        print("A fájl formátuma helyes.")
                    else:
                        print("A fájl formátuma helytelen.")