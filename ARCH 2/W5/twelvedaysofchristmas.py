

verses = [["first", "and a Partridge in a Pear Tree."],
          ["second", "two Turtle Doves, "],
          ["third", "three French Hens, "],
          ["fourth", "four Calling Birds, "],
          ["fifth", "five Gold Rings, "],
          ["sixth", "six Geese-a-Laying, "],
          ["seventh", "seven Swans-a-Swimming, "],
          ["eighth", "eight Maids-a-Milking, "],
          ["ninth", "nine Ladies Dancing, "],
          ["tenth", "ten Lords-a-Leaping, "],
          ["eleventh", "eleven Pipers Piping, "],
          ["twelfth", "twelve Drummers Drumming, "]]

def next_verse(vers_number: int):
    opener = f'on the {verses[vers_number][0]} day of Christmas, my true love gave to me '
    verse = "".join(str(verses[i][1]) for i in range(vers_number, -1, -1))
    return opener + (verse.replace("and ", "") if vers_number == 0 else verse)

    #continue a loop where in an f string the day is given of Christmas
    #and the song repeats with the corresponding gift item and joins them


def recite(start_verse, end_verse):
    return "\n".join(next_verse(verse_number)
                     for verse_number in range(start_verse, end_verse + 1))


print(recite(0, 11))
