from main import calculate_word_score, choose_letters_from_bag


def test_calculate_word_score():
    assert calculate_word_score("GUARDIAN") == 10


def test_calculate_word_score2():
    assert calculate_word_score("E") == 1


def test_calculate_word_score3():
    assert calculate_word_score("QE") == 11


def test_calculate_word_score4():
    assert calculate_word_score("FDE") == 7


def test_choose_letters_from_bag():
    assert choose_letters_from_bag({"EAIUOPP": 1}) == "EAIUOPP"


def test_choose_letters_from_bag2():
    assert choose_letters_from_bag({"EAIUOKK": 1}) == "No"