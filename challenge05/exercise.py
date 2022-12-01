text_file = open(r"/Users/daniel.chancir/Desktop/Autoestudio/Codember/challenge05/josephus.txt")
josephus_victims = text_file.read()[1:-1].split(',')
josephus_victims = [element.replace('\n  ', '').replace('\n', '').replace('"', '') for element in josephus_victims]
indexes = list(range(0, len(josephus_victims)))
def josephus(ls, skip):
    skip -= 1 # pop automatically skips the dead guy
    idx = skip
    while len(ls) > 1:
        print(ls.pop(idx)) # kill prisoner at idx
        idx = (idx + skip) % len(ls)
    return ls[0]

print(josephus(indexes, 2), josephus_victims[josephus(indexes, 1)])
