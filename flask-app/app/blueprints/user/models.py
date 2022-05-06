class User():
    def __init__(self, firstName, lastName, Supervisor, email, phoneNumber ):
        self.firstName = firstName
        self.lastName = lastName
        self.Supervisor = Supervisor
        self.email = email
        self.phoneNumber = phoneNumber

    def to_dict(self):
        if self.email and not self.phoneNumber:
            return {
                "firstName": self.firstName,
                "lastName": self.lastName,
                "email": self.email,
                "Supervisor": self.Supervisor
            }
        if self.phoneNumber and not self.email:
            return {
                "firstName": self.firstName,
                "lastName": self.lastName,
                "phoneNumber": self.phoneNumber,
                "Supervisor": self.Supervisor
            }
        if self.phoneNumber and self.email:
            return {
                "firstName": self.firstName,
                "lastName": self.lastName,
                "email": self.email,
                "phoneNumber": self.phoneNumber,
                "Supervisor": self.Supervisor
            }
        else:
            return {
                "firstName": self.firstName,
                "lastName": self.lastName,
                "Supervisor": self.Supervisor
            }