# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:47:00 2024

@author: KIEUNHI
"""

# Bai tap tam giac

a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if a+b>c and a+c>b and b+c>a:
    # Tam giác cân
    if a == b == c:
        print("a,b,c là 3 cạnh của tam giác và đây là tam giác đều")
    # Tam giác cân
    elif a == b or a == c or b == c:
        print("a,b,c là 3 cạnh của tam giác và đây là tam giác cân")
    # Tam giác vuông
    elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        print("a,b,c là 3 cạnh của tam giác và đây là tam giác vuông")
    else:
        print("a,b,c là 3 cạnh của tam giác")
else:
    print("a,b,c không là 3 cạnh của tam giác")
        
    
    