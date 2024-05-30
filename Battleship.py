import random

class Ship:
    def __init__(self, size, position, orientation):
        self.size = size
        self.position = position
        self.orientation = orientation
        self.hits = 0

    def is_sunk(self):
        return self.hits == self.size

class Board:
    def __init__(self, size=6):
        self.size = size
        self.player_board = [[" " for _ in range(size)] for _ in range(size)]
        self.computer_board = [[" " for _ in range(size)] for _ in range(size)]
        self.player_ships = []
        self.computer_ships = []

    def place_ship(self, ship, board):
        x, y = ship.position
        if ship.orientation == "horizontal":
            for i in range(ship.size):
                board[x][y + i] = "X"
        else:
            for i in range(ship.size):
                board[x + i][y] = "X"

    def place_ships(self):
        self.player_ships = [Ship(3, (0, 0), "horizontal"),
                            Ship(2, (3, 2), "vertical"),
                            Ship(1, (5, 5), "horizontal")]
        for ship in self.player_ships:
            self.place_ship(ship, self.player_board)

        self.computer_ships = [Ship(3, (random.randint(0, 5), random.randint(0, 3)), "horizontal"),
                              Ship(2, (random.randint(0, 4), random.randint(0, 4)), "vertical"),
                              Ship(1, (random.randint(0, 5), random.randint(0, 5)), "horizontal")]
        for ship in self.computer_ships:
            self.place_ship(ship, self.computer_board)

    def display_boards(self):
        print("Ваш ход:")
        for row in self.player_board:
            print(" ".join(row))
        print("\nComputer's board:")
        for row in self.computer_board:
            print(" ".join(row))

    def player_shoot(self):
        while True:
            try:
                x = int(input("Enter row (0-5): "))
                y = int(input("Enter column (0-5): "))
                if x < 0 or x >= self.size or y < 0 or y >= self.size:
                    print("Неправильно введенные кординаты. Повторите.")
                    continue
                if self.computer_board[x][y] != " ":
                    print("Ты уже стрелял сюда.Попробуй снова.")
                    continue
                break
            except ValueError:
                print("Неправильный ввод. Повторите.")

        for ship in self.computer_ships:
            if ship.position == (x, y):
                ship.hits += 1
                self.computer_board[x][y] = "X"
                print("Попал!")
                if ship.is_sunk():
                    print(f"Ты уничтожил  {ship.size}-корабль!")
                return
        self.computer_board[x][y] = "O"
        print("Мимо.")

    def computer_shoot(self):
        x = random.randint(0, self.size - 1)
        y = random.randint(0, self.size - 1)
        while self.player_board[x][y] != " ":
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)

        for ship in self.player_ships:
            if ship.position == (x, y):
                ship.hits += 1
                self.player_board[x][y] = "X"
                print("Твой соперник ранил твой корабль!")
                if ship.is_sunk():
                    print(f"Соперник уничтожил {ship.size}-корабль!")
                return
        self.player_board[x][y] = "O"
        print("Твой соперник промахнулся.")

    def play(self):
        self.place_ships()
        while True:
            self.display_boards()
            self.player_shoot()

            if all(ship.is_sunk() for ship in self.computer_ships):
                print("Вы победили!")
                break
            self.computer_shoot()
            if all(ship.is_sunk() for ship in self.player_ships):
                print("Победил соперник !")
                break

if __name__ == "__main__":
    game = Board()
    game.play()
