import tkinter
import server

s = [] # list config

class App:
    def __init__(self, *args): # basic dates
        self.size = (800, 600)
        self.title = 'Window'
        self.icon = 'path./'

    def run(self, region, status): # set start pos
        self.region = region
        self.status = status

    def config(self, **kwargs):
        for i in kwargs: # sorting in list
            s.pop[i]
            
if __name__ == '__main__':
    app = App
    app.run()
