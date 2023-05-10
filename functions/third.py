def get_vovel_symbol_count(text):
    vovels = ["a", "e", "i","o", "u"]

    # sum = 0
    # for vovel in vovels:
    #     if text.count(vovel):
    #         sum += text.count(vovel)

    #another way to do it

    vovel_count = sum([ text.count(vovel) for vovel in vovels if vovel in text])

    return vovel_count

print(get_vovel_symbol_count("abcf dfgdfsg dfgssdfg dfgsdf dfgsdf uuuuu"))






