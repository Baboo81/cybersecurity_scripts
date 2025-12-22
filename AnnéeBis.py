#!/usr/bin/env python3


#TP : Cette année est-elle bissextile ?

year = input("Saisissez une année : ");

year = int(year);

bissextile = False;

if year % 400 == 0:
    bissextile = True;
elif year % 100 == 0:
    bissextile = False;
elif year % 4 == 0:
    bissextile = True;
else: 
    bissextile = False;
if bissextile:
    print("L'année est bissextile !");
else:
    print("L'année n'est pas bissextile !");



