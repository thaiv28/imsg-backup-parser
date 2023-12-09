class Message():
    def __init__(self, text):
        s = text.strip().split('\n')
        if len(s) == 3:
            self.meta = s[0].strip()
            self.reply = s[1].strip()
            self.text = s[2].strip()
        elif len(s) == 2:
            self.meta = s[0].strip()
            self.text = s[1].strip()
            self.reply = None
        else:
            self.meta = s[0].strip()
            self.text = ''
            self.reply = None
            
        
    def __str__(self):
        if self.reply:
            return self.meta + '\n' + self.reply + '\n' + self.text
        else:
            return self.meta + '\n' + self.text