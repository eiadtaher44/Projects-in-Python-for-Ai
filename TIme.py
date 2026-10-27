
class Time:
    def __init__(self,hours=0,minutes=0,seconds=0):
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds
        self._normalize()
        
    def _normalize(self):
        self.minutes+=self.seconds //60
        self.seconds=self.seconds%60
        
        self.hours+=self.minutes //60
        self.minutes=self.minutes%60
        
    def __add__(self,other):
        new_hou=self.hours+other.hours
        new_min=self.minutes+other.minutes
        new_sec=self.seconds+other.seconds
        return Time(new_hou,new_min,new_sec)
       
    def __iadd__(self,seconds_incrmint=1):
        self.seconds+=seconds_incrmint
        self._normalize()
        return self
    def incrumant(self):
        self.seconds+=1
        self._normalize()
        
    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
        
t1=Time(1,120,160)
t2=Time(1,60,0)
print(t1+t2)
        