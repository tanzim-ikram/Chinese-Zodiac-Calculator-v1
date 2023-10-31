# Chinese Zodiac Calculator-v1

def chinese_zodiac(year):
    remainder = year % 12

    for sign in zodiac:
        return zodiac[remainder]


zodiac = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat"]

birth_year = int(input("Enter your birth year to know your Chinese Zodiac Sign: "))
symbol = chinese_zodiac(birth_year).upper()

print(f"Your Chinese Zodiac Sign is '{symbol}'")
