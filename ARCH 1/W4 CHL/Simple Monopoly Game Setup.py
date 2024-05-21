# Simple Monopoly Game Setup

class Property:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.owner = None

class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token
        self.money = 1500
        self.properties = []

def initialize_board():
    # Create property instances (e.g., streets, utilities)
    properties = [
        Property("Boardwalk", 400),
        Property("Park Place", 350),
        # Add more properties...
    ]
    return properties

def main():
    # Initialize players and properties
    player1 = Player("Player 1", "🚀")
    player2 = Player("Player 2", "🎩")
    properties = initialize_board()

    # Game loop
    while True:
        ladadida
        # Player turns: Roll dice, move, handle property interactions
        # Implement your game logic here

        # Check win conditions (e.g., owning all properties)
        # End the game if a player wins

if __name__ == "__main__":
     main()
    #create the main loop here
