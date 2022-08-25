from core import UpdateContext


async def send_logs(ctx: UpdateContext):
    await ctx.send_document('.log', filename='logs.txt')
