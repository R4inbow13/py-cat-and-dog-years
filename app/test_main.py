from app.main import get_human_age


def test_should_return_zero_for_ages_below_15() -> None:
    assert get_human_age(5, 8) == [0, 0]


def test_should_return_1_for_ages_between_15_and_24() -> None:
    assert get_human_age(16, 23) == [1, 1]


def test_should_return_2_if_ages_between_24_and_28() -> None:
    assert get_human_age(25, 27) == [2, 2]


def test_should_return_3_and_2_if_ages_equal_28() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_21_and_17_if_ages_equal_100() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_if_ages_different_ages_of_cat_and_dog() -> None:
    assert get_human_age(75, 46) == [14, 6]
