from time_machine import TimeMachine

if __name__ == "__main__":
    f = open('../backup.txt', 'r')
    
    t = TimeMachine(' ')
    search = t.search('')
    print(search[0])
    
    f.close()