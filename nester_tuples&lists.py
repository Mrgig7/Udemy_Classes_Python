albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975),
    ("Bad Company", "Bad Company", 1974),
    ("Night Flight", "Budgie", 1981,),
    ("More Mayhem", "Emilda May", 2011,),
    ("Ride the Lighting", "Metallica", 1984,),
]

print(len(albums))

# for album in albums:
#     print("Album: {}, Artist: {}, Year: {}"
#           .format(album[0], album[1], album[2]))

for name, artist, year in albums:
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))

print()

for album in albums:
    name, artist, year = album
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))