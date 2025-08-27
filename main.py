# i dont know if this works i didnt actually check it :/
# Import the Tkinter library for the GUI
import tkinter as tk

# Define a class for the game itself
class PongGame:
    def __init__(self, master):
        """
        Initializes the Pong game.

        Args:
            master: The root Tkinter window.
        """
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

        # Create score text
        self.player_score_text = self.canvas.create_text(
            200, 50, text=f"Player: {self.player_score}", fill="white", font=("Helvetica", 24)
        )
        self.computer_score_text = self.canvas.create_text(
            600, 50, text=f"Computer: {self.computer_score}", fill="white", font=("Helvetica", 24)
        )

        # Start/Reset button
        self.start_button = tk.Button(
            self.master, text="Start Game", command=self.start_game, font=("Helvetica", 16),
            bg="#2ecc71", fg="white", bd=0, relief="flat", padx=10, pady=5
        )
        self.start_button_window = self.canvas.create_window(
            400, 300, window=self.start_button
        )

        # Bind keyboard events for player paddle control
        self.master.bind("<Up>", self.move_paddle_up)
        self.master.bind("<Down>", self.move_paddle_down)

    def start_game(self):
        """Starts the game loop."""
        if not self.game_running:
            self.game_running = True
            # Hide the start button
            self.canvas.delete(self.start_button_window)
            self.reset_ball()
            self.game_loop()

    def reset_ball(self):
        """Resets the ball to the center of the screen."""
        self.canvas.coords(self.ball, 390, 290, 410, 310)
        self.ball_speed_x = -self.ball_speed_x
        self.ball_speed_y = -self.ball_speed_y

    def move_paddle_up(self, event):
        """Moves the player paddle up."""
        if self.game_running:
            coords = self.canvas.coords(self.player_paddle)
            if coords[1] > 0:
                self.canvas.move(self.player_paddle, 0, -self.paddle_speed)

    def move_paddle_down(self, event):
        """Moves the player paddle down."""
        if self.game_running:
            coords = self.canvas.coords(self.player_paddle)
            if coords[3] < 600:
                self.canvas.move(self.player_paddle, 0, self.paddle_speed)

    def move_computer_paddle(self):
        """Basic AI to move the computer paddle towards the ball."""
        ball_coords = self.canvas.coords(self.ball)
        paddle_coords = self.canvas.coords(self.computer_paddle)
        ball_y_center = (ball_coords[1] + ball_coords[3]) / 2
        paddle_y_center = (paddle_coords[1] + paddle_coords[3]) / 2

        if paddle_y_center < ball_y_center:
            if paddle_coords[3] < 600:
                self.canvas.move(self.computer_paddle, 0, self.paddle_speed / 2)
        elif paddle_y_center > ball_y_center:
            if paddle_coords[1] > 0:
                self.canvas.move(self.computer_paddle, 0, -self.paddle_speed / 2)

    def game_loop(self):
        """The main game loop that updates the game state."""
        if not self.game_running:
            return

        # Move the ball
        self.canvas.move(self.ball, self.ball_speed_x, self.ball_speed_y)

        # Get coordinates of the ball and paddles
        ball_coords = self.canvas.coords(self.ball)
        player_paddle_coords = self.canvas.coords(self.player_paddle)
        computer_paddle_coords = self.canvas.coords(self.computer_paddle)

        # Check for collision with top/bottom walls
        if ball_coords[1] <= 0 or ball_coords[3] >= 600:
            self.ball_speed_y = -self.ball_speed_y

        # Check for collision with paddles
        if (
            ball_coords[0] <= player_paddle_coords[2] and
            ball_coords[3] >= player_paddle_coords[1] and
            ball_coords[1] <= player_paddle_coords[3] and
            ball_coords[0] >= player_paddle_coords[0]
        ) or (
            ball_coords[2] >= computer_paddle_coords[0] and
            ball_coords[3] >= computer_paddle_coords[1] and
            ball_coords[1] <= computer_paddle_coords[3] and
            ball_coords[2] <= computer_paddle_coords[2]
        ):
            self.ball_speed_x = -self.ball_speed_x

        # Check for scoring (ball goes past a paddle)
        if ball_coords[0] < 0:
            self.computer_score += 1
            self.canvas.itemconfig(self.computer_score_text, text=f"Computer: {self.computer_score}")
            self.reset_ball()
        elif ball_coords[2] > 800:
            self.player_score += 1
            self.canvas.itemconfig(self.player_score_text, text=f"Player: {self.player_score}")
            self.reset_ball()

        # Move the computer paddle
        self.move_computer_paddle()

        # Continue the game loop after a short delay
        self.master.after(10, self.game_loop)

# Main part of the script
if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()

    # Create and run the game
    game = PongGame(root)

    # Start the Tkinter event loop
    root.mainloop()
