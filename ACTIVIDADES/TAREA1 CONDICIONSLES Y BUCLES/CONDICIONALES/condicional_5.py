#elaborar un sistema donde se solicite el usuario los ingresos netos anuales y este indique si tiene que declarar renta y cuanto es el monto a declarar
ingresos = int(input("Ingrese los ingresos anueales que tiene:"))
uvt = ingresos / 38004
if uvt <= 1090:
    print("No debes pagar impuestos")
elif uvt <= 1700:
    uvt = (uvt - 1090) * 0.19
    impuesto = uvt * 38004
    print(f"la tarifa del impuesto que de be pagar es de ${impuesto:,}")
elif uvt <= 4100:
    uvt = (uvt - 1700) * 0.28 + 116
    impuesto = uvt * 38004
    print(f"la tarifa del impuesto que de be pagar es de ${impuesto:,}")
elif uvt <= 8670:
    uvt = (uvt - 4100) * 0.33 + 788
    impuesto = uvt * 38004
    print(f"la tarifa del impuesto que de be pagar es de ${impuesto:,}")
elif uvt <= 18970:
    uvt = (uvt - 8670) * 0.35 + 2296
    impuesto = uvt * 38004
    print(f"la tarifa del impuesto que de be pagar es de ${impuesto:,}")
elif uvt <= 31000:
    uvt = (uvt - 18970) * 0.37 + 5901
    impuesto = uvt * 38004
    print(f"la tarifa del impuesto que de be pagar es de ${impuesto:,}")
elif uvt > 31000:
    uvt = (uvt - 31000) * 0.39 + 10352
    impuesto = uvt * 38004
    print(f"la tarifa del impuesto que de be pagar es de ${impuesto:,}")
else:
    print("valor no aceptado")