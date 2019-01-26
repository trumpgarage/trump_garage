

def load_file(fp):
    f = open(fp, "r")
    return f.read()

def build_input(nextwords, text):
    words = text.split()
    words = ["START"] + words + ["END"]

    for i in range(len(words)):
        curr = words[i]
        if curr != "END":
            nxt = words[i+1]
            nextwords = update_dict(nextwords, curr, nxt)

    return nextwords


def update_dict(nextwords, curr, nxt):

    if curr in nextwords:
        if nxt in nextwords[curr]:
            nextwords[curr][nxt] += 1
        else:
            nextwords[curr][nxt] = 1
    else:
        nextwords[curr] = {nxt:1}

    return nextwords






if __name__ == '__main__':

    text = load_file('dont_stop_believin.txt')
    print(text)
    print('\n\n')
    nextwords = build_input({}, text)
    print(nextwords)
