def calc_dragon_head(age):
    #FOOOL PROOF
    if not isinstance(age, int) or age <= 0:    #является ли обьект, на который указывает ссылочная переменная классом int
        return -1

    head = 3
    if age <= 100:
        head = head + age * 3
    elif age <= 200:
        head = head + 100 * 3 + (age - 100) * 2
    else:
        head = head + 100 * 3 + 100 * 2 + (age - 200) * 1
    return head



if __name__ == "__main__":
    assert calc_dragon_head(0) == -1
    assert calc_dragon_head(-100) == -1
    assert calc_dragon_head(1) == 6
    assert calc_dragon_head(50) == 153
    assert calc_dragon_head(150) == 403
    assert calc_dragon_head(300) == 603
    assert calc_dragon_head(100) == 303
    assert calc_dragon_head(101) == 305
    assert calc_dragon_head(200) == 503
    assert calc_dragon_head(201) == 504
    assert calc_dragon_head("200") == -1
    assert calc_dragon_head(None) == -1
