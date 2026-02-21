from pathlib import Path

import arcade

ASSETS_PATH = Path(__file__).parent / "assets"


class App(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Arcade Project")
        arcade.set_background_color(arcade.color.CORNFLOWER_BLUE)

        self.robot_texture = arcade.load_texture(ASSETS_PATH / "robot.png")
        self.robot_sprite = arcade.Sprite(
            self.robot_texture, center_x=200, center_y=200
        )
        self.sprite_list = arcade.SpriteList()
        self.sprite_list.append(self.robot_sprite)

    def on_draw(self):
        self.clear()
        self.sprite_list.draw()


def main():
    App().run()


if __name__ == "__main__":
    main()
