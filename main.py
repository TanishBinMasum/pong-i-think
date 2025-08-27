# i dont know if this works i didnt actually check it :/
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
        # Create game elements
        self.player_paddle = self.canvas.create_rectangle(
            50, 250, 50 + self.paddle_width, 250 + self.paddle_height, fill="#3498db"
        )
        self.computer_paddle = self.canvas.create_rectangle(
            740, 250, 740 + self.paddle_width, 250 + self.paddle_height, fill="#e74c3c"
        )
        self.ball = self.canvas.create_oval(
            390, 290, 390 + self.ball_radius * 2, 290 + self.ball_radius * 2, fill="#f1c40f"
        )
