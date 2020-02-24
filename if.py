# GET VALUES BY CONSOLE ___________________________________
guyAge = int(input('Type age guy'))
girlAge = int(input('Type age girl'))

# IF ___________________________________
# == != <= >= and or
if (guyAge > girlAge):
    print('Guy with age', guyAge)
    if (guyAge >= 18):
        print('Guy major')
    else:
        print('Guy minor')
else:
    print('Girl with age', girlAge)
    if (girlAge >= 18):
        print('Girl major')
    else:
        print('Girl minor')

if(guyAge == girlAge) and (guyAge > 18):
    print('Guy with age', guyAge)
elif (girlAge == guyAge == 18):
    print('Equal age')
