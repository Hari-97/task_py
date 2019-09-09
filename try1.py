class Sumofdigits:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    def addition(self):
        self.list_of_sum = []
        for i in range(self.start,self.stop):
            sum1=0
            while i > 0:
                rem = i % 10
                sum1 = sum1 + rem
                i = i // 10
            self.list_of_sum.append(sum1)