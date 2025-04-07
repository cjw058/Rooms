from random import randint
class Room:
    def __init__(self, name):
        self.name = name
        self.exits = []
        self.exitLocations = []
        self.items = []
        self.itemDescriptions = []
        self.grabbables = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def exitLocations(self):
        return self._exitLocations

    @exitLocations.setter
    def exitLocations(self, value):
        self._exitLocations = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

def addExit(self, exits, room):
    self._exits.append(exit)
    self._exitlocations.append(room)

def addItem(self, item, desc):
        self._items.append(item)
        self._itemDescriptions.append(desc)

def addGrabbable(self, item):
    self._grabbables.append(item)

def delGrabbable(self, item):
    self._grabbables.remove(item)

def __str__(self):
    # first, the room name
    s = "You are in the {}.\n".format(self._name)

    # next, the items the room
    s += "You see: "
    for items in self._items:
        s += items + ", "
    s = "\n"

    # next, the exits from the room
    s += "Exits are: "
    for exits in self._exits:
        s += exits + ", "
    s += exit + " "
    return s

def death():
    print(" " * 17 + "u" * 7)
    print(" " * 13 + "u" * 2 + "$" * 11 + "u" * 2)
    print(" " * 10 + "u" * 2 + "$" * 17 + "u" * 2)
    print(" " * 9 + "u" + "$" * 21 + "u")
    print(" " * 8 + "u" + "$" * 23 + "u")
    print(" " * 7 + "u" + "$" * 25 + "u")
    print(" " * 7 + "u" + "$" * 25 + "u")
    print(" " * 7 + "u" + "$" * 6 + "\"" + " " * 3 + "\"" + "$" * 3 + "\"" + " " * 3 + "\"" + "$" * 6 + "u")
    print(" " * 7 + "\"" + "$" * 4 + "\"" + " " * 6 + "u$u" + " " * 7 + "$" * 4 + "\"")
    print(" " * 8 + "$" * 3 + "u" + " " * 7 + "u$u" + " " * 7 + "u" + "$" * 3)
    print(" " * 8 + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3)
    print(" " * 9 + "\"" + "$" * 4 + "u" * 2 + "$" * 3 + " " * 3 + "$" * 3 + "u" * 2 + "$" * 4 + "\"")
    print(" " * 10 + "\"" + "$" * 7 + "\"" + " " * 3 + "\"" + "$" * 7 + "\"")
    print(" " * 12 + "u" + "$" * 7 + "u" + "$" * 7 + "u")
    print(" " * 13 + "u$\"$\"$\"$\"$\"$\"$u")
    print(" " * 2 + "u" * 3 + " " * 8 + "$" * 2 + "u$ $ $ $ $u" + "$" * 2 + " " * 7 + "u" * 3)
    print(" u" + "$" * 4 + " " * 8 + "$")

def createRooms():
    global currentRoom
    r1 = Room("Room 1")
    r2 = Room("Room 2")
    r3 = Room("Room 3")
    r4 = Room("Room 4")
    r5 = Room("Room 5")
    r6 = Room("Room 6")
    r7 = Room("Room 7")
    # 3 new rooms, make them themed

    r1.addExits("east", r2)
    r1.addExits("south", r3)
    r1.addGrabbable("key")
    r1.addItem("chair", "It is made of wicker and noone is sitting on it.")
    r1.addItem("Table", "It is made of wood, and a golden key is on the table.")

    r2.addExits("west", r1)
    r2.addExits("south", r4)
    r2.addItems("rug", "It is nice and Indian. It needs to be cleaned.")
    r2.addItems("fireplace", "Full of ashes and cold.")


    r3.addExits("north", r1)
    r3.addExits("east", r4)
    r3.addGrabbables("book")
    r3.addItem("bookshelves", "Empty. Big surprise.")
    r3.addItem("desk", "A statue rests upon it. So is a book.")

    r4.addExits("north", r2)
    r4.addExits("west", r3)
    r4.addExits("south", None)
    r4.addGrabbable("6-pack")
    r4.addItems("brew_rig", "Gourd is brewing some sort of oatmeal"
                                "stout on the brew rig. A 6-pack is resting beside it.")
    currentRoom = r1

#Start the game!
inventory = []
while True:
    #situational awareness, see what you have
    status = "{}\nYou are carrying: {}\n".format(currentRoom, inventory)
    #if current room is None, player is dead.
    if (currentRoom == None):
        death()
        break


    print("========================================================")
    print(status)

    #if current room is None, player is dead, exit game
    action = input("What to do? ")
    action = action.lower
    #exits game if players inputs these words
    if (action == "quit" or action == 'exit' or action == "bye"):
        break
        #puts words in a list
    words = action.split()

    #the game only knows two words
    if (len(words) == 2):
        verb = words[0] #verb
        noun = words[1] #noun
        #verb is go
        if (verb == "go"):
            #set a default response
            response = "Invalid Exit"

            # check for valid exits
            for i in range(len(currentRoom.exits[i])):
                if (noun == currentRoom.exits[i]):
                ##change the current room to the one that is
                #specified by the exit
                    currentRoom = currentRoom.exitLocations[i]
                    response = "Room changed."
                    break
                # if verb is look
                elif (verb == "look"):
                    #default response
                    response = "I dont see that item"
                    #checks for valid items in a room
                    for i in range(len(currentRoom.items)):
                        if (noun == currentRoom.items[i]):
                            # set response to item description
                            response = currentRoom.itemDescriptions[i]
                            # no need to check any more items
                            break
                elif (verb == "take"):
                    # default response
                    response = "I dont see that item."
                    #check for valid grabbables
                    for grabbables in currentRoom.grabbables:
                        # a valid grabbable is found
                        if (noun == grabbables):
                            #add it to inventory
                            inventory.append(grabbables)

                            #remove it from the room
                            currentRoom.delGrabbable(grabbables)
                            # set the response (success)
                            response = "Item grabbed."

                            #no need to check anymore grabbables
                            break

            print("\n{}".format(response))