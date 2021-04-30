print("From which unit you want to convert the vale ?mm,cm,dm,m,Dm,hm,km")
name1 = input()
name2 = input("In which value you want to convert?cm,dm,m,Dm,hm,km")
while 2 > 1 :
    try:
        name3 = input("Enter the Value")
        name3 = int(name3)
        break
    except:
        print("enter a valid  number")
        continue
if name1 == "mm":
    if name2 == "mm" :
        mm_to_mm = name3
        print(f'{mm_to_mm} {name2}')
    if name2 == "cm" :
        mm_to_cm = name3 / 10
        print(f'{mm_to_cm} {name2}')
    if name2 == "dm" :
        mm_to_dm = name3 / 100
        print(f'{mm_to_dm} {name2}')
    if name2 == "m" :
        mm_to_m = name3 / 1000
        print(f'{mm_to_m} {name2}')
    if name2 == "Dm" :
        mm_to_Dm = name3 / 10000
        print(f'{mm_to_Dm} {name2}')
    if name2 == "hm" :
        mm_to_hm = name3 / 100000
        print(f'{mm_to_hm} {name2}')
    if name2 == "km" :
        mm_to_km = name3 / 1000000
        print(f'{mm_to_km} {name2}')

if name1 == "cm":
    if name2 == "mm" :
        mm_to_mm = name3 * 10
        print(f'{mm_to_mm} {name2}')
    if name2 == "cm" :
        mm_to_cm = name3
        print(f'{mm_to_cm} {name2}')
    if name2 == "dm" :
        mm_to_dm = name3 / 10
        print(f'{mm_to_dm} {name2}')
    if name2 == "m" :
        mm_to_m = name3 / 100
        print(f'{mm_to_m} {name2}')
    if name2 == "Dm" :
        mm_to_Dm = name3 / 1000
        print(f'{mm_to_Dm} {name2}')
    if name2 == "hm" :
        mm_to_hm = name3 / 10000
        print(f'{mm_to_hm} {name2}')
    if name2 == "km" :
        mm_to_km = name3 / 100000
        print(f'{mm_to_km} {name2}')

if name1 == "dm":
    if name2 == "mm" :
        mm_to_mm = name3 * 100
        print(f'{mm_to_mm} {name2}')
    if name2 == "cm" :
        mm_to_cm = name3 * 10
        print(f'{mm_to_cm} {name2}')
    if name2 == "dm" :
        mm_to_dm = name3
        print(f'{mm_to_dm} {name2}')
    if name2 == "m" :
        mm_to_m = name3 / 10
        print(f'{mm_to_m} {name2}')
    if name2 == "Dm" :
        mm_to_Dm = name3 / 100
        print(f'{mm_to_Dm} {name2}')
    if name2 == "hm" :
        mm_to_hm = name3 / 1000
        print(f'{mm_to_hm} {name2}')
    if name2 == "km" :
        mm_to_km = name3 / 10000
        print(f'{mm_to_km} {name2}')

if name1 == "m":
    if name2 == "mm" :
        mm_to_mm = name3 * 1000
        print(f'{mm_to_mm} {name2}')
    if name2 == "cm" :
        mm_to_cm = name3 * 100
        print(f'{mm_to_cm} {name2}')
    if name2 == "dm" :
        mm_to_dm = name3 * 10
        print(f'{mm_to_dm} {name2}')
    if name2 == "m" :
        mm_to_m = name3
        print(f'{mm_to_m} {name2}')
    if name2 == "Dm" :
        mm_to_Dm = name3 / 100
        print(f'{mm_to_Dm} {name2}')
    if name2 == "hm" :
        mm_to_hm = name3 / 1000
        print(f'{mm_to_hm} {name2}')
    if name2 == "km" :
        mm_to_km = name3 / 10000
        print(f'{mm_to_km} {name2}')

if name1 == "Dm":
    if name2 == "mm" :
        mm_to_mm = name3 * 10000
        print(f'{mm_to_mm} {name2}')
    if name2 == "cm" :
        mm_to_cm = name3 * 1000
        print(f'{mm_to_cm} {name2}')
    if name2 == "dm" :
        mm_to_dm = name3 * 100
        print(f'{mm_to_dm} {name2}')
    if name2 == "m" :
        mm_to_m = name3 * 10
        print(f'{mm_to_m} {name2}')
    if name2 == "Dm" :
        mm_to_Dm = name3
        print(f'{mm_to_Dm} {name2}')
    if name2 == "hm" :
        mm_to_hm = name3 / 10
        print(f'{mm_to_hm} {name2}')
    if name2 == "km" :
        mm_to_km = name3 / 100
        print(f'{mm_to_km} {name2}')

if name1 == "hm":
    if name2 == "mm" :
        mm_to_mm = name3 * 100000
        print(f'{mm_to_mm} {name2}')
    if name2 == "cm" :
        mm_to_cm = name3 * 10000
        print(f'{mm_to_cm} {name2}')
    if name2 == "dm" :
        mm_to_dm = name3 * 1000
        print(f'{mm_to_dm} {name2}')
    if name2 == "m" :
        mm_to_m = name3 * 100
        print(f'{mm_to_m} {name2}')
    if name2 == "Dm" :
        mm_to_Dm = name3 * 10
        print(f'{mm_to_Dm} {name2}')
    if name2 == "hm" :
        mm_to_hm = name3
        print(f'{mm_to_hm} {name2}')
    if name2 == "km" :
        mm_to_km = name3 / 10
        print(f'{mm_to_km} {name2}')

if name1 == "km":
    if name2 == "mm" :
        mm_to_mm = name3 * 1000000
        print(f'{mm_to_mm} {name2}')
    if name2 == "cm" :
        mm_to_cm = name3 * 100000
        print(f'{mm_to_cm} {name2}')
    if name2 == "dm" :
        mm_to_dm = name3 * 10000
        print(f'{mm_to_dm} {name2}')
    if name2 == "m" :
        mm_to_m = name3 * 1000
        print(f'{mm_to_m} {name2}')
    if name2 == "Dm" :
        mm_to_Dm = name3 * 100
        print(f'{mm_to_Dm} {name2}')
    if name2 == "hm" :
        mm_to_hm = name3 * 10
        print(f'{mm_to_hm} {name2}')
    if name2 == "km" :
        mm_to_km = name3
        print(f'{mm_to_km} {name2}')