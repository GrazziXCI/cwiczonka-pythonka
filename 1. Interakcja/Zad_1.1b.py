'''Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał,
ile kosztuje kilo ziemniaków i ile kilo chce kupić. Niech program policzy i wyświetli,
ile trzeba będzie zapłacić za te ziemniaki.'''

ilosc = float(input(' Ile kg ziemniaków chcesz kupić? '))
cena = float(input('Jaka jest cena za 1kg ziemniaków? '))

naleznosc = ilosc * cena

print(f'Za {ilosc}kg ziemniaków należy zapłacić {naleznosc:.2f}zł')