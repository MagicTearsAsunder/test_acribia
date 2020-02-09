import os
import asyncio
import aiohttp
import aiofiles
from .models import Response
from django.conf import settings


async def exists_directory(session, url):
    async with session.head(url, allow_redirects=False) as response:
        if response.status == 200:
            Response.objects.create(response=f'Response from {url}: 200 OK')


async def main(url):
    tasks = []
    directories_list = os.path.join(
        settings.BASE_DIR, 'directories', 'directories_list.txt'
    )

    async with aiohttp.ClientSession() as session:
        async with aiofiles.open(directories_list, mode='r') as file:
            async for line in file:
                updated_url = url + line.rstrip()
                task = asyncio.create_task(
                    exists_directory(session, updated_url)
                )
                tasks.append(task)
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main(input('Enter url:\n')))
