# Temperature Conversion Program

end = False
deg = chr(176)

#program greeting
print('''This program converts the temperature from one scale 
to another (Fahrenheit/Celsius/Kelvin)''')

while not end:
    which = int(input('''\nEnter:
(1) to convert from Celsius to Kelvin
(2) to convert from Celsius to Fahrenheit
(3) to convert from Fahrenheit to Celsius
(4) to convert from Fahrenheit to Kelvin
(5) to convert from Kelvin to Fahrenheit
(6) to convert from Kelvin to Celsius
Enter your choice: '''))

    while not(1<= which <= 6):
        which = int(input('\nINVALID INPUT\nEnter your choice(1-6): '))
        
    temp = float(input('\nEnter the tempetature to be converted: '))
    
    confirm = False
    while not confirm:
        if which == 1 or which == 2:
            while temp < -273.15:
                print('The temperature cannot be lesser than the\n absolute 0 of Celsius (-273.15)')
                temp = float(input('\nEnter another temperature value: '))
            if which == 1:
                conv = format(temp + 273.15, '.2f')
                print(str(temp)+ deg +'C is equivalent to',str(conv)+'K')
                confirm = True
            else:
                 conv = format(9 / 5 * temp + 32, '.2f')
                 print(str(temp)+ deg + 'C is equivalent to', str(conv) + deg + 'F')
                 confirm = True
        elif which in (3,4):
            while temp < -459.67:
                print('The temperature cannot be lesser than the\n absolute 0 of Fahrenheit (-459.67)')
                temp = float(input('\nEnter another temperature value: '))
            if which == 3:
                conv = format(5 / 9 * (temp - 32), '.2f')
                print(str(temp) + deg + 'F is equivalent to', str(conv) + deg + 'C')
                confirm = True
            else:
                conv = format(float(format(5 / 9 * (temp - 32), '.2f')) + 273.15, '.2f')
                print(str(temp) + deg + 'F is equivalent to', str(conv) + 'K')
                confirm = True
        else:
            while temp < 0:
                print('The temperature cannot be lesser than the\n absolute 0 of kelvin(0.0)')
                temp = float(input('Enter another temperature value: '))
            if which == 5:
                conv =format(float(format(9 / 5 * (temp - 273.15), '.2f')) + 32, '.2f')
                print(str(temp) + 'K is equivalent to', str(conv) + deg + 'F')
                confirm = True
            else:
                conv = format(temp - 273.15, '.2f')
                print(str(temp) + 'K is equivalent to', str(conv) + deg + 'C')
                confirm = True
        next = input('\nWould you like to continue\n Enter (y/n): ')
        while next not in('y', 'n'):
            next = input('Enter(y/ n): ')
        if next == 'n':
             end = True
            