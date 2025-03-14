class Ship:

    def __init__(self, destination, voyage_duration):
        self.destination = destination
        self.voyage_duration = voyage_duration
        self.crew = []

    def calculate_fuel(self):
        return 100 * self.voyage_duration

    def add_crew_member(self, param):
        if param == "":
            raise ValueError("Crew member name cannot be empty")

        self.crew.append(param)
