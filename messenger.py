class Messenger(object):
    def send(self, destination, msg):
        print(msg)

class Emailer(Messenger):
    pass
