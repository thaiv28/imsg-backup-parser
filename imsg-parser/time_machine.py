import random
from message import Message

class TimeMachine():
    def __init__(self, text):
        self.text = text
        self.separator = '----------------------------------------------------'
        self.messages = self.get_messages(text)
        
    
    def random(self):
        return self.messages[random.randint(0, len(self.messages) - 1)]
    
    def get_messages(self, text):
        split = text.splitlines()
        messages = []
        
        if split[0] == self.separator:
            split.pop(0)
        
        t = ''
        for line in split:
            if line == self.separator:
                messages.append(Message(t))
                t = ''
            elif line != '':
                t += line + '\n'
                
        return messages
            
    
if __name__ == "__main__":
    f = open('../backup.txt', 'r')
    
    t = TimeMachine(f.read())
    print(t.random())
    
    f.close()