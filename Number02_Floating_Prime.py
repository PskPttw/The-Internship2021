# Editor: 박민지

def prime(val, round_counter, divisor = 2):
    round_val = round(val)
    # Ceiling
    if round_val - val > 0:
        if round_counter < 3:
            if round_val - 1 <= 2:
                return True if (round_val - 1 == 2) else prime(val * 10, round_counter + 1, divisor)
            if (round_val - 1) % divisor == 0:
                return prime(val * 10, round_counter + 1, divisor)
            if divisor * divisor > (round_val - 1):
                return True
            return prime(val, round_counter, divisor + 1)
    # Floor
    elif round_val - val < 0:
        if round_counter < 3:
            if round_val <= 2:
                return True if (round_val == 2) else prime(val * 10, round_counter + 1, divisor)
            if round_val % divisor == 0:
                return prime(val * 10, round_counter + 1, divisor)
            if divisor * divisor > round_val:
                return True
            return prime(val, round_counter, divisor + 1)

    elif round_val - val == 0:
        if round_val <= 2:
            return True if (round_val == 2) else False
        if round_val % divisor == 0:
            return False
        if divisor * divisor > round_val:
            return True
        return prime(val, round_counter, divisor + 1)


while True:
    print("2.Floating Prime")
    number = input("Enter Number: ")
    str_number = str(number)
    flt_temp_number = float(number)
    try:
        if flt_temp_number == 0.0:
            break
        flt_number = float(number)
        if (flt_number * 10) % 10 != 0:
            flt_number *= 10
            if prime(flt_number, 0):
                print("TRUE")
            else:
                print("FALSE")

    except ValueError:
        continue
    size = len(str_number) - 1

