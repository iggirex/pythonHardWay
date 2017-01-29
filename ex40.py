class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for werds in self.lyrics:
            print werds

happy_bday = Song(["Happy birthday to you",
"I don't want to get sued", "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()


class Shopping(object):
    def __init__(self, myFood, catFood, laterFood):
        self.myFood = myFood,
        self.catFood = catFood,
        self.laterFood = laterFood
    def myShoppingList(self):
        for items in self.myFood:
            print "this is", items
    def kittyShoppingList(self):
        for items in self.catFood:
            print items
    def laterShopping(self):
        for items in self.laterFood:
            print items

myList = Shopping(["Fancy Feast", "cat nip"], ["tortillas", "vegan cheese"], ["pbJ", "OJ"])

print '-' * 10

myList.kittyShoppingList()
myList.myShoppingList()
myList.laterShopping()
