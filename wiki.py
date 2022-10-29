import wikipedia

wikipedia.set_lang("ru")


def search_wiki(word):

    try:
        w = wikipedia.search(word)
        if w:
            w1 = wikipedia.summary(word)
            w2 = wikipedia.page(word).url
            return w1, "\nLink: " + w2
        return "Request its not found", ""
    except:
        return "None", ""



