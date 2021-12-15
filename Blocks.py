blocks = int(input("Enter the number of blocks: "))

height = 0

inlayer = 1

while inlayer <= blocks:

    height += 1 #h=1 #h=2
    blocks -= inlayer #b=5 #b=3
    inlayer += 1 #l=2 #l=3

print("The height of the pyramid: ", height)


