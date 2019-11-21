'''Napisz program, który prosi użytkownika (przez `input()`),
żeby podał, ile kosztuje kilo ziemniaków. Niech program policzy i wyświetli,
ile trzeba będzie zapłacić za pięć kilo ziemniaków.'''

kg = 5

cena = float(input('Podaj aktualną cene za 1kg ziemniaków: '))
naleznosc = cena * kg

print(f'Za 5kg ziemniaków należy zapłacić {naleznosc:.2f}zł')
