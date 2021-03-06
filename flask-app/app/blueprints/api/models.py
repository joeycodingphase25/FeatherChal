
# Creating models to have parsed data fufilled by model methods, Instead of routes
## Note that should there be a PK,FK relationship, the Supervisor model can be changed to flaskDB model and backref to the user model

# supervisors model will hold the list of supervisor objects, can be scaled by adding more to the model
class Supervisors():
    def __init__(self, sups):
        self.listing = []
        for i in range(len(sups)): # each dictionary in the list of supervisors REQUEST.json()
            first = sups[i]['firstName']
            last = sups[i]['lastName']
            jury = sups[i]['jurisdiction']
            x = Supervisor(first=first, last=last, jury=jury)
            self.listing.append(x)

    # sort the objects supervisor per requirements -- Time complexity O(n) + 0(n) --
    def sorter(self):    
        # sort first by jury
        self.listing.sort(key=lambda x: x.jury)
        # then sort by last name
        for i in range(len(self.listing) - 1):
            if self.listing[i].jury == self.listing[i+1].jury:
                if self.listing[i].lastName > self.listing[i+1].lastName:
                    self.listing[i], self.listing[i+1] = self.listing[i+1], self.listing[i]
                    # then Sort By first name
                if self.listing[i].lastName == self.listing[i+1].lastName:
                    if self.listing[i].firstName > self.listing[i+1].firstName:
                        self.listing[i], self.listing[i+1] = self.listing[i+1], self.listing[i]

# will place to_dict method on supervisor to return to REACT
# can be migrated to a database and connected to user via PK-FK relationship with flaskDB

class Supervisor():
    def __init__(self, first, last, jury):
        self.firstName = first
        self.lastName = last
        self.jury = jury

    def to_dict(self):
        return {
            'firstName': self.firstName,
            'lastName': self.lastName,
            'jurisdiction':self.jury
        }
    # REQUIRED FORMAT per instructions
    def required(self):
        return f"<{self.jury}> - <{self.lastName}>, <{self.firstName}>"
    
    def __repr__(self):
        return f"<{self.jury}> - <{self.lastName}>, <{self.firstName}>"
    
    def __str__(self):
        return f"this supervisor is {self.firstName, self.lastName}"