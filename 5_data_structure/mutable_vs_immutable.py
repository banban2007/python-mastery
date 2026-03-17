# mutable_vs_immutable

print('------------List----------')

print('Ls  ', ['a'])
print('Li  ', [1])
print('Lf  ', [1.1])
print('Lb  ', [True])
print('LL  ', [[1,2,3]])
print('LT  ', [(1,2,3)])
print('LS  ', [{1,2,3}])
print('LD  ', [{1:'a'}])

print('------------Tuple----------')

print('Ts  ', ('a',))
print('Ti  ', (1,))
print('Tf  ', (1.1,))
print('Tb  ', (True,))
print('TL  ', ([1,2,3],))
print('TT  ', ((1,2,3),))
print('TS  ', ({1,2,3},))
print('TD  ', ({1:'a'},))

print('------------Set----------')

print('Ss  ', {'a'})
print('Si  ', {1})
print('Sf  ', {1.1})
print('Sb  ', {True})
#print('SL  ', {[1,2,3]}) #TypeError: unhashable type: 'list'
print('ST  ', {(1,2,3)})
#print('SS  ', {{1,2,3}}) #TypeError: unhashable type: 'set'
#print('SD  ', {{1:'a'}}) #TypeError: unhashable type: 'dict'

print('------------Dict Key----------')

print('Dks  ', {'k':'v'})
print('Dki  ', {1:'v'})
print('Dkf  ', {1.1:'v'})
print('Dkb  ', {True:'v'})
#print('DkL  ', {['a']:'v'})#TypeError: unhashable type: 'list'
print('DkT  ', {('a'):'v'})
#print('DkS  ', {{'a'}:'v'})#TypeError: unhashable type: 'set'
#print('DkD  ', {{'k':'v'}:'v'})#TypeError: unhashable type: 'dict'

print('------------Dict Value----------')

print('Dvs  ', {'k':'v'})
print('Dvi  ', {'k':1})
print('Dvf  ', {'k':1.1})
print('Dvb  ', {'k':True})
print('DvL  ', {'k': ['v']})
print('DvT  ', {'k':('v')})
print('DvS  ', {'k':{'v'}})
print('DvD  ', {'k':{'k':'v'}})

