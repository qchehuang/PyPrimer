words= ["cat", 'dog', 'tiger']
for w in words[:]:
    print (w, len(w))
    if (len(w) > 3):
        words.insert(0,w)

print words
