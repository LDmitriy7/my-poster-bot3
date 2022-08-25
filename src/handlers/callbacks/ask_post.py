from core import UpdateContext


async def ask_post(ctx: UpdateContext):
    await ctx.send_message('Отправь мне пост')
