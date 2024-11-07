# Q1
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

norway_pandemic()