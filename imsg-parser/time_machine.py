import random
from message import Message

class TimeMachine():
    def __init__(self, text):
        self.text = text
        self.separator = '----------------------------------------------------'
        self.messages = self.get_messages(text)
        
    
    def random(self):
        return self.messages[random.randint(0, len(self.messages) - 1)]
    
    
    def search(self, term, caps_sensitive=False, strict=False):
        ret = []
        
        s = term.strip()
        
        for msg in self.messages:
            if caps_sensitive and self.contains(msg.text, s, strict=strict):
                ret.append(msg)
            if not caps_sensitive and self.contains(msg.text.upper(), s.upper(),
                                                    strict=strict):
                ret.append(msg)
        return ret
    
    
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
    
    # strict variable determines if allows search term to be start of a word,
    # but not the whole word
    def contains(self, msg, search, strict=True):
        index = msg.find(search)
        last_index = index + len(search) - 1
        
        if index == -1:
            return False
        
        # #checks if standalone word
        if index > 0 and msg[index - 1].isspace():
            if last_index < len(msg) - 1 and msg[last_index + 1].isspace():
                return True
        
        # checks if word is whole message
        if msg == search:
            return True
        
        # #checks if word is at beginning
        if index == 0 and msg[last_index + 1].isspace():
            return True
        
        # #checks if word is at end
        if last_index == len(msg) - 1 and msg[index - 1].isspace():
            return True
        
        if not strict:
            if index == 0:
                return True
            if msg[index - 1].isspace():
                return True
        
        return False
            
    
if __name__ == "__main__":
    f = open('../backup.txt', 'r')
    
    t = TimeMachine(f.read())
    search = t.search('bagel', strict=False, caps_sensitive=False)
    for s in search:
        print(s)
        print(t.separator)
    
    f.close()