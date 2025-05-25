import random
names = ["samyukth","anirudh", "sahishnu", "tj", "kedar", "dhara", "vaishnavi"]
#names = ["samyukth","anirudh", "sahishnu", "tj"]
connectors = ["is", "is not"]
adjectives = ["cool", "awesome", "funny", "amazing", "naughty", "brilliant", "sleepy"]
name = names[random.randint(0, 3)]
connector = connectors[random.randint(0, 1)]
adjective = adjectives[random.randint(0, 6)]
print(name.capitalize(), connector, adjective,".")
