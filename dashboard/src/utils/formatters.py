def fmt_brl(value: float) -> str:
    """R$ 1.234,56"""
    try:
        return f"R$ {float(value):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except (TypeError, ValueError):
        return "R$ 0,00"
 
 
def fmt_int_br(value: int) -> str:
    """1.234.567"""
    try:
        return f"{int(value):,}".replace(",", ".")
    except (TypeError, ValueError):
        return "0"
 
 
def fmt_compact(value: float) -> str:
    """R$ 1,42 B  /  R$ 14,20 M  /  R$ 142,0 K"""
    try:
        val = float(value)
        if val >= 1_000_000_000:
            return f"R$ {val / 1_000_000_000:.2f} B".replace(".", ",")
        if val >= 1_000_000:
            return f"R$ {val / 1_000_000:.2f} M".replace(".", ",")
        if val >= 1_000:
            return f"R$ {val / 1_000:.1f} K".replace(".", ",")
        return fmt_brl(val)
    except (TypeError, ValueError):
        return "R$ 0,00"
 
