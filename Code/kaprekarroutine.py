def arr_des(number):
    digits = sorted(str(number), reverse=True)
    return int("".join(digits).zfill(4))


def arr_asc(number):
    digits = sorted(str(number), reverse=False)
    return int("".join(digits).zfill(4))


def cal_func(number):
    if(number == 1111 or number == 0000):
        raise ValueError("Value invalid")
    if (len(set(str(number))) < 2):
        raise ValueError("Value invalid")

    while number != 6174:
        descending = arr_des(number)
        ascending = arr_asc(number)
        result = descending - ascending
        if (result != 6174):
            print(result, end=", ")
            number = result
        else:
            print(result)
            number = result
    return number

if __name__ == "cal_func":
    val = input(
        "Enter a four-digit number with at least two different digits (excluding 1111, 0000): "
    )   
    try:
        val_int = int(val)
        if (
            len(set(val)) > 1
            and val != "0000"
            and val != "1111"
            and len(val) == 4
        ):
            print(val_int, end=", ")
            cal_func(val_int)
        else:
            print(
                "Invalid input."
            )
    except ValueError as e:
        print("Invalid input: ", e)
