#Define a function named fortune(). Inside the function, print out a random fortune from the list of options below:

#Don't pursue happiness – create it.
#All things are difficult before they are easy.
#The early bird gets the worm, but the second mouse gets the cheese.
#Someone in your life needs a letter from you.
#Don't just think. Act!
#Your heart will skip a beat.
#The fortune you search for is in another cookie.
#Help! I'm being held prisoner in a Chinese bakery! rewrite the function without an if/elif/else.
import random
def fortune():
    fortunes = [
        "Don't pursue happiness – create it.",
        "All things are difficult before they are easy.",
        "The early bird gets the worm, but the second mouse gets the cheese.",
        "Someone in your life needs a letter from you.",
        "Don't just think. Act!",
        "Your heart will skip a beat.",
        "The fortune you search for is in another cookie.",
        "Help! I'm being held prisoner in a Chinese bakery!"
    ]
    print(random.choices(fortunes, k=3)[0])
fortune()