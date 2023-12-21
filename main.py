import tkinter
import server

class App:
    def __init__(self, *args):
        self.size = (800, 600)
        self.title = 'Window'
        self.icon = 'path./'

    def run(self,to_region, region, status):
        self.region = region
        self.to_region = to_region
        self.status = status

        if region != to_region:
            status = True
            while status:
                start()
                if status == False:
                    server.exit()
        else:
            print("Нет подключения. Выберите другую страну!")

    def config(self, **kwargs):
        pass

if __name__ == '__main__':
    app = App
    app.run()

