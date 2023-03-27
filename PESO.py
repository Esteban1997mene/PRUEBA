#HARRY
peso_en_tierra = float(input("Introduce el peso en la Tierra (en kg): "))
gravedad_en_tierra = 9.81
gravedad_en_luna = 1.62
peso_en_luna = (peso_en_tierra / gravedad_en_tierra) * gravedad_en_luna
print("El peso en la Luna es de", round(peso_en_luna, 2), "kg.")
#ANDRES

gravedad_en_marte = 9.62
peso_en_marte = (peso_en_tierra / gravedad_en_tierra) * gravedad_en_marte
print("El peso en la Luna es de", round(peso_en_marte, 2), "kg.")
