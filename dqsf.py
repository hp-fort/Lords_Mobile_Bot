def roundDown(n):
    return int("{:.0f}".format(n))

roundedValue = roundDown(145/56)
print("The rounded value of {} is: {}".format(2.5, roundedValue))