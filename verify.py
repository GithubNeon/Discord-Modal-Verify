@bot.slash_command(name="verify", description="discord modal verify")
async def verify(ctx, interaction : nextcord.Interaction):
    modal=verify_modal()
    await interaction.response.send_modal(modal)

class verify_modal(nextcord.ui.Modal):
    def __init__(self):
        super().__init__("코드를 입력해주세요")  # Modal title

        string  = "Q W E R T Y U I O P A S D F G H J K L Z X C V B N M"
        integer = "1 2 3 4 5 6 7 8 9"

        maxcode = random.randrange(6, 11)

        self.code = ""
        for i in range(1, maxcode):
            if random.randint(0, 1)==1:
                t=random.choice(string.split(" "))
            else:
                t=random.choice(integer.split(" "))
            self.code += t

        self.input=nextcord.ui.TextInput(
            label=f"코드 : {self.code}",
            style=TextInputStyle.short,
            placeholder=self.code,
            min_length=len(self.code),
            max_length=len(self.code)
        )
        self.add_item(self.input)

    async def callback(self, interaction : nextcord.Interaction):
        if str(self.code)==self.input.value:
            role=nextcord.utils.get(interaction.guild.roles, name="역할이름")
            response="인증 성공!\nbot made by. ㅂㅇㅊ#2978"
            await interaction.user.add_roles(role)
        elif str(self.code) != self.input.value:
            response="인증 실패!\nbot made by. ㅂㅇㅊ#2978"
        await interaction.response.send_message(response)
