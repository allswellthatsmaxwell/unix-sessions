class Session:
    def __init__(self, commands):
        self.commands = commands

class Command:
    def __init__(self, command, options, args):
        self.command = command
        self.options = options
        self.args = args
        
def parse_command_sequences(infile):
    with open(infile) as f:
        lines = [line.strip() for line in f.readlines()]
    sessions = []
    for line in lines:
        if line == "**SOF**":
            commands = []
        elif line == "**EOF**":
            sessions.append(Session(commands))