class Item:
    def __init__(self, location, priority):
        self.location = location
        self.priority = priority
        self.id = id(self)


    def move_location(self, newLocation):
        knewLocation = self.location
        self.location = newLocation
        print(f"Location {knewLocation} Changed to {self.location}")

    def update_priority(self, newPriority):

class OrderList:
    def __init__(self, items):
        self.items = [Item]

    def add(self, item):
        self.items.append(item)

    def delete(self, item):
        print(f"The Item: {item} is Deleted")
        self.items.remove(item)

    def read(self):
        for item in self.items:
            print(f"{item.location}")

    def update(self, ):


