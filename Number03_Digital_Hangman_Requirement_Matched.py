# Editor: 박민지

print("3.Digital Hangman")
round_setting = 5
score = int(0)
collector = ""
check_repeat = []
temp = []

# Get Integer Pattern
while True:
    try:
        final_ans = [int(x) for x in input("").split()]
        if len(final_ans) != 12:
            raise ValueError
        for i in range(len(final_ans)):
            final_ans[i] = str(final_ans[i])
            print("-", end = " ")
        break
    except ValueError:
        continue
# In game
while round_setting > 0:
    while True:
        try:
            val = int(input("\n"))
            val = str(val)
            break
        except ValueError:
            continue

    # Find value in final ans and check repeat
    if val not in final_ans and val not in check_repeat:
        check_repeat.append(val)
    elif val in final_ans and val not in check_repeat:
        temp.append(val)
        check_repeat.append(val)
        for i in range(len(final_ans)):
            if val == final_ans[i]:
                score += 1
    # Print result for each round
    for temp_value in final_ans:
        if temp_value in temp:
            print(temp_value, end = " ")
        else:
            print("-", end = " ")
    # Print wrong answer from every round in each round
    for val_rep in check_repeat:
        if val_rep not in final_ans:
            print(val_rep, end = " ")
    # Decrease play round
    round_setting -= 1
# Print final score
print("\n" + str(score))


