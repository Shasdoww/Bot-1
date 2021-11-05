from commands.base_command import BaseCommand

class Kick(BaseCommand):
  def __init__(self):
    description = "Kicks a specific user"
    params = ["user", "reason"]
    super().__init__(description, params)
  
  async def handle(self, params, message, client):
    msg = "todo"
    await client.send_message(message.channel, msg)
