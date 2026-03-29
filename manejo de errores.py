import asyncio

async def division(n,n2):
    try:
        res = n/n2
    except ZeroDivisionError:
        print("Se dectecto un eror de division por zero")
        res = 0
    await asyncio.sleep(2)
    return res


async def main():
    res =  await asyncio.gather(division(1,2), division(2,0), division(3,1))
    print(res)


asyncio.run(main())