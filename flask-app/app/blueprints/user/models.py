class User():
    def __init__(self, firstName, lastName, Supervisor, email, phoneNumber ):
        self.firstName = firstName
        self.lastName = lastName
        self.Supervisor = Supervisor
        self.email = email
        self.phoneNumber = phoneNumber



    def to_dict(self):
        return {
            "firstName": self.firstName,
            "lastName": self.lastName,
            "email": self.email,
            "phoneNumber": self.phoneNumber,
            "Supervisor": self.Supervisor
        }
        