# Editor: 박민지

def abbreviation(name):
    token = name.split()
    abb = ""
    for item in token:
        if item[0].isupper():
            abb += str(item[0])
    return abb

def alphabetically_sorted(set):
    sorted_set = sorted(set)
    return sorted_set


print("1.Sorting Acronyms")
name_collector = []
abb_collector = []

# Get amount of name
while True:
    try:
        name_amount = int(input("Enter amount of name: "))
        break
    except ValueError:
        print("Input integer number only.")
        continue

# Get name for name_amount round
for count in range(name_amount):
    while True:
        temp_name = str(input("Enter name number " + str(count + 1) + ": "))
        for char in temp_name:
            if char.isnumeric():
                print("Number is not allow.")
                break
        else:
            name_collector.append(temp_name)
            break

for word in name_collector:
    abb_collector.append(abbreviation(word))

sorted_list = alphabetically_sorted(abb_collector)

for word in sorted_list:
    print(str(word))
