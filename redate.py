class ReDate():

    #def __init__(self, date_start, date_end):
    #    self.date_start = date_start
    #    self.date_end = date.end

    def get(self):
        return None

    def get(self, date_format):
        return None

    @classmethod 
    def number_range_regexp(cls, start, end):
        if int(start) > int(end):
            raise ValueError('Start number is higher than end number')
        elif len(start) != len(end):
            raise ValueError('Numbers is not of the same length')

        if len(start) == 1:
            if start == end:
                return start
            else:
                return '[' + start + '-' + end + ']'

        if start[0] == end[0]:
            # regexp for range between axx and byy:
            # if a = b, return a(regexp_range(xx-yy))
            result = start[0] 
            result += cls.number_range_regexp(start[1:], end[1:])
            
        else:
            # a(regexp_range(xx-99))
            nines = '9' * len(start[1:])
            result = start[0] + cls.number_range_regexp(start[1:], nines)
            result += '|'
            first_start = int(start[0])
            first_end = int(end[0])
            if first_end - first_start > 1:
                if first_start+1 == first_end-1:
                    # a+1[0-9]{len-1}
                    result += str(first_start+1)
                else:
                    # [a+1 - b-1][0-9]{len-1}
                    result += '[' + str(first_start+1) 
                    result += '-' + str(first_end-1) + ']'
                
                result += '[0-9]'
                if len(start[1:]) > 1:
                    result += '{' + str(len(start[1:])) + '}'
                result += '|' 

            # b(regexp_range(00-yy))
            zeroes = '0' * len(end[1:])
            result += end[0] + cls.number_range_regexp(zeroes, end[1:])


        if '|' in result:
            result = '(' + result + ')'
        return result 

if __name__=='__main__':
    result = ReDate.number_range_regexp(str(180), str(390))
    print(result)

