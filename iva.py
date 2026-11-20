def precio_e_IVA(precio: float, IVA: int = 21 ) -> float:
    return precio*(1 + IVA /100)

print(precio_e_IVA()) #121.0 (usa 21)
print(precio_e_IVA(100,0))  