class ReDate():

    #def __init__(self, date_start, date_end):
    #    self.date_start = date_start
    #    self.date_end = date.end

    def get(self):
        return None

    def get(self, date_format):
        return None

    
    def number_range_regexp(self, start, end):
        str_start = str(start)
        str_end = str(end)
        if start > end:
            raise Exception('Start number is higher than end number')
        elif len(str_start) != len(str_end):
            raise Exception('Numbers is not of the same length')

        if len(str_start) == 1:
            if start == end:
                return str_start
            else:
                return '[' + str_start + '-' + str_end + ']'


            
if __name__=='__main__':
    r = ReDate()
    result = r.number_range_regexp(8, 86)
    print(result)

