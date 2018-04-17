import os, re
import numpy as np

class UserHistory:
    TRAIN_LEN = 5000
    BLOCK_LEN = 100
    
    def __init__(self, fname, commands):
        assert(re.match(r'User[0-9]{1,2}', fname))
        self.user = int(fname[4:])
        self.commands = commands

    def get_training_set(self):
        """ returns the training block sequence of commands """
        return self.commands[:UserHistory.TRAIN_LEN]    

    def get_nth_masq_block(self, n):
        """ returns the nth potentially-masquerader (not training) block """
        return self.commands[self.__blockwin(n):self.__blockwin(n + 1)]

    @staticmethod
    def __blockwin(k):
        """ 
        returns the starting index of the kth post-training block (0-indexed) 
        """
        return UserHistory.TRAIN_LEN + UserHistory.BLOCK_LEN * k
    
    def __repr__(self):
        return f"User: {self.user} | first command: {self.commands[0]}"
    
    def __lt__(self, other):
        return self.user <= other.user
    
def read_sequences(userfiles_dir):
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
    user_histories.sort()
    return user_histories

def read_indicator_matrix(infile):
    mat = np.loadtxt(infile)
    return mat

os.chdir("/home/mson/home/unixseq")
MASQ_DIR = "data/masquerade_users"
MASQ_IND_FPATH = "data/masquerade_summary.txt"
seqs = read_sequences(MASQ_DIR)
inds = read_indicator_matrix(MASQ_IND_FPATH)
