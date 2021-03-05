from backend.utils import *
import nltk

def tag_text(text, pos_tagger):
    sentences = nltk.sent_tokenize(text)
    sentences = [[x.upos for x in pos_tagger(s).iter_words()] for s in sentences]
    return sentences

def get_grammar_tuples(sentences):
    """sentences : output of tag_text"""
    return grammar_induction(sentences, n=2)


def get_grammar_cfg_string(grammar_tuples):
    return grammar2cfg(grammar_tuples)


def get_grammar_cfg(grammar_cfg_string):
    return nltk.CFG.fromstring(grammar_cfg_string)


def get_parser(grammar_cfg):
    grammar_lark = grammar_cfg_string_to_lark(grammar_cfg)
    parser = lark.Lark(grammar_lark, start='s', lexer="dynamic_complete")
    return parser

def parse(parser, sent):
    tree = parser.parse(' '.join(sent))
    return tree.pretty()
