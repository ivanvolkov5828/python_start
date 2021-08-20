from random import choice


def get_jokes(number, flag=False):
    """
       Creating a list of n jokes formed from three random words taken from three lists (one from each)

       :param number: Number of jokes
       :return: a list with n number of jokes
       """

    my_list = []

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    for i in range(number):
        noun = choice(nouns)
        adverb = choice(adverbs)
        adjective = choice(adjectives)
        joke = f"{noun} {adverb} {adjective}"
        my_list.append(joke)
        my_list_2 = []
        if flag:
            my_list_2 = joke.split()
            for noun in nouns:
                for el in my_list_2:
                    if noun == el:
                        nouns.remove(noun)

            for adverb in adverbs:
                for el in my_list_2:
                    if adverb == el:
                        adverbs.remove(adverb)

            for adjective in adjectives:
                for el in my_list_2:
                    if adjective == el:
                        adjectives.remove(adjective)
    return my_list


print(get_jokes(2, flag=True))
