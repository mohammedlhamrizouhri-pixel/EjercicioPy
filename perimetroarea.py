def area_y_perimetro(base: float, altura: float) -> tuple[float, float]:
    return base * altura, 2 * (base + altura)

area, perimetro = area_y_perimetro (4,3) #12.0 y 14.0
print(f" El Area es: {area} y el perimetro es: {perimetro}")