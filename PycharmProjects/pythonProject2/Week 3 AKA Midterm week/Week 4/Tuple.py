def area_perimeter (a,b=10):
    area = a*b
    perimeter = 2*a+2*b
    return (area,perimeter)
(area_1, peri_1) = area_perimeter(3,5)
print("area =",area_1)
print("perimeteter =",peri_1)