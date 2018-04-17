
class UserHistory:
    def __init__(self, user, commands):
        self.user = user
        self.commands = commands

def parse_masquerade(infile):
    """
    collects user names and command sequences. Assumes infile is formatted as follows:
    the first line begins with "User";
    each line following the first line is a single command;
    the next user's sequence begins with a line that begins with "User";
    and so on.
    Arguments: MasqueradeDat (uncompressed)
        from http://www.schonlau.net/intrusion.html
    returns: a list of UserHistory, with each user's info and 
        ordered command sequence.
    """
    with open(infile) as f:
        lines = [line.strip() for line in f.readlines()]
    user_histories = []
    user = lines[0]
    commands = []
    for line in lines[1:]:        
        if line.startswith("User"):
            user_histories.append(UserHistory(user, commands))
            user = line
            commands = []
        else:
            commands.append(line)
    return user_histories

MASQ_FILE = "/home/mson/home/unixseq/data/MasqueradeDat"
masqs = parse_masquerade(MASQ_FILE)
