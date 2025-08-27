class PongGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Python Pong")
        self.master.geometry("800x600")

        # Create the game canvas
        self.canvas = tk.Canvas(self.master, bg="#2c3e50", width=800, height=600)
        self.canvas.pack()

        # Game variables
        self.paddle_width = 10
        self.paddle_height = 100
        self.ball_radius = 10
        self.ball_speed_x = 5
        self.ball_speed_y = 5
        self.paddle_speed = 10
        self.player_score = 0
        self.computer_score = 0
        self.game_running = False
