from lyricsgenius import Genius

token = 'NoIEDg435uhButX--j32h5TN5tpFEGXQXjcxetfWWINhZqsCgsZLH9rFsiZL2J6J'
genius = Genius(token)
song = genius.search_song("Carrosel", "Da Weasel")
print(song.lyrics)
