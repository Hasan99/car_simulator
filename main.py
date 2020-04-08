class Car:
    RIGHT = 1
    LEFT = -1
    REVERSE_DIRECTION = -6
    FORWARD = 1
    REVERSE = 0

    def __init__(self):
        self.speed = 0
        self.gear = 1
        self.direction = 0
        self.broken = False
        self.simulation = []
        self.simulation_loaded = False

    def accelerate(self):
        print("Accelerating . . .")
        if not self.broken:
            if self.gear == self.REVERSE:
                if self.speed <= -1:
                    self.speed -= 5
                    if self.speed < -10:
                        self.speed = -10
                elif self.speed >= 0:
                    self.speed -= 5
                    if self.speed > -1:
                        self.speed = -1

            else:
                if self.speed <= 75:
                    self.speed += 5
                else:
                    self.speed = 80
                self.change_gear(self.FORWARD)

            self.display_stats()

    def brake(self):
        if not self.broken:
            if self.gear == self.REVERSE:
                if -10 <= self.speed <= -1:
                    self.speed += 5
                else:
                    self.speed = -5

            else:
                self.speed -= 5
                self.change_gear(self.FORWARD)
            self.display_stats()

    def turn_steering_wheel(self, direction_change):
        if not self.broken:
            if self.gear == self.REVERSE:
                self.direction = direction_change
            else:
                self.direction = direction_change
            self.display_stats()

    def change_gear(self, selected_gear=FORWARD):
        if not self.broken:
            if selected_gear == self.FORWARD:
                if 0 <= self.speed <= 10:
                    current_gear = self.gear
                    if current_gear != 1:
                        if current_gear > 1:
                            while current_gear != 1:
                                print("Changing down . . .")
                                current_gear -= 1
                            self.gear = 1
                            print(f"Current gear = {self.gear}")
                        else:
                            print("Changing up . . .")
                            self.gear = 1
                            print(f"Current gear = {self.gear}")

                elif 5 <= self.speed <= 25:
                    current_gear = self.gear
                    if current_gear != 2:
                        if current_gear > 2:
                            while current_gear != 2:
                                print("Changing down . . .")
                                current_gear -= 1
                            self.gear = 2
                            print(f"Current gear = {self.gear}")
                        else:
                            while current_gear != 2:
                                print("Changing up . . .")
                                current_gear += 1
                            self.gear = 2
                            print(f"Current gear = {self.gear}")

                elif 20 <= self.speed <= 40:
                    current_gear = self.gear
                    if current_gear != 3:
                        if current_gear > 3:
                            while current_gear != 3:
                                print("Changing down . . .")
                                current_gear -= 1
                            self.gear = 3
                            print(f"Current gear = {self.gear}")
                        else:
                            while current_gear != 3:
                                print("Changing up . . .")
                                current_gear += 1
                            self.gear = 3
                            print(f"Current gear = {self.gear}")

                elif 40 <= self.speed <= 60:
                    current_gear = self.gear
                    if current_gear != 4:
                        if current_gear > 4:
                            while current_gear != 4:
                                print("Changing down . . .")
                                current_gear -= 1
                            self.gear = 4
                            print(f"Current gear = {self.gear}")
                        else:
                            while current_gear != 4:
                                print("Changing up . . .")
                                current_gear += 1
                            self.gear = 4
                            print(f"Current gear = {self.gear}")

                elif 45 <= self.speed <= 80:
                    current_gear = self.gear
                    if current_gear != 5:
                        while current_gear != 5:
                            print("Changing up . . .")
                            current_gear += 1
                        self.gear = 5
                        print(f"Current gear = {self.gear}")

            elif selected_gear == self.REVERSE:
                if -10 <= self.speed <= -1:
                    current_gear = self.gear
                    if current_gear != 0:
                        while current_gear != 0:
                            print("Changing down . . .")
                            current_gear -= 1
                        self.gear = 0
                        print(f"Current gear = {self.gear}")

    def display_stats(self):
        print(f"Speed = {self.speed}, Gear = {self.gear}, Direction = {self.direction}")

    def load_simulation(self, filename):
        with open(filename) as file:
            data = file.read()
            commands = data.split("\n")

            self.simulation_loaded = True
            self.simulation = commands

            print("Loading simulation . . .")

    def run_simulation(self):
        if self.simulation_loaded:

            for command in self.simulation:
                if command == "FORWARD":
                    self.change_gear(self.FORWARD)
                elif command == "ACCELERATE":
                    self.accelerate()
                elif command == "LEFT":
                    self.turn_steering_wheel(self.LEFT)
                elif command == "RIGHT":
                    self.turn_steering_wheel(self.RIGHT)
                elif command == "BRAKE":
                    self.brake()
                elif command == "REVERSE":
                    self.change_gear(self.REVERSE)
                else:
                    print(f"Invalid Command, '{command}'")
        else:
            print("Simulation is not loaded!")


if __name__ == '__main__':
    my_car = Car()
    my_car.load_simulation("simulation.txt")
    my_car.run_simulation()
