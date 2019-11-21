'''Napisz trzy programy, które dla podanych liczb: wzrostu w cm i masy ciała w kg obliczą
i wypiszą współczynnik BMI, oraz podsumowanie informujące o stanie/zaleceniach.'''

masa = int(input('Podaj swoją wage w kg: '))
wzrost = int(input('Podaj swój wzrost w cm: '))
wzrost_m = wzrost / 100

bmi = masa / (wzrost_m**2)

print()
print(f'Mierzysz {wzrost}cm przy wadze {masa}kg.')
if bmi > 0 and bmi <= 18.5:
    print(f'Twoje BMI wynosi {bmi:.1f}. \nMusisz przytyć...szczęściarzu!')
elif bmi > 18.5 and bmi <= 24.9:
    print(f'Twoje BMI wynosi {bmi:.1f}. \nTwoja waga jest normie, gratulacje!')
elif bmi > 24.9 and bmi <= 29.9:
    print(f'Twoje BMI wynosi {bmi:.1f}. \nMasz nadwagę, uważaj na nią!')
elif bmi > 29.9 and bmi <= 39.9:
    print(f'Twoje BMI wynosi {bmi:.1f}. \nCierpisz na I stopień otyłości! Schudnij!')
elif bmi > 39.9 and bmi < 60:
    print(f'Twoje BMI wynosi {bmi:.1f}. \nCierpisz na ciężką otyłość! Opanuj się!')
else:
    print('Coś poszło zdecydowanie nie tak. Wpisałeś złe dane?')