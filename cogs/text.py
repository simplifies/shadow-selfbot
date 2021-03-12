import discord
from datetime import datetime
from discord.ext import commands
from main import PREFIX, bot, EMBEDCOLOUR


class Text(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="text", description="Main text command.", usage="")
    async def text(self, ctx):
        embed = discord.Embed(title="📝 Text Commands",
                              description=f"""
`{PREFIX}`**secret [message]** » Send all your messages in a secret block.
`{PREFIX}`**secretletters [message]** » Put all lettes from your message into separate secret blocks.
`{PREFIX}`**bold [message]** » Send all your messages in bold.
`{PREFIX}`**italic [message]** » Send all your messages in italics.
`{PREFIX}`**cpp [message]** » Send all your messages in a C++ code block.
`{PREFIX}`**cs [message]** » Send all your messages in a C Sharp code block.
`{PREFIX}`**java [message]** » Send all your messages in a Java code block.
`{PREFIX}`**python [message]** » Send all your messages in a Python code block.
`{PREFIX}`**js [message]** » Send all your messages in a JavaScript code block.
`{PREFIX}`**lua [message]** » Send all your messages in a Lua code block.
`{PREFIX}`**php [message]** » Send all your messages in a PHP code block.
`{PREFIX}`**html [message]** » Send all your messages in a HTML code block.
`{PREFIX}`**css [message]** » Send all your messages in a CSS code block.
`{PREFIX}`**yaml [message]** » Send all your messages in a YAML code block.
`{PREFIX}`**json [message]** » Send all your messages in a JSON code block.
""",
                              color=EMBEDCOLOUR)
        embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
        embed.timestamp = datetime.now()
        await ctx.send(embed=embed)

    @commands.command(name="secret", description="Send all your messages in a secret block.", usage=" [message]")
    async def secret(self, ctx, *, message):
        await ctx.send('||' + message + '||')

    @commands.command(name="secretletters", description="Put all lettes from your message into separate secret blocks.", usage=" [message]")
    async def secretletters(self, ctx, *, message):
        def split(word):
            return list(word)
        msg = ""
        for letter in split(message):
            msg += "||" + letter +  "||"
        await ctx.send(msg)

    @commands.command(name="bold", description="Send all your messages in bold.", usage=" [message]")
    async def bold(self, ctx, *, message):
        await ctx.send('**' + message + '**')

    @commands.command(name="italic", description="Send all your messages in italics.", usage=" [message]")
    async def italic(self, ctx, *, message):
        await ctx.send('*' + message + '*')

    @commands.command(name="cpp", description="Send all your messages in a C++ code block.", usage=" [message]")
    async def cpp(self, ctx, *, message):
        await ctx.send(f"""```cpp\n{message}```""")

    @commands.command(name="cs", description="Send all your messages in a C Sharp code block.", usage=" [message]")
    async def cs(self, ctx, *, message):
        await ctx.send(f"""```cs\n{message}```""")

    @commands.command(name="java", description="Send all your messages in a Java code block.", usage=" [message]")
    async def java(self, ctx, *, message):
        await ctx.send(f"""```java\n{message}```""")

    @commands.command(name="python", description="Send all your messages in a Python code block.", usage=" [message]")
    async def python(self, ctx, *, message):
        await ctx.send(f"""```py\n{message}```""")

    @commands.command(name="js", description="Send all your messages in a JavaScript code block.", usage=" [message]")
    async def js(self, ctx, *, message):
        await ctx.send(f"""```js\n{message}```""")

    @commands.command(name="lua", description="Send all your messages in a Lua code block.", usage=" [message]")
    async def lua(self, ctx, *, message):
        await ctx.send(f"""```lua\n{message}```""")

    @commands.command(name="php", description="Send all your messages in a PHP code block.", usage=" [message]")
    async def php(self, ctx, *, message):
        await ctx.send(f"""```php\n{message}```""")

    @commands.command(name="html", description="Send all your messages in a HTML code block.", usage=" [message]")
    async def html(self, ctx, *, message):
        await ctx.send(f"""```html\n{message}```""")

    @commands.command(name="css", description="Send all your messages in a CSS code block.", usage=" [message]")
    async def css(self, ctx, *, message):
        await ctx.send(f"""```css\n{message}```""")

    @commands.command(name="yaml", description="Send all your messages in a YAML code block.", usage=" [message]")
    async def yaml(self, ctx, *, message):
        await ctx.send(f"""```yaml\n{message}```""")

    @commands.command(name="json", description="Send all your messages in a JSON code block.", usage=" [message]")
    async def _json(self, ctx, *, message):
        await ctx.send(f"""```json\n{message}```""")


def setup(bot):
    bot.add_cog(Text(bot))
