import urllib

htmlSource = urllib.urlopen("http://www.wikipedia.org").read(200000)
for chunk in htmlSource.lower().split('href=')[1:]:
    indexes = [i for i in [chunk.find('"',1),chunk.find('>'),chunk.find(' ')] if i>-1]
    print chunk[:min(indexes)]
