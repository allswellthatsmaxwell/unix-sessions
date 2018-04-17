import os

class UserHistory:
    def __init__(self, user, commands):
        self.user = user
        self.commands = commands
    def __repr__(self):
        return f"User: {self.user} | first command: {self.commands[0]}"
        
def read_masquerade_sequences(userfiles_dir):
    """
    collects user names and command sequences. Assumes userfiles_dir has
    one file per user, and that each file has one line per command.
    Arguments: (repository root)/data/masquerade_users 
      as generated from running root/sh/get_masquerade_data.sh    
    returns: a list of UserHistory, with each user's info and 
      ordered command sequence.
    """
    user_histories = []
    for user_fname in os.listdir(userfiles_dir):
        with open(os.path.join(userfiles_dir, user_fname)) as f:
            commands = [line.strip() for line in f.readlines()]
        user_histories.append(UserHistory(user_fname, commands))
    return user_histories

MASQ_DIR = "data/masquerade_users"
masqs = read_masquerade_sequences(MASQ_DIR)
