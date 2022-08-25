from core import UpdateContext


async def echo_photo(ctx: UpdateContext):
    await ctx.send_photo(ctx.photo_id)
