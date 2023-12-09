class Split():
    
    # month is starting month, year is starting year
    def __init__(self, month=0, year=2023):
        self.year = str(year)
        self.months = ['01', '02', '03', '04', '05', '06', 
                  '07', '08', '09', '10', '11', '12']
        self.m_ind = month
        self.path = '../texts/'
    
    def parse_month(self, file):
        
        f = open(self.path + self.year + '-' + self.months[self.m_ind] + '.txt', 'w')
        
        for line in file.readlines():
            
            if(str(int(self.year) + 1) in line):
                f.close()
                f = self.increment_year()
            
            if(self.m_ind != 11 and self.year + '-' + self.months[self.m_ind + 1] in line):
                f.close()
                f = self.increment_month()
                
            f.write(line)
            
        f.close()
                
                
    def increment_year(self):
        self.year = str(int(self.year) + 1)
        print(self.year)    
        self.m_ind = 0
        f = open(self.path + self.year + '-' + self.months[self.m_ind]+'.txt', 'w')
        return f
            
    def increment_month(self):
        f = open(self.path + self.year + '-' + self.months[self.m_ind + 1]+'.txt', 'w')
        self.m_ind += 1
        
        return f
    

if __name__ == "__main__":
    file = open('../backup.txt', 'r')
    
    s = Split(month=10, year=2022)
    s.parse_month(file)
    
    file.close()
    
    