VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
PUNCTUATION = ",.!?"

def checkio(text):
    text = text.upper()
    for c in PUNCTUATION:
        text = text.replace( c, " " )
    for c in VOWELS:
        text = text.replace( c, "v" )
    for c in CONSONANTS:
        text = text.replace( c, "c" )

    words = text.split( " " )

    count = 0
    for word in words:
        if len( word ) > 1 and word.isalpha():
            if word.find( "cc" ) == -1 and word.find( "vv" ) == -1:
                count += 1

    return count
