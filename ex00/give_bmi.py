def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """ """
    if len(height) != len(weight):
        raise ValueError("len of the 2 list are different")
    bmi = []
    i = 0
    for h in height:
        if not isinstance(h, (int, float)):
            raise TypeError("Value of height is not an int nor a float")
        carre = h * h
        w = weight[i]
        if not isinstance(w, (int, float)):
            raise TypeError("Value of weight is not an int nor a float")
        bmi.append(w / carre)
        i += 1
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """ check the limit and returns a list of \
bool for each elem of the bmi list """
    ret_lst = []
    for elem in bmi:
        if elem > limit:
            ret_lst.append(True)
        else:
            ret_lst.append(False)
    return ret_lst


def main():
    try:
        height = [2.71, 1.15]
        weight = [165.3, 38.4]
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except (Exception, TypeError, ValueError) as e:
        print(f"Error : {e}")


if __name__ == "__main__":
    main()
