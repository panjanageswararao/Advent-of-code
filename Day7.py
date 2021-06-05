def check_in_bag(color, rules):
    if key_color in rules[color]:
        return True

    return any(check_in_bag(name, rules) for name in rules[color].keys())


with open("input7.txt") as infile:

    rules = {}
    for instruction in infile.readlines():
        instruction = instruction.strip()[:-1]
        words = instruction.split()
        bag_color = " ".join(words[:2])

        contains = instruction[instruction.find("contain") + 8 :]
        rule = {}
        if "no other" in contains:
            rules[bag_color] = {}
        else:
            for con in contains.split(","):
                con = con.strip()
                bags = con.split()
                rule[" ".join(bags[1:3])] = int(bags[0])
            rules[bag_color] = rule

    valid = 0
    for name in rules.keys():
        if check_in_bag(name, rules):

            valid += 1

    print(valid)


with open("input7.txt") as infile:

    rules = {}
    for instruction in infile.readlines():
        instruction = instruction.strip()[:-1]
        words = instruction.split()
        bag_color = " ".join(words[:2])

        contains = instruction[instruction.find("contain") + 8 :]
        rule = {}
        if "no other" in contains:
            rules[bag_color] = {}
        else:
            for con in contains.split(","):
                con = con.strip()
                bags = con.split()
                rule[" ".join(bags[1:3])] = int(bags[0])
            rules[bag_color] = rule

    tot_shiny_gold = number_in_bag(key_color, rules) - 1

    print(tot_shiny_gold)
