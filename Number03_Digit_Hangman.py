# Editor: 박민지

print("3.Digital Hangman")
while True:
    round_setting = 5
    score = int(0)
    collector = ""
    check_repeat = []
    temp = []

    # Get Integer Pattern
    while True:
        try:
            final_ans = [int(x) for x in input("Enter set of 12 integer numbers(eg. 1 2 3 ... 12): ").split()]
            for i in range(len(final_ans)):
                final_ans[i] = str(final_ans[i])
            if len(final_ans) != 12:
                raise ValueError
            else:
                break
        except ValueError:
            print("Please input only set of integer number as same as the following pattern.")
            print("1 2 3 4 5 6 7 8 9 10 11 12")
            continue

    # In game
    while round_setting > 0:
        while True:
            try:
                val = int(input("\nGuess: "))
                val = str(val)
                break
            except ValueError:
                print("Please input only integer number.")
                continue
        # Find value in final ans and check repeat
        if val not in final_ans and val in check_repeat:
            print("Don't you remember. That number is not in the answer.")
        elif val not in final_ans and val not in check_repeat:
            print("That's wrong.")
            check_repeat.append(val)
        elif val in final_ans and val in check_repeat:
            print("You already answer that number.")
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
    print("\nFinal score: " + str(score))
    # Check input from user if they want to try again or not
    checkend = input("Wanna try again (Y for Yes/any character for No): ").upper()
    if checkend != "Y":
        print("Goodbye")
        break

