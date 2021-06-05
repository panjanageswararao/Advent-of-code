with open("input6.txt") as infile:

    total = 0
    groups = infile.read().split("\n\n")

    yeses = [len(set(answers)) for answers in groups]

    print(sum(yeses))

with open("input6.txt") as infile:

    total = 0
    groups = infile.read().split("\n\n")
    for group in groups:
        group = group.split()
        yeses = set(group[0])
        for answer in group[1:]:
            yeses = yeses.intersection(set(answer))

        total += len(yeses)

    print(total)
