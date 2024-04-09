import aiohttp_jinja2

from aiohttp import web

from .models import *

@aiohttp_jinja2.template('users.html')
async def index(request):
    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute(user.select())
        records = await cursor.fetchall()
        users = [dict(r) for r in records]
        return {'users': users}