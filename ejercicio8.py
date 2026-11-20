IVA: int = 21


def desglose(unidades: int, precio: float) -> tuple[float, float, float]:
    """Base, IVA y total de una compra, redondeados a 2 decimales."""
    base: float = unidades * precio
    iva: float = base * IVA / 100
    return round(base, 2), round(iva, 2), round(base + iva, 2)