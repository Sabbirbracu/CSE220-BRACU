def hocBuilder(height):
    if height <= 0:
        return 0
    elif height == 1:
        return 8
    else:
        return 8 + 5 * (height - 1) + hocBuilder(height - 1)

# Test the function
height = int(input("Enter the height of the house of cards: "))
cards_needed = hocBuilder(height)
print(f"The number of cards required for a house of height {height} is {cards_needed}")
