fish_breeds = {}

class FishBreed():

    def __init__(self, size_min, size_max, bag, location, identifiers):
        self.size_min = size_min
        self.size_max = size_max
        self.bag = bag
        self.location = location
        self.identifiers = identifiers

fish_breeds["Bream"] = FishBreed(28, 38, 10, "rivers", "silvery bronze colour, single dorsal fin")

fish_breeds["King George Whitting"] = FishBreed(27, None, 20, "coastal waters", "long head and body, prown spots, silver colour, small head and mouth")

fish_breeds["Mullet"] = FishBreed(None, None, 40, "costal waters and sometimes freshwater", "ss")

print(fish_breeds["Bream"].size_max)