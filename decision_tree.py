mainBranch, sleepBranch, awakeBranch = [],[],[]
petCharlie, getOutOfBed = [], [] #sleepBranch
treatCharlie, growCharlie = [],[] #PetCharlie
oujiaChoice, sitNStew = [], [] #treatCharlie

shirtOn, noClothes, leaveRoom = [],[], [] #awakeBranch

mainBranch.extend([
    "",
    ["Go back to sleep", sleepBranch],
    ["Get out of bed",awakeBranch],
])

##################################################

sleepBranch.extend([
    "You go back to sleep...\nBut suddenly you are awoken by your dog",
    ["Go back to sleep", ["Youzzzzzzzr dog explodes!"]],
    ["Pet Charlie, your dog", petCharlie],
    ["Get out of your wonderful bed, and into your miserable life", getOutOfBed],
])

petCharlie.extend([
    "You pet charlie! He seems content with this...",
    ["Give Charlie a treat", treatCharlie],
    ["Get out of bed", awakeBranch],
    ["Grow Charlie into a person", growCharlie],
])

treatCharlie.extend([
    "You give Charlie a treat! He licks your face...",
    ["Wipe it off", ["Your hand begins to melt... then your face"]],
    ["Get a oujia board", oujiaChoice],
    ["Just sit... and wait", sitNStew],
])

oujiaChoice.extend([
    "You give Charlie a treat! He licks your face...",
    ["Summon a ghost", ["The ghost snaps your neck"]],
    ["Invite charlie", growCharlie],
    ["Just sit... and wait", sitNStew],
    ["Demand god smite your ops", ["a ski mask decends froms the sky"]],
])


sitNStew.extend([
    "You sit and ponder life...",
    ["Stop thinking", ["Your head explodes from thinking too much"]],
    ["Just sit... and think", sitNStew],
])

getOutOfBed.extend([
    "You get out of bed, finally... Your dad walks in",
    ["Say Hi", ["He says hi back, and then you wake up bc you don't have a dad"]],
    ["Get back in bed", awakeBranch],
])

growCharlie.extend([
    "Charlie grows to the size and porption of a full human",
    ["Say Hi", ["You explode"]],
    ["Get back in bed", mainBranch],
])

##################################################

awakeBranch.extend([
    "You get out of bed",
    ["Explode",["Your head explodes"]],
    ["Put a shirt on",shirtOn],
    ["Walk around without clothes",noClothes],
])

shirtOn.extend([
    "you throw your shirt on",
    ["put another shirt on",shirtOn],
    ["take the shirt off",noClothes],
    ["say hi to your dog", petCharlie],
    ["explore the universe", sitNStew],
])

noClothes.extend([
    "you decide to walk around shirtless",
    ["Walk out of your room",leaveRoom],
    ["take the shirt off",noClothes],
    ["say hi to your dog", petCharlie],
    ["explore the universe", sitNStew],
])

leaveRoom.extend([
    "you walk out of your room",
    ["say hi to your dad",["you dont have a dad"]],
    ["go to school", ["explode"]],
    ["go get your oujia board", oujiaChoice],
])


def makeChoice(list):
    if not list[0] == "":
        print(" ")
        print(list[0])
    
    for i in range(len(list)-1):
            print(f"{i+1}. {list[i+1][0]}")
    response = int(input("What choice will you make? "))

    if response > (len(list)-1) or response < 1:
        print("Uh oh you did it wrong, twin 🥀")
    else:
        if len(list[response][1]) == 1:
            print(list[response][1][0])
        else:
            makeChoice(list[response][1])

def startRun():
    print("welcome to your life\nhope you have fun")
    makeChoice(mainBranch)

startRun()