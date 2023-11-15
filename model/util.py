from random import randint, shuffle, choice
# number_of_small_letters=4,
# number_of_capital_letters=2,
# number_of_digits=2,
# number_of_special_chars=2,
# allowed_special_chars="_+-!"
# (https://pl.wikipedia.org/wiki/ASCII)


def generate_id():
    allowed_special_chars = r"_+-!"
    number_of_small_letters = 4
    number_of_capital_letters = 2
    number_of_digits = 2
    number_of_special_chars = 2

    generated_id = []

    for i in range(number_of_small_letters):
        generated_id.append(chr(randint(97, 122)))
    for i in range(number_of_capital_letters):
        generated_id.append(chr(randint(65, 90)))
    for i in range(number_of_digits):
        generated_id.append(chr(randint(48, 57)))
    for i in range(number_of_special_chars):
        generated_id.append(choice(allowed_special_chars))

    shuffle(generated_id)
    return "".join(generated_id)
