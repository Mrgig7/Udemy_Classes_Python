# t = "a", "b", "c"
# print(t)
#
# t = ("a", "b", "c")
# print(t)

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "NightFLight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lighting", "Metallica", 1984

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])

# # metallica[0] = "Master of Puppets" # Tuples are immutable that is it cany be changed
# metallica2 = list(metallica)
# print(metallica2)
#
# metallica2[0] = "Master of Puppets"
# print(metallica2)

title, artist, year = metallica
print(title)
print(artist)
print(year)

table = ("Coffee table", 200, 100, 75, 34.50)
print((table[1] * table[2]))

name, length, width, height, price = table
print(length * width)
