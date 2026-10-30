def metodo_productos_medios():
  print("--- MÉTODO: PRODUCTOS MEDIOS ---")
  try:
    s1 = int(input("Introduce la primera semilla (S1): "))
    s2 = int(input("Introduce la segunda semilla (S2): "))
    n = int(
        input(
            "Introduce el número de dígitos de las semillas (n, ej. 4 para 1234):"
            " "
        )
    )
    iteraciones = int(
        input("¿Cuántos números aleatorios deseas generar?: ")
    )
  except ValueError:
    print("Entrada inválida. Asegúrate de ingresar números enteros.")
    return

  print("\n--- INICIO DE GENERACIÓN ---")
  for i in range(iteraciones):
    # 1. Multiplicar las semillas
    p = s1 * s2
    p_str = str(p)

    # Asegurar longitud doble para extraer la parte central correctamente
    target_len = 2 * n
    p_str_padded = p_str.zfill(target_len)

    # 2. Extraer n dígitos centrales
    total_len = len(p_str_padded)
    start = (total_len - n) // 2
    end = start + n
    x_str = p_str_padded[start:end]
    x = int(x_str)

    print(f"Iteración {i+1}:")
    print(f"  Operación: {s1} * {s2} = {p}")
    print(f"  Dígitos centrales extraídos: {x_str}")
    print(f"  Nuevo Número (X): {x}")
    print("-" * 30)

    # 3. Actualizar variables para la siguiente iteración (S1 = S2, S2 = X)
    s1 = s2
    s2 = x


if __name__ == "__main__":
  metodo_productos_medios()