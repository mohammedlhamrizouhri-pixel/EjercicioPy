def linea_ticket(producto: str, unidades: int, precio: float) -> str:
    importe: float = unidades * precio
    return "{producto:<12}{unidades:>3} x {precio:>6.2f} = {importe:>8.2f} €"