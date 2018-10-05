switcher = {
    1: "Hey, introduce yourself to the nearest person to you!",
    2: "Text someone that they're great",
    3: "Yeet",
}
def switch_demo(argument):
    return switcher.get(argument, "You're doing great!")

def numberOfChallenges():
    return len(switcher.keys())