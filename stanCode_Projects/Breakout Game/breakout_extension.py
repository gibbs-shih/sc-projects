"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

This program runs a classic breakout game.
"""

from campy.gui.events.timer import pause
from breakoutgraphic_extensions import BreakoutGraphics


FRAME_RATE = 1000 / 120  # 120 frames per second.
NUM_LIVES = 3  # chances you have


def main():
    """
    This function runs the breakout game.
    """
    graphics = BreakoutGraphics()
    brick_num = 0
    lives_used = 0
    dy2 = 0
    # Add animation loop here!
    while True:
        graphics.set_ball_velocity()
        dx = graphics.get_dx()
        dy = graphics.get_dy()
        lock = graphics.lock
        pause(1)
        while lock:
            if brick_num > graphics.bricks/2:
                graphics.ball.move(dx, dy2)
            else:
                graphics.ball.move(dx, dy)
            pause(FRAME_RATE)
            # ball moves in the window
            if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width-graphics.ball.width:
                dx = -dx
            if graphics.ball.y <= 0 or graphics.ball.y >= graphics.window.height-graphics.ball.height:
                dy = -dy
                dy2 = -dy2
            #  ball bounces when touches bricks and paddle; and remove the bricks
            obj = graphics.check()
            if obj is graphics.paddle:
                if dy > 0 or dy2 > 0:
                    dy = -dy
                    dy2 = -dy2
            elif obj is graphics.l1 or obj is graphics.l2 or obj is graphics.l3:
                pass
            elif obj:
                graphics.window.remove(obj)
                dy = -dy
                dy2 = -dy2
                brick_num += 1
                graphics.score_label.text = f'scores: {brick_num}'
                #  win the game
                if brick_num == graphics.bricks:
                    break
                if brick_num > graphics.bricks/2:
                    dy2 = dy*1.5
            #  ball moves out of the window, try again
            if graphics.ball.y+graphics.ball.height >= graphics.window.height:
                graphics.set_ball()
                graphics.lock = False
                lives_used += 1
                break
        # you win
        if brick_num == graphics.bricks:
            # graphics.set_ball()
            graphics.window.remove(graphics.ball)
            graphics.win()
            break
        # game over
        if lives_used == NUM_LIVES:
            graphics.window.remove(graphics.ball)
            graphics.game_over()
            break


if __name__ == '__main__':
    main()

'''
2. 如何加長/縮短paddle  remove再add
3. 如何掉落物體
'''