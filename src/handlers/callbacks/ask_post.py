from core import Context


async def ask_post(ctx: Context):
    await ctx.send_message('Отправь мне пост')
