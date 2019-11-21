'''Potem napisz program, który prosi użytkownika (przez `input()`),
żeby podał, ile kosztuje kilo ziemniaków, ile kilo ziemniaków chce kupić,
ile kosztuje kilo bananów i ile kilo bananów chce kupić. Niech program policzy i wyświetli,
ile trzeba będzie zapłacić za te ziemniaki i banany razem. I niech program sprawdzi i powie,
za co trzeba będzie zapłacić więcej - za banany czy za ziemniaki.'''

ziemniaki_cena = float(input('Ile ziemniaków chcesz kupić? '))
ziemniaki_ilosc = float(input('Jaka jest cena za 1kg ziemniaków? '))
banany_cena = float(input('Ile bananów chcesz kupić? '))
banany_ilosc = float(input('Jaka jest cena za 1kg bananów? '))
print()
ziemniaki_naleznosc = ziemniaki_cena * ziemniaki_ilosc
banany_naleznosc = banany_cena * banany_ilosc
print(f'Za {ziemniaki_ilosc}kg ziemniaków należy zapłacić {ziemniaki_naleznosc:.2f}zł.')
print(f'Za {banany_ilosc}kg bananów należy zapłacić {banany_naleznosc:.2f}zł.')
print(f'W sumie należy zapłacić {ziemniaki_naleznosc + banany_naleznosc:.2f}zł.')
print()
if ziemniaki_naleznosc > banany_naleznosc:
    print('Większość kwoty to koszt ziemniaków')
elif banany_naleznosc > ziemniaki_naleznosc:
    print('Większość kwoty to koszt bananów')
else:
    print('Za oba towary należy zapłacić tyle samo')
