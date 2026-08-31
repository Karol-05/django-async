import asyncio
from django.http import HttpResponse


async def contador(request):
    for numero in range(1, 6):
        await asyncio.sleep(1)
        print(numero)

    return HttpResponse("Contador finalizado!")