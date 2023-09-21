import random
import string

alphabet = list(string.ascii_letters)
stop = False

while True:
    try:
        choice = int(input("Generálási mód kiválasztása:\n  Írj be egy pozitív egész számot 1-4-ig\n    1: ki.txt generálása véletlen számokkal\n    2: ki.txt generálása véletlen karakterekkel\n    3: ki.txt formátumának ellenőrzése - véletlen számokkal\n    4: ki.txt formátumának ellenőrzése - véletlen karakterekkel\n"))
        if 1 <= choice <= 4:
            break
        else:
            print("A szám legyen nagyobb, vagy egyenlő, mint 1, és kisebb, vagy egyenlő, mint 4")
    except ValueError:
        print("Egy egész számot írj be.")
    except KeyboardInterrupt:
        stop = True
        break
    except:
        print("Hiba történt. Próbálkozz újra.")


if not stop:
    match choice:
        case 1:
            while True:
                try:
                    amount = int(input("Hány darab szám legyen generálva? "))
                    limits = input("Alsó és felső határ:\n  Formátum: [alsó határ] [felső határ]\n  Példa: 32 97\n")
                    lower_limit = int(limits.split(" ")[0])
                    upper_limit = int(limits.split(" ")[1])
                    break
                except ValueError:
                    print("Kérlek számokat írj be a kért formátumban.")
                except KeyboardInterrupt:
                    stop = True
                    break
                except:
                    print("Érvénytelen. Próbálkozz újra.")

            if not stop:
                numbers = []
                for i in range(amount):
                    x = random.randint(lower_limit, upper_limit)
                    numbers.append(x)
                
                with open("ki.txt", "w", encoding="utf-8") as f:
                    for i in range(len(numbers)):
                        if i == 0:
                            f.write(str(numbers[i]))
                        else:
                            f.write(";" + str(numbers[i]))

        case 2:
            while True:
                try:
                    amount = int(input("Hány darab szövegrész legyen generálva? "))
                    break
                except ValueError:
                    print("Egy egész számot írj be.")
                except KeyboardInterrupt:
                    stop = True
                    break
                except:
                    print("Hiba történt. Próbálkozz újra.")
            
            if not stop:
                final_output = ""
                for i in range(amount):
                    output = ""
                    y = random.randint(1, 20)
                    for j in range(y):
                        x = random.randint(0, len(alphabet) - 1)
                        output += str(alphabet[x])
                    if i == 0:
                        final_output += output
                    else:
                        final_output += ";" + output
                
                with open("ki.txt", "w", encoding="utf-8") as f:
                    f.write(final_output)
        
        case 3:
            while True:
                try:
                    amount = int(input("Hány darab szám van generálva? "))
                    limits = input("Alsó és felső határ:\n  Formátum: [alsó határ] [felső határ]\n  Példa: 32 97\n")
                    lower_limit = int(limits.split(" ")[0])
                    upper_limit = int(limits.split(" ")[1])
                    break
                except ValueError:
                    print("Kérlek számokat írj be a kért formátumban.")
                except KeyboardInterrupt:
                    stop = True
                    break
                except:
                    print("Érvénytelen. Próbálkozz újra.")
            
            if not stop:
                try:
                    with open("ki.txt", "r", encoding="utf-8") as f:
                        toCheck = f.readline()
                except:
                    stop = True
                if not stop:
                    check = toCheck.split(";")
                    isGood = True
                    if len(check) != amount:
                        isGood = False
                    i = 0
                    line = list(check)
                    for x in line:
                        try:
                            x = int(x)
                        except:
                            isGood = False
                            break
                        if x > upper_limit or x < lower_limit:
                            isGood = False
                            break
                    
                    if isGood:
                        print("A fájl formátuma helyes.")
                    else:
                        print("A fájl formátuma helytelen.")
        
        case 4:
            while True:
                try:
                    amount = int(input("Hány darab írásjegy van generálva? "))
                    break
                except ValueError:
                    print("Egy egész számot írj be.")
                except KeyboardInterrupt:
                    stop = True
                    break
                except:
                    print("Hiba történt. Próbálkozz újra.")

            if not stop:
                try:
                    with open("ki.txt", "r", encoding="utf-8") as f:
                        toCheck = f.readline()
                except:
                    stop = True
                
                if not stop:
                    check = toCheck.split(";")
                    isGood = True
                    if len(check) != amount:
                        isGood = False
                    i = 0
                    while True:
                        try:
                            line = check[i]
                            if len(line) > 20 or len(line) < 1:
                                isGood = False
                                break
                            line = list(line)
                            for x in line:
                                if x not in alphabet:
                                    isGood = False
                                    break
                            i += 1
                        except:
                            break
                    
                    if isGood:
                        print("A fájl formátuma helyes.")
                    else:
                        print("A fájl formátuma helytelen.")