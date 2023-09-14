class Item:
    def __init__(self, id, location, priority):
        self.id = id
        self.location = location
        self.priority = priority

    def move_location(self, newLocation):
        knewLocation = self.location
        self.location = newLocation
        print(f"Location {knewLocation} Changed to {self.location}")

    def update_priority(self, newPriority):
        print("Hello")



class OrderList:
    def __init__(self, items):
        self.items = items

    def add(self, item):
        self.items.append(item)

    def delete(self, item):
        print(f"The Item: {item} is Deleted")
        self.items.remove(item)

    def read(self):
        for item in self.items:
            print(f"{item.location}")


