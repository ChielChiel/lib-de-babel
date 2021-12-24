print("dit is kaasje import")

# class Library_de_babel:
#     pass


class Library_de_babel:
    """sumary_line
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    
    def __init__(self, page_size) -> None:
        # self.alfabet = "abcdefghijklmnopqrstuvwxyz., "
        self.alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', ',', ' ', '\n']
        self.lookup_alfabet = {'a': 0, 'b': 1, 'c': 2,'d': 3,'e': 4,'f': 5,'g': 6,'h': 7,'i': 8,'j': 9,'k': 10,'l': 11,'m': 12,'n': 13,'o': 14,'p': 15,'q': 16,'r': 17,'s': 18,'t': 19,'u': 20,'v': 21,'w': 22,'x': 23,'y': 24,'z': 25,'.': 26,',': 27,' ': 28}
        self.alfabet_size = 29 # len(self.alfabet)
        self.page_size = page_size
        return


    """
    [summary]
        converts base-10 into a page
    [args]
        numb: int base-10
        length: int
    """
    def creat_page(self, numb, length = None):
        # print(numb)
        if length == None:
            length = self.page_size
        result = self.nthnary(numb, lente=length)
        # print("start:" + ''.join([alfabet[x] for x in k]) + ";end")
        result = [x for y in (result[i:i+80] + [29] * (i < len(result) - 2) for i in range(0, len(result), 80)) for x in y]

        return ''.join([self.alfabet[x] for x in result])

    def FillZero(self, to, listt):
        while len(listt) < to:
            listt.append(0)
        return listt

    """
    [summary]
        converts int into base 29 number
    [args]
        n : base-10 number
        lente : int number of wheels

    [returns]
        nums: [base-29]
    """
    def nthnary(self, n, lente=4):
        if n == 0:
            return self.FillZero(lente, [])
        nums = []
        while n:
            n, r = divmod(n, self.alfabet_size)
            nums.append(r)
            # print("nums", nums)
        nums = self.FillZero(lente, nums)
        # return ''.join(reversed(nums))
        nums.reverse()
        
        return nums #reversed(nums)


    def arynth(self, input_base, output_base = 29):
        arr = [int(i) for i in input_base]
        arr.reverse()
        n = 0
        total = 0
        for digit in arr:
            total += digit * (output_base ** n)
            n += 1
        return total

    def nth(self, input_list):
        outputt = []
        for digit in input_list:
            outputt.append(self.arynth(digit))
        return outputt    

    def string_to_base(self, input_str):
        mid_string = []
        for s in input_str:
            mid_string.append(str(self.lookup_alfabet[s]))
        return mid_string