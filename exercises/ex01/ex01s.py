# Q1 Pandemic rules
def norway_pandemic():
    region = input("Hvor er du bosatt? ")
    if region[0] == "V" or region[1] == "V":
        print("Velkommen til Norge!")
        return
    else:
        vaccine = input("Er du fullvaksinert?")
        if vaccine == "ja":
            print("Velkommen til Norge!")
            return
        else:
            covid = input("Har du gjennomgått koronasykdom de siste seks månedene?")
            if covid == "ja":
                print("Velkommen til Norge!")
                return
            else:
                print("Velkommen til Norge, men du må teste deg och sitte i karantene.")

# norway_pandemic()


# Q2 Ordering drinks
def price(drinks):
    prices = [("kaffe", 30), ("öl", 50), ("kola", 25)]
    [qty, name] = drinks.split()
    for (item, rate) in prices:
        if item == name:
            return rate*int(qty)
    return 0

def get_order():
    order = input("Vad vill ni dricka? ")
    total = 0
    while order != "Det är bra så":
        p = price(order)
        if p == 0:
            print("Finns tyvärr inte ")
        total += p
        order = input("Något mer? ")
    print("Det blir", total, "kronor")

#get_order()

# Q3 Scrambled text


