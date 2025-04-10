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

    def addExits(self, exit, room):
        self.exits.append(exit)
        self._exitLocations.append(room)

    def addItem(self, item, desc):
            self._items.append(item)
            self.itemDescriptions.append(desc)

    def addGrabbable(self, item):
        self._grabbables.append(item)

    def delGrabbable(self, item):
        self._grabbables.remove(item)

    def __str__(self):
    # first, the room name
        s = "You are in the {}.\n".format(self.name)

    # next, the items in the room
        s += "You see: "
        for item in self.items:
            s += item + " "
        s += "\n"

    # next, the exits from the room
        s += "Exits are: "
        for exit in self.exits:
            s += exit + " "
        s += "\n"
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
    r8 = Room("Room 8")
    # 4 new rooms, make them themed, except start.

    r1.addExits("west", r7)
    r1.addExits("east", r2)
    r1.addExits("south", r3)
    r1.addItem("chair", "It is made of wicker and noone is sitting on it.")
    r1.addItem("table", "A key with one written on it is on the table.")
    r1.addGrabbable("key1")

    r2.addExits("east", r5)
    r2.addExits("west", r1)
    r2.addExits("south", r4)
    r2.addItem("rug", "It is nice and Indian. It needs to be cleaned.")
    r2.addItem("fireplace", "Full of ashes and cold.")
    r2.addGrabbable("map")

    r3.addExits("west", r8)
    r3.addExits("north", r1)
    r3.addExits("east", r4)
    r3.addGrabbable("book")
    r3.addItem("bookshelves", "Full of books. The whole room is covered in.")
    r3.addItem("desk", "A statue rests upon it. So is a book.")

    r4.addExits("east", r6)
    r4.addExits("north", r2)
    r4.addExits("west", r3)
    r4.addExits("south", None)
    r4.addItem("bedroom", "Kinda small. There's a stool to reach high things here.")
    r4.addGrabbable("stool")

    r5.addExits("west", r2)
    r5.addExits("south", r6)
    r5.addExits("hole", None)
    r5.addItem("hole", "Doesn't look like anything good.")
    r5.addItem("table", "It is made of wood. It is empty.")
    r5.addItem("lamp.", "It is a red and yellow lamp. There's a lighter beside it.")

    r6.addExits("north", r5)
    r6.addExits("west", r4)
    r6.addExits("vent", r1)
    r6.addItem("toys", "Looks like a play-set for a child.")
    r6.addItem("desk", "It looks like something is inside. A gun?")
    r6.addGrabbable("gun")

    r7.addExits("east", r1)
    r7.addExits("south", r8)
    r7.addItem("man", "He's standing in front of the door. He won't let you pass.")
    r7.addItem("locked_door.", "It has a lock, and it's chained. Gonna need a key and bolt cutters.")

    r8.addExits("north", r7)
    r8.addExits("east", r3)
    r8.addItem("closet", "A bunch of tools. There's some bolt cutters hanging on a rack. You'll need "
                         " a stool to get them")



    currentRoom = r1
createRooms()
#Start the game!
inventory = []
grabbable_matches = {
    "key1": r7,
    "bolt cutters": r7,
    "gun": r7,
    "stool": r7
}
while True:
    #situational awareness, see what you have
    status = "{}\nYou are carrying: {}\n".format(currentRoom, inventory)
    #if current room is None, player is dead.
    if (currentRoom == None):
        death()
        break


    print("========================================================")
    print(status)
    print("You can use the following commands: go (location), look (item, inventory), take (Grabbable), use (item).")


    #if current room is None, player is dead, exit game
    action = input("What to do? ")
    action = action.lower()
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
    for i in range(len(currentRoom.exits)):
        if (noun == currentRoom.exits[i]):
             ##change the current room to the one that is
            #specified by the exit
                currentRoom = currentRoom.exitLocations[i]
                response = "Room changed."
                break
                #if verb is look
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
                    if noun == "bolt cutters" and "stool" not in inventory:
                        response = "You need a stool to get them."

                #check for valid grabbables
                    for grabbable in currentRoom.grabbables:
                    # a valid grabbable is found
                        if (noun == grabbable):
                        #add it to inventory
                            inventory.append(grabbable)

                        #remove it from the room
                            currentRoom.delGrabbable(grabbable)
                        # set the response (success)
                            response = "Item grabbed."

                            #no need to check anymore grabbables
                            break
        elif (verb == "use"):
            if noun not in inventory:
               print("You don't have that.")
            target = noun
            used_items =[]
            for grabbable, room in grabbable_matches.items():
                if target == grabbable:
                    currentRoom = room
                    response = "You used the {}.".format(target)
                    inventory.remove(target)
                    if target == "gun":
                        response += "The man is dead."
                        used_items.append(target)
                    elif target == "bolt cutters" and "stool" in inventory:
                        response += "The door is no longer chained."
                        used_items.append(target)
                    elif target == "stool":
                        response += "You can now reach the bolt cutters."
                        used_items.append(target)






        elif (action == "open inventory"): # adds a way to check inventory again. For whatever reason.
            response = "You have: "
            for item in inventory:
                response += item + " "




    print("\n{}".format(response))