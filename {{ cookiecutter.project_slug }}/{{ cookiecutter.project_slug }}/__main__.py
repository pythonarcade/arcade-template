import arcade


class App(arcade.Window):
    
    def __init__(self):
        super().__init__(800, 600, "Arcade Web Template")
        arcade.set_background_color(arcade.color.CORNFLOWER_BLUE)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Hello, Arcade!", self.width // 2, self.height // 2, arcade.color.WHITE)


def main():
    App().run()


if __name__ == "__main__":
    main()