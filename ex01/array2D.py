def slice_me(family: list, start: int, end: int) -> list:
    if not isinstance(family, list):
        raise TypeError("family needs to be a list")
    if not all(isinstance(row, list) for row in family):
        raise TypeError("family must be a 2D list")
    row_len = len(family[0])
    if not all(len(row) == row_len for row in family):
        raise AssertionError("All rows must be of the same size")
    print(f"My shape is ({len(family)}, {row_len})")
    sliced = family[start:end]
    print(f"My shape is ({len(sliced)}, {row_len})")
    return sliced


def main():
    try:
        slice_me()
    except Exception as e:
        print(f"error : {e}")


if __name__ == "__main__":
    main()
