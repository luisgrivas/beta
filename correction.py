import pickle

with open('data/names.pickle', 'rb') as f:
	NAMES = pickle.load(f)

with open('data/lastnames.pickle', 'rb') as f:
    LASTNAMES = pickle.load(f)

DICT = NAMES

def change_dict():
    "Select which dictionary you want to use"
    global DICT
    if DICT == NAMES:
        DICT = LASTNAMES
        print('Dictionary changed to lastnames')
    else:
        DICT = NAMES
        print('Dictionary changed to name')


def P(name, N=sum(DICT.values())):
    "Probability of `name`."
    if name in DICT.keys():
        return DICT[name] / N
    else:
        return 0


def correction(name):
    "Most probable correction for name."
    return max(candidates(name.upper()), key=P)


def candidates(name):
    "Generate possible spelling corrections for name."
    return (known([name]) or known(edits1(name)) or known(edits2(name)) or [name])


def known(names):
    "The subset of `names` that appear in the dictionary of DICT."
    return set(w for w in names if w in DICT)

def edits1(name):
    "All edits that are one edit away from `name`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(name[:i], name[i:])    for i in range(len(name) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(name):
    "All edits that are two edits away from `name`."
    return (e2 for e1 in edits1(name) for e2 in edits1(e1))
