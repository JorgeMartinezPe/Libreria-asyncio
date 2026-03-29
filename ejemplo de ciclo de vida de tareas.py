import asyncio

async def preparar_pedido(nombre, tiempo):
    print(f"Preparando pedido: {nombre}")
    await asyncio.sleep(tiempo)
    print(f"Pedido listo: {nombre}")
    return nombre

async def main():
    print("Llegan pedidos...")

    # Se lanzan tareas en background
    tarea1 = asyncio.create_task(preparar_pedido("Hamburguesa", 3))
    tarea2 = asyncio.create_task(preparar_pedido("Pizza", 2))
    tarea3 = asyncio.create_task(preparar_pedido("Tacos", 1))

    print("El sistema sigue recibiendo pedidos...")

    # Simulamos que el sistema hace otras cosas
    for i in range(3):
        print(f"Procesando sistema... {i}")
        await asyncio.sleep(1)

    # Esperamos resultados al final
    resultados = await asyncio.gather(tarea1, tarea2, tarea3)

    print("Pedidos completados:", resultados)

asyncio.run(main())