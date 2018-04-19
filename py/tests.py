def test_build_transitions_matrix():
    seq = ['a', 'a', 'b', 'a', 'c', 'a', 'c']
    transmat, names = build_transition_matrix(seq)
    return transmat, names