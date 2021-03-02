import random

import stanza

from backend.utils import *

random.seed(0)
pos_tag = stanza.Pipeline(lang='fr', processors='tokenize,mwt,pos', dir='../backend/')

sent_tags = read_data('../resources/pos_tag.txt', custom=True)
sent_raw = read_data('../resources/raw_text.txt', raw=True)
sent_tags = zip(sent_raw, sent_tags)
sent_tags = [x for x in sent_tags if len(x[1]) < 9]
random.shuffle(sent_tags)
sent_tags, sent_tags_test = sent_tags[:1500], sent_tags[1500:1500 + 150]
sent_raw, sent_tags = zip(*sent_tags)
sent_raw, sent_tags = list(sent_raw), list(sent_tags)

sent_raw_test, sent_tags_test = zip(*sent_tags_test)
sent_raw_test, sent_tags_test = list(sent_raw_test), list(sent_tags_test)

test = ["Je suis Hichem."]
# test = [[str(x) for x in y] for y in test]
rules = grammar_induction(sent_tags, n=2)
print(len(rules))
cfg = grammar2cfg(rules)
with open('grammar', 'w') as f:
    f.write(cfg)
print(evaluation(cfg, test, pos_tag))
