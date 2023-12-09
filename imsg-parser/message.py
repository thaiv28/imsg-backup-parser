class Message():
    def __init__(self, text):
        self.meta = text.split('\n')[0].strip()
        self.text = text.split('\n')[1].strip()
        
    def __str__(self):
        return self.meta + '\n' + self.text