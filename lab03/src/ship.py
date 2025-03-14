class Ship:

    def __init__(self, destination, voyage_duration):
        self.destination = destination
        self.voyage_duration = voyage_duration

    def calculate_fuel(self):
        return 100 * self.voyage_duration
