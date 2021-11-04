from commands.base_command  import BaseCommand
from utils                  import get_emoji
from random                 import randint
from discord_interactive import Page, Help

# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command

class Help(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "Help menu."
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params' 
        # argument in the handle() method
        # If no params are expected, leave this list empty or set it to None
        params = []
        super().__init__(description, params)

    # Override the handle() method
    # It will be called every time the command is received
    async def handle(self, params, message, client):
        # 'params' is a list that contains the parameters that the command 
        # expects to receive, t is guaranteed to have AT LEAST as many
        # parameters as specified in __init__
        # 'message' is the discord.py Message object for the command to handle
        # 'client' is the bot Client object

        root = Page('Welcome !\n')
        page_1 = Page('This is page 1')
        page_2 = Page('This is page 2')

        page_1.link(page_2, description='Click this icon to access page 2', reaction='💩')
        root.link(page_1, description='Click this icon to access page 1')

        # Set the root page as the root of other page (so user can come back with a specific reaction)
        root.root_of([page_1, page_2])

        # Create the Help object
        
        h = Help(client, root)


        # And display the help !
        await h.display(message.author)
