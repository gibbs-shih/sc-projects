"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

This file contains a class,BreakoutGraphics, to build a basic framework of breakout game.
And some methods help to successfully run the game.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random
from campy.graphics.gimage import GImage


BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 4        # Number of rows of bricks.
BRICK_COLS = 4        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 2.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:
    """
    This class builds a basic framework of breakout game.
    """

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)
        self.bg = GRect(self.window.width, self.window.height)
        self.bg.filled = True
        self.bg.filled_color = 'black'
        self.bg.color = 'black'
        self.window.add(self.bg)

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'crimson'
        self.paddle.color = 'honeydew'
        self.window.add(self.paddle, (self.window_width-paddle_width)/2, self.window_height-paddle_offset)

        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.ball.fill_color = 'hotpink'
        self.ball.color = 'hotpink'
        self.window.add(self.ball, (self.window_width-ball_radius)/2, (self.window_height-ball_radius)/2)

        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = INITIAL_Y_SPEED

        # Initialize our mouse listeners.
        onmousemoved(self.move)
        onmouseclicked(self.start)

        # Draw bricks.
        for i in range(0, brick_rows):
            for j in range(0, brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if i < brick_rows / 5:
                    self.brick.color = 'red'
                    self.brick.fill_color = 'red'
                elif i < brick_rows / 5 * 2:
                    self.brick.color = 'coral'
                    self.brick.fill_color = 'coral'
                elif i < brick_rows / 5 * 3:
                    self.brick.color = 'gold'
                    self.brick.fill_color = 'gold'
                elif i < brick_rows / 5 * 4:
                    self.brick.color = 'green'
                    self.brick.fill_color = 'green'
                elif i <= brick_rows:
                    self.brick.color = 'royalblue'
                    self.brick.fill_color = 'royalblue'
                self.window.add(self.brick, (brick_width+brick_spacing)*j, brick_offset+(brick_height+brick_spacing)*i)
                self.bricks = brick_rows * brick_cols

        # lives
        self.l1 = GOval(ball_radius*2, ball_radius*2)
        self.l1.filled = True
        self.l1.fill_color = 'hotpink'
        self.l1.color = 'hotpink'
        self.window.add(self.l1, (self.window_width-10*ball_radius), (self.window_height-3*ball_radius))

        self.l2 = GOval(ball_radius * 2, ball_radius * 2)
        self.l2.filled = True
        self.l2.fill_color = 'hotpink'
        self.l2.color = 'hotpink'
        self.window.add(self.l2, (self.window_width - 7 * ball_radius), (self.window_height - 3 * ball_radius))

        self.l3 = GOval(ball_radius * 2, ball_radius * 2)
        self.l3.filled = True
        self.l3.fill_color = 'hotpink'
        self.l3.color = 'hotpink'
        self.window.add(self.l3, (self.window_width - 4 * ball_radius), (self.window_height - 3 * ball_radius))

        self.lives = 0

        # score_label
        self.score_label = GLabel('scores: 0')
        self.score_label.font = 'SansSerif-20-bold'
        self.score_label.color = 'cornsilk'
        self.window.add(self.score_label, 1, self.window.height-1)

        # A switch controls whether to start the game.
        self.lock = False

        # An object is used to store a value while using window.get_object_at().
        self.obj = None

    def move(self, event):
        """
        :param event: mouse(x,y)
        This function controls the paddle horizontally moving with the mouse.
        """
        self.paddle.y = self.window.height-PADDLE_OFFSET
        if event.x <= PADDLE_WIDTH/2:
            self.paddle.x = 0
        elif event.x <= self.window_width-PADDLE_WIDTH/2:
            self.paddle.x = event.x-PADDLE_WIDTH/2
        elif event.x > self.window_width-PADDLE_WIDTH/2:
            self.paddle.x = self.window_width-PADDLE_WIDTH

    def start(self, event):
        """
        This function controls to throw a ball and shows how many lives left.
        While the ball is moving, this function helps to avoid any mouse clicks.
        """
        if self.lock:
            pass
        else:
            self.lock = True
            self.lives += 1
            if self.lives == 1:
                self.window.remove(self.l1)
            if self.lives == 2:
                self.window.remove(self.l2)
            if self.lives == 3:
                self.window.remove(self.l3)

    def get_dx(self):
        """
        This method gets the hidden dx and return.
        :return: __dx
        """
        return self.__dx

    def get_dy(self):
        """
        This method gets the hidden dy and return.
        :return: __dy
        """
        return self.__dy

    def check(self):
        """
        This method checks the four points of the ball and return the object if it's not None.
        :return: obj (if it's not None)
        """
        self.obj = self.window.get_object_at(self.ball.x, self.ball.y)
        if self.obj is not None and self.obj is not self.score_label and self.obj is not self.bg:
            return self.obj
        else:
            self.obj = self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS, self.ball.y)
            if self.obj is not None and self.obj is not self.score_label and self.obj is not self.bg:
                return self.obj
            else:
                self.obj = self.window.get_object_at(self.ball.x, self.ball.y + 2 * BALL_RADIUS)
                if self.obj is not None and self.obj is not self.score_label and self.obj is not self.bg:
                    return self.obj
                else:
                    self.obj = self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS, self.ball.y + 2 * BALL_RADIUS)
                    if self.obj is not None and self.obj is not self.score_label and self.obj is not self.bg:
                        return self.obj

    def set_ball(self):
        """
        This method sets the ball in the central area of the breakout game.
        """
        self.window.add(self.ball, (self.window_width - BALL_RADIUS) / 2, (self.window_height - BALL_RADIUS) / 2)

    def set_ball_velocity(self):
        """
        This method gives dx randomly.
        """
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def game_over(self):
        """
        When lives are used over, the game is over!
        """
        game_over = GLabel('Game over :(')
        game_over.font = '-40-bold'
        game_over.color = 'gray'
        self.window.add(game_over, (self.window.width/2)-(game_over.width/2), self.window.height/2)

    def win(self):
        """
        All of the bricks are broken out. You win!
        """
        win = GImage('win.gif')
        self.window.add(win, (self.window.width/2)-(win.width/2), BRICK_OFFSET)


