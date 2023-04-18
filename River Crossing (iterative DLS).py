# Coded By Parsa Yousefi Nejad
# Version 4: Iterative_DLS_Search() replaced Recursive DLS_Search() and some minor changes were made

# Importing Necessary libraries
from os import system, name  # For Clear() method
from copy import copy        # To shallow copy of an object
from time import sleep       # For implementing pause mechanism in PathShow()

# Display: Shows one Record Graphically
def Display(Record):
    listOfChars = ["POLICE", "THIEF", "FATHER", "MOTHER",
                   "DAUGHTER_1", "DAUGHTER_2", "SON_1", "SON_2",]
    shore = ('\x1b[0;32;42m'+"⥯"+'\x1b[0m') * 10
    plainText = '\033[2m'+"❖"+'\x1b[0m'+" {} "+'\x1b[4;35;43m'+"|"+'\x1b[0m'+'\x1b[1;33;34m' + \
        "~~~~~~~~~~~~~~~~"+'\x1b[0m'+'\x1b[4;35;43m' + \
        "|" + '\x1b[0m'+" {} "+('\033[2m'+"❖"+'\x1b[0m')

    print(('\033[2m'+"✵"+'\x1b[0m') * 44)
    print(plainText.format(shore, shore))

    for i in range(0, 8):
        characterName = listOfChars[i] + \
            ('\x1b[1;32;42m'+"⥯"+'\x1b[0m') * (10 - len(listOfChars[i]))
        if Record[i] == 0:
            print(plainText.format(
                '\x1b[7;35;46m'+characterName+'\x1b[0m', shore))
        else:
            print(plainText.format(
                shore, '\x1b[7;35;46m'+characterName+'\x1b[0m'))
        if i == 3:
            if Record[8]:
                print('\033[2m'+"❖"+'\x1b[0m', shore, '\x1b[4;35;43m'+"|"+'\x1b[0m', '\x1b[1;33;34m'+"~~~~~~~~~~~" +
                      '\x1b[0m', '\x1b[1;34;41m'+"⛵️"+'\x1b[0m', '\x1b[4;35;43m'+"|"+'\x1b[0m', shore, '\033[2m'+"❖"+'\x1b[0m')
            else:
                print('\033[2m'+"❖"+'\x1b[0m', shore, '\x1b[4;35;43m'+"|"+'\x1b[0m', '\x1b[1;34;41m'+"⛵️"+'\x1b[0m',
                      '\x1b[1;33;34m'+"~~~~~~~~~~~"+'\x1b[0m', '\x1b[4;35;43m'+"|"+'\x1b[0m', shore, '\033[2m'+"❖"+'\x1b[0m')

    print(plainText.format(shore, shore))
    print(('\033[2m'+"✵"+'\x1b[0m') * 44)

# PathShow:  Shows Multiple States in order
def PathShow(List_States):
    if List_States == None:
        print("\x1B[41;2;35mThere is Nothing To Show\033[0m")
        exit(-1)
    counter = 1
    previousState = List_States[0]
    for state in List_States[1:]:
        if counter != 1:
            sleep(0.1)
        Clear()
        print(f"\033[3;46;35mChild State {counter}\033[0m")
        Display(state)
        TellMove(previousState, state)
        counter += 1
        previousState = state

# Clear:     Clears Terminal output
def Clear():
    if name == 'nt':
        system('cls')
    else:
        system('Clear')

# Assigning values to problem members
POLICE = 0; THIEF = 1; FATHER = 2; MOTHER = 3; DAUGHTER_1 = 4; DAUGHTER_2 = 5; SON_1 = 6; SON_2 = 7; BOAT_Direction = 8

# Checks whether a state is valid
def IsValid(state):
    return ((state[DAUGHTER_1] == state[MOTHER] or state[DAUGHTER_1] != state[FATHER]) and (
            state[DAUGHTER_2] == state[MOTHER] or state[DAUGHTER_2] != state[FATHER])) and ((

            state[SON_1] == state[FATHER] or state[SON_1] != state[MOTHER]) and (
            state[SON_2] == state[FATHER] or state[SON_2] != state[MOTHER])) and (

            state[POLICE] == state[THIEF] or (state[THIEF] != state[FATHER] and
            state[THIEF] != state[MOTHER] and state[THIEF] != state[DAUGHTER_1] and
            state[THIEF] != state[DAUGHTER_2] and state[THIEF] != state[SON_1] and
            state[THIEF] != state[SON_2]))

# checks if the state is the Goal
def IsGoal(state):
    return state == [1, 1, 1, 1, 1, 1, 1, 1, 1]

# it generates all states from a valid state and filters all invalid ones
def GenerateAllValidStates(state):

    if not IsValid(state):
        print('\n'+"\x1B[41;1;35mSorry I can\'t Generate States for an Invalid State\033[0m")
        exit(-1)

    validStates = []
    for currentCharacter in [POLICE, THIEF, FATHER, MOTHER, DAUGHTER_1, DAUGHTER_2, SON_1, SON_2]:
        for parent in [FATHER, MOTHER, POLICE]:
            if state[currentCharacter] == state[parent] == state[BOAT_Direction]:
                new_State = copy(state)

                if new_State[currentCharacter]:
                    new_State[currentCharacter] = new_State[parent] = new_State[BOAT_Direction] = 0
                else:
                    new_State[currentCharacter] = new_State[parent] = new_State[BOAT_Direction] = 1

                if IsValid(new_State) and new_State not in validStates:
                    validStates.append(new_State)

    return validStates

# Describes State Changes in Context
def TellMove(state, new_state):
    peopleList = ['POLICE', 'THIEF', 'FATHER', 'MOTHER',
                  'DAUGHTER_1', 'DAUGHTER_2', 'SON_1', 'SON_2', 'BOAT_Direction']

    diff = list()
    for item1, item2 in zip(state, new_state):
        item = item1 - item2
        diff.append(item)

    Direction = 'RIGHT' if diff[8] == -1 else 'LEFT'

    movedPeople = list()
    for i in range(8):
        if diff[i] == -1 or diff[i] == 1:
            movedPeople.append(i)
    if len(movedPeople) == 1:

        print("\n" + f"\033[4;43;35m{peopleList[movedPeople[0]]}\033[0m" +
              ' moved to the ' f"\033[3;44;30m{Direction}\033[0m")
    else:
        print("\n" + f"\033[4;43;35m{peopleList[movedPeople[0]]}\033[0m"' and ' +
              f"\033[4;43;35m{peopleList[movedPeople[1]]}\033[0m"+' moved to the ' f"\033[3;44;30m{Direction}\033[0m")

# Non Recursive Depth-Limited-Search with viewAllStatesFlag feature
def Iterative_DLS_Search(state, DEPTH_LIMIT, viewAllStatesFlag):

    if not IsValid(state):
        print(
            '\n'+"\x1B[41;1;35mSorry I cannot Find a Soution for an Invalid State\033[0m")
        exit(-1)

    #tuple of currentState, currentStateDepth
    unExpandedNodes = [(state, 0)]
    expandedNodesList = []

    while unExpandedNodes is not None:

        stateOfLastUnexpandedNode,depthOfLastUnexpandedNode= unExpandedNodes.pop()

        if IsGoal(stateOfLastUnexpandedNode):
            expandedNodesList.append((stateOfLastUnexpandedNode, depthOfLastUnexpandedNode))
            if viewAllStatesFlag:
                allCheckedStatesList = []
                for eachNode in expandedNodesList:
                    allCheckedStatesList.append(eachNode[0])
                return allCheckedStatesList
            else:
                trueAnswerStatesList = filterFinalTrueAnswerStates(expandedNodesList)
                return trueAnswerStatesList
            
        # checks wheter current depth Reached to the DEPTH_LIMIT
        if depthOfLastUnexpandedNode < DEPTH_LIMIT:

            expandedStatesList = []
            for i in expandedNodesList:
                expandedStatesList.append(i[0])
        
            if stateOfLastUnexpandedNode not in expandedStatesList:

                expandedNodesList.append((stateOfLastUnexpandedNode, depthOfLastUnexpandedNode))
                generatedChildrenNodesList = GenerateAllValidStates(stateOfLastUnexpandedNode)
                depthOfLastUnexpandedNode += 1
                depthOfChlidrenNodes = [depthOfLastUnexpandedNode]*(len(generatedChildrenNodesList))
                tupleOfChildrenAndDepthsList = tuple(zip(generatedChildrenNodesList, depthOfChlidrenNodes))
                unExpandedNodes.extend(tupleOfChildrenAndDepthsList)

def filterFinalTrueAnswerStates(finalNodes):
    lastDepth = (finalNodes[-1])[1]   
    finalNodes.reverse()
    filteredStates = []
    #node is tuple of currentState, currentStateDepth
    for node in finalNodes:
        if node[1] < lastDepth:
            filteredStates.append(node[0])  #appends state
            lastDepth = node[1]             #changes lastDepth value with currentStateDepth

    filteredStates.reverse()
    filteredStates.append((finalNodes[0])[0])
    return filteredStates

# main part of the Code, Calling Iterative_DLS_Search on begin state=[0..0]
# ////////////////MAIN//////////////////
viewAllStatesFlag = False

startState = [0]*9
finalStates = Iterative_DLS_Search(startState, 17, viewAllStatesFlag)
PathShow(finalStates)

# By Parsa Yousefi Nejad