
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())

    pattern = r"@gmail\.com$"
    regex = re.compile(pattern)
    firstname = []

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        if regex.search(emailID):
            firstname.append(firstName)

    firstname.sort()
    for name in firstname:
        print(name)
