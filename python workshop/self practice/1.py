#!/bin/python3

import math
import os
import random
import re
import sys

n = int(input("Enter positive number: "))
if n % 2 != 0:
    print("Weird")
elif 2 <=n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")