def get_comment(note):
    if note > 15:
        commentaire = 'bravoooooo !'
    elif note > 10:
        commentaire = 'peux mieux faire !'
    elif note > 5:
        commentaire = 'ATTENTION !'

commentaire = 'nullllll !'
get_comment(int(input("Donne ta note : ")))
print(commentaire)

