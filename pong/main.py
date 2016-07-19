from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, \
        ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

# TODO: finish touch input
# TODO: package game to Android


class PongGame(Widget):
    ball = ObjectProperty(None)

    def serve_ball(self):
        self.ball_center = self.center
        self.ball.velocity = Vector(4,0).rotate(randint(0, 360))

    def update(self, dt):
        self.ball.move()

        # bounce off top and bottom
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

        # bounce off left/right
        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.velocity_x *= -1


class PongBall(Widget):
    # velocity of the ball
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # move the ball one step - function will be called in equal intervals
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos



class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball() # finally moving
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


if __name__ == '__main__':
    PongApp().run()

