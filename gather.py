import asyncio

async def obtener_datos(year):
    print(f"Consultando year {year}")
    await asyncio.sleep(2)  # simula BD
    return f"datos_{year}"

async def main():
    years = [1, 2, 3, 4, 5, 6]

    resultados = await asyncio.gather(
        *[obtener_datos(year) for year in years] # el simbolo "*" sirve para desempaquetar la lista
    )

    print(resultados)

asyncio.run(main())