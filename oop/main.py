from oop.dog import Dog
from oop.snake import Snake


class Main:
    @staticmethod
    def run() -> None:
        dog = Dog(name="Rex")
        print(dog)
        print(dog.communicate())
        print(dog.behavior())

        print("----------------------------------")

        snake = Snake(name="Viper")
        print(snake)
        print(snake.communicate())
        print(snake.behavior())


if __name__ == "__main__":
    Main.run()
