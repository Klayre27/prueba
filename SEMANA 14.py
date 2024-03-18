# Definición de la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento en una compra.

    Parámetros:
        monto_total (float): El monto total de la compra.
        porcentaje_descuento (float, opcional): El porcentaje de descuento a aplicar, por defecto es 10%.

    Retorna:
        float: El monto del descuento calculado.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Llamada a la función calcular_descuento
monto_compra1 = 100
descuento1 = calcular_descuento(monto_compra1)
monto_final1 = monto_compra1 - descuento1
print(f"Compra 1 - Monto total: ${monto_compra1}, Descuento: ${descuento1}, Monto final a pagar: ${monto_final1}")

monto_compra2 = 200
porcentaje_descuento2 = 20
descuento2 = calcular_descuento(monto_compra2, porcentaje_descuento2)
monto_final2 = monto_compra2 - descuento2
print(f"Compra 2 - Monto total: ${monto_compra2}, Descuento: ${descuento2}, Monto final a pagar: ${monto_final2}")