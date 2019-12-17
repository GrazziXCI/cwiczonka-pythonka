'''Napisz dekorator `crazy_case`, który co drugą literę w słowie będzie zamieniał na dużą. '''

def crazy_case(func):
    def wrapper(*args, **kwargs):
        wynik = func(*args, **kwargs)
        ret = ''
        i = True
        for char in wynik:
            if i:
                ret += char.upper()
            else:
                ret += char.lower()
            if char != ' ':
                i = not i
        return ret

    return wrapper

@crazy_case
def powiedz_ala():
    return 'Ala ma kota'


print(powiedz_ala())