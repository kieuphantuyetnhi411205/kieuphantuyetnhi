# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:45:52 2024

@author: KIEUNHI
"""

#Bai tap GPA
GPA = float(input("Nhập điểm trung bình (GPA):"))

if GPA < 3.5:
    print("Học lực Kém")
elif GPA >= 3.5 and GPA < 5.0:
    print("Học lực Yếu")
elif GPA >= 5.0 and GPA < 7.0:
    print("Học lực Trung bình")
elif GPA >= 7.0 and GPA < 8.0:
    print("Học lực Khá")
elif GPA >= 8.0 and GPA < 9.0:
    print("Học lực Giỏi")
else:
    print("Học lực Xuất sắc")
    