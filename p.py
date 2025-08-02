print("Finding the binary represention of a number only.")
num = int((input("Enter a number: ")))
binary = bin(num)[2:]
print("Binary is: ", binary)

print("Finding the set number of binary")
# When you want to see the bit number
num = int((input("Enter a number: ")))
binary = bin(num)[2:]
print("Binary is: ", binary)

n = int(input("Which bit number do you want to see? (1 = first from left): "))
if 1 <= n <= len(binary):
    bit = binary[n - 1]
    print("That bit is: ", bit)
else:
    print("Ooops!")






print("Find the the set bit of the binary representation of 7 and 8 from the right: using the codes below.")
num = int((input("Enter a number: ")))
binary = bin(num)[2:]
print("Binary is: ", binary)

n = int(input("Which bit number do you want to see? (1 = first from right): "))
if 1 <= n <= len(binary):
    bit = binary[1 - n]
    print("That bit is: ", bit)
else:
    print("Ooops!")

# When you want to see the bit number
num = int((input("Enter a number: ")))
binary = bin(num)[2:]
print("Binary is: ", binary)

n = int(input("Which bit number do you want to see? (1 = first from right): "))
if 1 <= n <= len(binary):
    bit = binary[1 - n]
    print("That bit is: ", bit)
else:
    print("Ooops!")






def check_bit():
    print("Welcome to the bit checker game!")
    print("Enter a number and I will tell you whether it's 0-bit 0r 1- bit.\n")

    while True:
        bit = input("Enter a bit(0 or 1), or type 'exit' to quit:").strip()

        if bit.lower() == 'exit':
            print("Thanks for playing! Bye!")
            break
        elif bit == '0':
            print("You entered 0. That's a zero bit!\n")

        elif bit == '1':
            print("You entered 1. That's a one bit.\n")
        else:
            print("Oops! That's not a valid bit. Please enter only 0 or 1.\n")

check_bit( )