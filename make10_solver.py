def formula_str_2_value(formula_str):
    result = None
    size_str = len(formula_str)
    if formula_str[0] == "+":
        result = int(formula_str[1])
        for c_id in range(2, size_str, 2):
            result = result + int(formula_str[c_id:c_id+2])
    else:
        result = (-1) * int(formula_str[1])
        for c_id in range(2, size_str, 2):
            result = result + int(formula_str[c_id:c_id+2])
    return result


def make10(abcd):
# if __name__ == "__main__":
    # abcd = input()
    n = len(abcd)

    ret_can_make10 = False
    ret_formula_str = "Nothing"

    # bit-searching
    # 0:="-", 1:="+"
    for bits in range(2**n):
        specified_digits = "0" + str(n) + "b"
        bits_str = format(bits, specified_digits)

        curr_formula_str = ""
        for c_id, bit in enumerate(bits_str):
            ope = None
            if bit == "1":
                ope = "+"
            else:
                ope = "-"

            curr_formula_str = curr_formula_str + ope + abcd[c_id]

        if formula_str_2_value(curr_formula_str) == 10:
            print(curr_formula_str + "=10")
            ret_formula_str = curr_formula_str + "=10"
            ret_can_make10 = True
            break

    return ret_can_make10, ret_formula_str
