from core import Context


async def send_logs(ctx: Context):
    await ctx.send_document('.log', filename='logs.txt')
