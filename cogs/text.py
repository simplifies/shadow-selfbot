import discord
import asyncio
import requests
import urllib
import main
import base64
from datetime import datetime
from discord.ext import commands
from main import PREFIX, bot, EMBEDCOLOUR, PUREEMBEDCOLOUR


class Text(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="text", description="Main text command.", usage="")
    async def text(self, ctx):
        try:
            embed = discord.Embed(title="📝 Text Commands",
                                  description=f"""
`{PREFIX}`**base64 [message]** » Encrypt your messages using Base64
`{PREFIX}`**base64decode [message]** » Decrypt a Base64 message.
`{PREFIX}`**suggest [suggestion]** » Make a suggestion.
`{PREFIX}`**cembed [title] (description) (colour) (showtime yes/no)** » Create a custom embedded message.
`{PREFIX}`**embed [title]** » Create an embedded message.
`{PREFIX}`**secret [message]** » Send all your messages in a secret block.
`{PREFIX}`**secretletters [message]** » Put all lettes from your message into separate secret blocks.
`{PREFIX}`**purgehack** » Purge messages without permission.
`{PREFIX}`**uppercase [message]** » Send your message in uppercase.
`{PREFIX}`**lowercase [message]** » Send your message in lowercase.
`{PREFIX}`**aesthetic [message]** » Send your messages s p a c e d out.
`{PREFIX}`**animate [message]** » Animate your messages.
`{PREFIX}`**chatbypass [message]** » Send your messages in a different font.
`{PREFIX}`**regional [message]** » Convert your messages into emojis.
`{PREFIX}`**ascii [message]** » Send a message in ascii art.
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
            embed.set_thumbnail(url=main.EMBEDIMAGE)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send(f"""**📝 Text Commands**

`{PREFIX}`**base64 [message]** » Encrypt your messages using Base64
`{PREFIX}`**base64decode [message]** » Decrypt a Base64 message.
`{PREFIX}`**suggest [suggestion]** » Make a suggestion.
`{PREFIX}`**cembed [title] (description) (colour) (showtime yes/no)** » Create a custom embedded message.
`{PREFIX}`**embed [title]** » Create an embedded message.
`{PREFIX}`**secret [message]** » Send all your messages in a secret block.
`{PREFIX}`**secretletters [message]** » Put all lettes from your message into separate secret blocks.
`{PREFIX}`**purgehack** » Purge messages without permission.
`{PREFIX}`**uppercase [message]** » Send your message in uppercase.
`{PREFIX}`**lowercase [message]** » Send your message in lowercase.
`{PREFIX}`**aesthetic [message]** » Send your messages s p a c e d out.
`{PREFIX}`**animate [message]** » Animate your messages.
`{PREFIX}`**chatbypass [message]** » Send your messages in a different font.
`{PREFIX}`**regional [message]** » Convert your messages into emojis.
`{PREFIX}`**ascii [message]** » Send a message in ascii art.
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
                                """)

    @commands.command(name="regional", description="Convert your messages into emojis.", usage=" [message]")
    async def regional(self, ctx, *, message):
        text = message.lower()

        regional_indicators = {
        'a': '<:regional_indicator_a:803940414524620800>',
        'b': '<:regional_indicator_b:803940414524620800>',
        'c': '<:regional_indicator_c:803940414524620800>',
        'd': '<:regional_indicator_d:803940414524620800>',
        'e': '<:regional_indicator_e:803940414524620800>',
        'f': '<:regional_indicator_f:803940414524620800>',
        'g': '<:regional_indicator_g:803940414524620800>',
        'h': '<:regional_indicator_h:803940414524620800>',
        'i': '<:regional_indicator_i:803940414524620800>',
        'j': '<:regional_indicator_j:803940414524620800>',
        'k': '<:regional_indicator_k:803940414524620800>',
        'l': '<:regional_indicator_l:803940414524620800>',
        'm': '<:regional_indicator_m:803940414524620800>',
        'n': '<:regional_indicator_n:803940414524620800>',
        'o': '<:regional_indicator_o:803940414524620800>',
        'p': '<:regional_indicator_p:803940414524620800>',
        'q': '<:regional_indicator_q:803940414524620800>',
        'r': '<:regional_indicator_r:803940414524620800>',
        's': '<:regional_indicator_s:803940414524620800>',
        't': '<:regional_indicator_t:803940414524620800>',
        'u': '<:regional_indicator_u:803940414524620800>',
        'v': '<:regional_indicator_v:803940414524620800>',
        'w': '<:regional_indicator_w:803940414524620800>',
        'x': '<:regional_indicator_x:803940414524620800>',
        'y': '<:regional_indicator_y:803940414524620800>',
        'z': '<:regional_indicator_z:803940414524620800>'
        }

        output = ""
        text = list(text)
        for letter in text:
            if letter in regional_indicators:
                output = output + regional_indicators[letter] + " "
            else:
                output = output + letter
        await ctx.send(output)

    @commands.command(name="base64", description="Encrypt your messages using Base64", usage=" [message]")
    async def base64(self, ctx, *, message):
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')

        await ctx.send(base64_message)

    @commands.command(name="base64decode", description="Decrypt a Base64 message.", usage=" [message]")
    async def base64decode(self, ctx, *, message):
        base64_bytes = message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        decoded = message_bytes.decode('ascii')

        await ctx.send(decoded)

    @commands.command(name="suggest", description="Make a suggestion.", usage=" [suggestion]")
    async def suggest(self, ctx, *, suggestion):
        try:
            embed = discord.Embed(title="💭 Suggestion", description=suggestion, color=EMBEDCOLOUR)
            embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
            embed.set_thumbnail(url=main.EMBEDIMAGE)
            embed.timestamp = datetime.now()
            msg = await ctx.send(embed=embed)
        except discord.HTTPException:
            msg = await ctx.send(f"**💭 Suggestion**\n{suggestion}")

        await msg.add_reaction('\U0001F44D')
        await msg.add_reaction('\U0001F44E')

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

    @commands.command(name="purgehack", description="Purge messages without permission.", usage="")
    async def purgehack(self, ctx):
        purgeMsg = "** **\n" * 75
        await ctx.send(purgeMsg)

    @commands.command(name="uppercase", description="Send your message in uppercase.", usage=" [message]")
    async def uppercase(self, ctx, *, message):
        string = message.upper()
        await ctx.send(string)

    @commands.command(name="lowercase", description="Send your message in lowercase.", usage=" [message]")
    async def lowercase(ctx, *, message):
        string = message.lower()
        await ctx.send(string)

    @commands.command(name="aesthetic", description="Send your messages s p a c e d out.", usage=" [message]")
    async def aesthetic(self, ctx, *, message):
        msg = ""
        for letter in main.split(message):
            msg += " " + letter +  " "
        await ctx.send(msg)

    @commands.command(name="animate", description="Animate your messages.", usage="animate [message]")
    async def animate(self, ctx, *, message):
        output = ""
        text = list(message)
        msg = await ctx.send(text[0])
        for letter in text:
            output = output + letter + ""
            await msg.edit(content=output)
            await asyncio.sleep(1)

    @commands.command(name="chatbypass", description="Send your messages in a different font.", usage="chatbypass [message]")
    async def chatbypass(self, ctx, *, message):
        text = message.lower()

        letters = {
        'a': '𝚊',
        'b': '𝚋',
        'c': '𝚌',
        'd': '𝚍',
        'e': '𝚎',
        'f': '𝚏',
        'g': '𝚐',
        'h': '𝚑',
        'i': '𝚒',
        'j': '𝚓',
        'k': '𝚔',
        'l': '𝚕',
        'm': '𝚖',
        'n': '𝚗',
        'o': '𝚘',
        'p': '𝚙',
        'q': '𝚚',
        'r': '𝚛',
        's': '𝚜',
        't': '𝚝',
        'u': '𝚞',
        'v': '𝚟',
        'w': '𝚠',
        'x': '𝚡',
        'y': '𝚢',
        'z': '𝚣'
        }

        output = ""
        text = list(text)
        for letter in text:
            if letter in letters:
                output = output + letters[letter] + ""
            else:
                output = output + letter
        await ctx.send(output)

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

    @commands.command(name="cembed", description="Create a custom embedded message.", usage=" [title] (description) (colour) (showtime yes/no)")
    async def cembed(self, ctx, title, description="", colour=PUREEMBEDCOLOUR, showtimecode="yes"):
        colour = int(colour.replace("#", "0x"), 0)
        try:
            cembed = discord.Embed(title=title, description=description, color=colour)

            if showtimecode.lower() == "yes":
                cembed.timestamp = datetime.now()
            elif showtimecode.lower() == "no":
                pass
            else:
                pass

            await ctx.send(embed=cembed)
        except discord.HTTPException:
            pass

    @commands.command(name="embed", description="Create an embedded message.", usage=" [title]")
    async def embed(self, ctx, title):
        colour = EMBEDCOLOUR

        try:
            embed = discord.Embed(title=title, color=colour)
            embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
            embed.set_thumbnail(url=main.EMBEDIMAGE)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        except discord.HTTPException:
            pass

    @commands.command(name="ascii", description="Send a message in ascii art.", usage=" [message]")
    async def ascii(self, ctx, *, message):
        art = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(message)}+&font=standard').text
        await ctx.send(f"```{art}```")

def setup(bot):
    bot.add_cog(Text(bot))
