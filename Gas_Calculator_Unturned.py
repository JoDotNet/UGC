"""
Unturned Gas Calculator

Updates:
    16.04.2022 | Version 1.0 - release
    16.04.2022 | Version 1.1 - Fixed str to int issue

"""

gasPrice = input("Current Gas Price: ")

tankPercent = input("Tank Level: ")


gasPrice_converted = float(gasPrice)
tankPercent_converted = int(tankPercent)


gasPercentToFill = 100 - tankPercent_converted

print("")
print("")

print("Total Price:", gasPercentToFill * gasPrice_converted)

print("")

a = input('Press "ENTER" to continue')