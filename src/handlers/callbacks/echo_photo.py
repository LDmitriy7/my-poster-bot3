from core import Context


async def echo_photo(ctx: Context):
    await ctx.send_message('!')
