'''Napisz taki program: użytkownik ma podać, w jaki dzień tygodnia oddał buty do szewca 
(poniedziałek to dzień 1, wtorek to dzień 2 itp.). Ma też podać, ile dni będzie trwała naprawa. 

Program ma wypisać, w jaki dzień tygodnia buty będą gotowe do odbioru. 
Jeśli tak będzie ci wygodniej, możesz założyć, że naprawa butów nigdy nie będzie trwała dłużej niż siedem dni.'''

dzien = int(input('W który dzień tygodnia oddałeś buty do szewca? '))
naprawa = int(input('Ile dni będzie trwała naprawa? '))

odbior = dzien + naprawa


if odbior % 7 == 0:
    print('Zamówienie będzie gotowe w niedziele')
elif odbior % 6 == 0:
    print('Zamówienie będzie gotowe w sobotę')
elif odbior % 5 == 0:
    print('Zamówienie będzie gotowe w piątek')
elif odbior % 4 == 0:
    print('Zamówienie będzie gotowe w czwartek')
elif odbior % 3 == 0:
    print('Zamówienie będzie gotowe w środę')
elif odbior % 2 == 0:
    print('Zamówienie będzie gotowe we wtorek')
else:
    print('Zamówienie będzie gotowe w poniedziałek')