# Editor: 박민지

def prime(val, round_counter, divisor=2):
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


print("2.Floating Prime")
while True:
    number = input("")
    str_number = str(number)
    try:
        flt_temp_number = float(number)
        int_number = int(round(flt_temp_number))
        if flt_temp_number > 10.0 or flt_temp_number < 1.0:
            continue
        if flt_temp_number == 0.0:
            break
        flt_number = float(number)

        if int_number - flt_temp_number == 0:
            if (flt_number * 10) % 10 != 0:
                flt_number *= 10
                if prime(flt_number, 0):
                    print("TRUE")
                else:
                    print("FALSE")
            else:
                if prime(flt_number, 0):
                    print("TRUE")
                else:
                    print("FALSE")
        else:
            if (flt_number * 10) % 10 != 0:
                flt_number *= 10
                if prime(flt_number, 0):
                    print("TRUE")
                else:
                    print("FALSE")
            else:
                if prime(flt_number, 0):
                    print("TRUE")
                else:
                    print("FALSE")
    except ValueError:
        continue
    size = len(str_number) - 1

