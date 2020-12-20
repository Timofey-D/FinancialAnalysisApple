PERIOD = 5


def printPeriod(nameReport, year):
    print("{:<85}".format(nameReport), end=": ")
    for i in range(PERIOD):
        print("{:>20}".format(year), end=" ")
        year -= 1
    print(end='\n')


def printList(nameReport, list):
    print("{:<85}".format(nameReport), end=": ")
    for i in range(len(list)):
        print("{:>20}".format(list[i]), end=" ")
    print(end='\n')