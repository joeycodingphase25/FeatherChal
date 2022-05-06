
# Creating models to have parsed data fufilled by model methods, Instead of routes

# supervisors model will hold the list of supervisor objects
class Supervisors():
    def __init__(self, sups): #kwargs will be the json file, list of object
        self.listing = []
        for i in range(len(sups)): # each dictionary in the list of supervisors REQUEST.json()
            # TYPE ERROR UNRESOLVED
            first = sups[i]['firstName']
            last = sups[i]['lastName']
            jury = sups[i]['jurisdiction']
            x = Supervisor(first=first, last=last, jury=jury)
            self.listing.append(x)

    # sort the objects supervisor per requirements
    def sorter(self):
        pass

# will place to_dict method on supervisor to return to REACT
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
    
    def __repr__(self):
        return f"<{self.jury}> - <{self.lastName}>, <{self.firstName}>"
    
    def __str__(self):
        return f"this supervisor is {self.firstName, self.lastName}"