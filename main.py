from handlers.engine import GraphicsEngine
import yaml


class App():
    def __init__(self) -> None:
        self.app = GraphicsEngine()

    def run(self, config_file='config.yml'):
        self.app.run()
        

    def load_data(self):
        pass

    def load_objects(self):
        pass


if __name__ == "__main__":
    app = App()
    app.run()
