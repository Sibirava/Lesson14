
def check_season(month):

    if isinstance(month, bool) or not isinstance(month, int) \
            or not (1 <= month <= 12):
       return -1

    season = "spring"

    if 2 >= month >= 1 or month == 12:
        season = "winter"
    elif 8 >= month >= 6:
        season = "summer"
    elif 11 >= month >= 9:
        season = "autumn"
    return season


if __name__ == "__main__":
    assert check_season("10") == -1
    assert check_season(7.4) == -1
    assert check_season(True) == -1
    assert check_season(None) == -1
    assert check_season([1, 2, 3]) == -1
    assert check_season(20) == -1
    assert check_season(-20) == -1
    assert check_season(1) == "winter"
    assert check_season(2) == "winter"
    assert check_season(12) == "winter"
    assert check_season(3) == "spring"
    assert check_season(4) == "spring"
    assert check_season(5) == "spring"
    assert check_season(6) == "summer"
    assert check_season(7) == "summer"
    assert check_season(8) == "summer"
    assert check_season(9) == "autumn"
    assert check_season(10) == "autumn"
    assert check_season(11) == "autumn"

