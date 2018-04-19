import numpy as np
import os, re
import seqlearn, hmmlearn

class UserHistory:
    TRAIN_LEN = 5000
    BLOCK_LEN = 100
    
    def __init__(self, fname, commands):
        assert(re.match(r'User[0-9]{1,2}', fname))
        self.user = int(fname[4:])
        self.commands = commands

    def set_contaminated_block_inds(self, contam_array):
        """
        sets for each block whether it is contaminated by a masquerader.
        contam_array: a 100 x 0 array
        """
        assert(contam_array.shape == (UserHistory.BLOCK_LEN,))
        self.contams = [{1:True, 0:False}[x] for x in contam_array]

    def get_training_set(self):
        """ returns the training block sequence of commands """
        return self.commands[:UserHistory.TRAIN_LEN]    

    def get_nth_block(self, n):
        """ returns the nth potentially-masquerader (not training) block """
        return self.commands[self.__blockwin(n):self.__blockwin(n + 1)]

    def nth_contaminated(self, n):
        """ returns whether the nth block is contaminated by a masquerader."""
        return self.contams[n]
    
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
    
def read_histories(userfiles_dir):
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

def read_and_setup_data(seqs_dir, inds_fpath):
    """     
    Arguments: 
    seqs_dir: a directory of user files; see read_histories docstring.
    inds_fpath: the path to the block contamination matrix file. From Schonlau:
    "This file contains 100 rows and 50 columns. Each column corresponds 
    to one of the 50 users. Each row corresponds to a set of 100 commands, 
    starting with command 5001 and ending with command 15000. 
    The entries in the files are 0 or 1. 0 means that the corresponding 
    100 commands are not contaminated by a masquerader. 
    1 means they are contaminated."
    Returns: a list of UserHistory objects, one per file in seqs_dir
    """
    histories = read_histories(seqs_dir)
    inds = np.loadtxt(inds_fpath)
    for i, column in enumerate(inds.T):
        histories[i].set_contaminated_block_inds(column)
    return histories

def divide_rows_by_row_sums(mat):
    return (mat.T / mat.sum(axis=1)).T

def build_transition_matrix(seq):
    """ 
    Get the transitions matrix (in the Markov context) 
    for the command sequence seq. The (i, j)th element is the observed probability
    that word i was followed by word j. Also returns names in order corresponding
    to row and column indices in the matrix.
    Arguments: seq: a list
    Returns: a square matrix and the names (row and column names are the same)
    of that matrix
    """
    words = list(set(seq))
    words.sort()
    words_idx = {}
    for i, word in enumerate(words):
        words_idx[word] = i
    transitions_mat = np.zeros((len(words), len(words)))
    for v, w in zip(seq[:-1], seq[1:]):
        ## Each time word v is followed by word w, increment M[v, w].
        transitions_mat[words_idx[v], words_idx[w]] += 1
    transitions_mat = divide_rows_by_row_sums(transitions_mat)                                             
    return transitions_mat, words
    

os.chdir("/home/mson/home/unixseq")
MASQ_DIR = "data/masquerade_users"
MASQ_INDS_FPATH = "data/masquerade_summary.txt"

histories = read_and_setup_data(MASQ_DIR, MASQ_INDS_FPATH)
transition_mats = [build_transition_matrix(history.get_training_set())
                   for history in histories]
