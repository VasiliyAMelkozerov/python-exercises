def is_vowel(x):
    if x.lower() in 'aeiou' or 'y':
        return True
    else:
        return False

def calculate_tip(x,y):
    return int(x) * float(y)

def get_def_letter(x):
    x =int(x)
    if x >= 90:
        return "A"
    elif x >= 80:
        return "B"
    elif x >= 70:
        return "C"
    elif x >= 60:
        return "D"
    elif 59 >= x >= 0:
        return "F"
    else:
        return False