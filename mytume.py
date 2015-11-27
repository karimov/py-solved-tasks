class MyTime:
    def __init__(self, hrs=0, mins=0, secs=0):
        """ Create a MyTime object initialized to hrs, mins, secs """
        self.hours = hrs
        self.minutes = mins
        self.seconds = secs
    def __str__(self):
    	return "{0}:{1}:{2}".format(self.hours, self.minutes, self.seconds)
    def increment(self, seconds):
        self.seconds += seconds
        while self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1
        while self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1
    
def add_time(t1, t2):
    h = t1.hours + t2.hours
    m = t1.minutes + t2.minutes
    s = t1.seconds + t2.seconds
    if s >= 60:
       s -= 60
       m += 1
    if m >= 60:
       m -= 60
       h += 1
    sum_t = MyTime(h, m, s)
    return sum_t
    
    
    
current_time = MyTime(9, 14, 30)
bread_time = MyTime(3, 35, 0)
done_time = add_time(current_time, bread_time)
