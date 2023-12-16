import tkinter
import server

class App:
    def __init__(self, *args):
        self.size = (800, 600)
        self.title = 'Window'
        self.icon = 'path./'

    def run(self, region, status):
        self.region = region
        self.status = status

    def config(self, **kwargs):
        pass

if __name__ == '__main__':
    app = App
    app.run()
