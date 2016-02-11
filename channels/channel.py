class Channel:
    def __init__(self, name):
        self.name = name
        self.subs = []

    def update(self, message):
        for sub in self.subs:
            sub.update(message)

    def sub(self, obj):
        self.subs.append(obj)

    def unsub(self, obj):
        self.subs.remove(obj)
