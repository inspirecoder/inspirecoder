# Testing slicing (+/-) with tuple data type values.
# tuple_slicing_nve.py
tuple_2 = ("a",1.2,6,"armour",7,4.6,"shield")
print("\ntuple_2 elements are : \n\t",tuple_2)
print("\n[:-3] is:\n\t",tuple_2[:-3])
print("\n[:4:-1] is:\n\t",tuple_2[:4:-1])
print("\n[-2::1] is:\n\t",tuple_2[-2::1])
print("\n[-3:-6:1] is:\n\t",tuple_2[-3:-6:1])
print("\n[-4:-6:-2] is:\n\t",tuple_2[-4:-6:-2])
print("\n[-2:-4:-1] is:\n\t",tuple_2[-2:-4:-1])

'''
Output :

tuple_2 elements are : 
	 ('a', 1.2, 6, 'armour', 7, 4.6, 'shield')

[:-3] is:
	 ('a', 1.2, 6, 'armour')

[:4:-1] is:
	 ('shield', 4.6)

[-2::1] is:
	 (4.6, 'shield')

[-3:-6:1] is:
	 ()

[-4:-6:-2] is:
	 ('armour',)

[-2:-4:-1] is:
	 (4.6, 7)
   '''
  
