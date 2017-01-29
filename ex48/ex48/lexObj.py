class LexObj(object):
    def scan(self, sentence):
        wordList = sentence.split()
        result = []
        for word in wordList:
            if word.isdigit():
                result.append(("number", int(word)))
            elif(word == "north" or word == "south" or word == "east"):
                result.append(("direction", word))
            elif(word == "bear" or word == "princess"):
                result.append(("noun", word))
            elif(word == "go" or word == "eat" or word == "kill"):
                result.append(("verb", word))
            elif(word == "stop" or word == "in" or word == "of" or word == "the"):
                result.append(("stop", word))
            else:
                result.append(("error", word))
        return result
