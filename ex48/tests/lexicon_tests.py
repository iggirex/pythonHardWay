from nose.tools import *
from ex48.lexObj import LexObj

def test_directions():
    lexicon = LexObj()

    assert_equal(lexicon.scan("north"), [("direction", "north")])
    result = lexicon.scan("north south east")
    assert_equal(result, [("direction", "north"),
                            ("direction", "south"),
                            ("direction", "east")])

def test_verbs():
    localLex = LexObj()

    assert_equal(localLex.scan("go"), [("verb", "go")])
    result = localLex.scan("go kill eat")
    assert_equal(result, [("verb", "go"),
                            ("verb", "kill"),
                            ("verb", "eat")])

def test_stops():
    lexicon = LexObj()

    assert_equal(lexicon.scan("the"), [("stop", "the")])
    result = lexicon.scan("the in of")
    assert_equal(result, [("stop", "the"),
                            ("stop", "in"),
                            ("stop", "of")])

def test_nouns():
    lexicon = LexObj()
    assert_equal(lexicon.scan("bear"), [("noun", "bear")])
    result = lexicon.scan("bear princess")
    assert_equal(result, [("noun", "bear"),
                            ("noun", "princess")])

def test_numbers():
    lexicon = LexObj()
    assert_equal(lexicon.scan("1234"), [("number", 1234)])
    result = lexicon.scan("3 91234")
    assert_equal(result, [("number", 3),
                            ("number", 91234)])

def test_errors():
    lexicon = LexObj()
    assert_equal(lexicon.scan("ASDFFASDF"), [("error", "ASDFFASDF")])
    result = lexicon.scan("bear IAS princess")
    assert_equal(result, [("noun", "bear"),
                            ("error", "IAS"),
                            ("noun", "princess")])
