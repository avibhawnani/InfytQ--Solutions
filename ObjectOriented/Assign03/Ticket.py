d = ["mumbai", "chennai", "pune", "kolkata"]


class Ticket:
    counter = 0

    def __init__(self, passenger_name, source, destination):
        self.__passenger_name = passenger_name
        self.__ticket_id = None
        self.__source = source
        self.__destination = destination

    def validate_source_destination(self):
        self.__source = self.__source.lower()
        self.__destination = self.__destination.lower()
        if self.__source == "delhi":
            if self.__destination in d:
                return True
            else:
                return False
        return False

    def generate_ticket(self):
        if self.validate_source_destination():
            Ticket.counter += 1
            self.__ticket_id = "D" + self.__destination[0].upper() + "{:02d}".format(Ticket.counter)
        else:
            self.__ticket_id = None

    def get_ticket_id(self):
        return self.__ticket_id

    def get_source(self):
        return self.__source

    def get_destination(self):
        return self.__destination

    def get_passenger_name(self):
        return self.__passenger_name
