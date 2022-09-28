import math, random


userInput = ""
vectorCollection = []


def headingCorrection(heading : str, direction: float):
    heading = heading.lower()
    headingCompass = {
        "n":0,
        "e":90,
        "s":180,
        "w":270
    }

    xheading = heading

    if direction > 90:
        return [False, False, False]
    if direction > 45: 
        xheading = xheading[::-1]
        direction -= 45


    if abs(headingCompass[xheading[0]] - headingCompass[xheading[1]]) == 180:
        return [False, False, False]

    if xheading[1] == "n" or xheading[1] == "s":
        # opposite side is the x axis 
        return [1, direction, xheading]
    else:
        # opposite side is the y axis 
        return [-1, direction, xheading]



while userInput != "x":
    userInput = input(f"\n\n\t{random.randint(1,99)}[N{random.randint(1,44)}E]\n\tExample\n\nType 'x' to move on\nPlease print the vector:\t")
    try:
        firstBracket = userInput.find("[")
        endBracket = userInput.find("]")

        mag = float(userInput[:firstBracket])
        # create check for length of heading letters.
        headingLetters = userInput[firstBracket + 1: firstBracket + 2] + userInput[endBracket - 1:endBracket]
        heading, direction, xheaderLetters = headingCorrection(headingLetters, float(userInput[firstBracket + 2: endBracket - 1]))
        if not heading:
            int("no")

        collector = (mag, heading, direction, xheaderLetters)
        vectorCollection.append(collector)

        print("Form accepted")

    except (ValueError):
        if userInput !="x":
            print("invalid form")


class vectors:
    def init(self) -> None:
        self.DEGTORAD = math.pi/180

    def Opposite(self, theta : math.degrees, H : math.radians):
        # calculates the opposite side 
        return H * math.sin(theta * self.DEGTORAD)

    def Adjacent(self, theta : math.degrees, H : math.radians):
        # calculates the adjacent side
        return H * math.cos(theta * self.DEGTORAD)

vd = vectors()


print(vectorCollection)
xComponents = ()
yComponents = ()
x = 0
y = 0
for vector in vectorCollection:
    if vector[1] == 1:
        pass
    else: 
        pass




