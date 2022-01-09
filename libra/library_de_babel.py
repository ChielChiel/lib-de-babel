import numpy as np
import random
from typing import List

class Library_de_babel:
    
    def __init__(self, page_size: int) -> None:
        self.alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', ',', ' ', '\n']
        self.lookup_alfabet = {'a': 0, 'b': 1, 'c': 2,'d': 3,'e': 4,'f': 5,'g': 6,'h': 7,'i': 8,'j': 9,'k': 10,'l': 11,'m': 12,'n': 13,'o': 14,'p': 15,'q': 16,'r': 17,'s': 18,'t': 19,'u': 20,'v': 21,'w': 22,'x': 23,'y': 24,'z': 25,'.': 26,',': 27,' ': 28}
        self.alfabet_size = len(self.lookup_alfabet)
        self.page_size = page_size
        return



    def search(self, search_string: str) -> int:
        """Returns number where you can find the search string.

        Args:
            search_string (str): The string you want to find in the library of babel.

        Returns:
            int: The page number where your search string is firstly encountered.
        """        
        list_of_base_representations: List[str] = self.string_to_base(search_string)
        total_rotations_for_search: int = self.calculate_rotations(list_of_base_representations)
        return total_rotations_for_search


    def create_page(self, page_number: str, length = None) -> str:
        """Converts base-10 into a page

        Args:
            page_number (int): page number given in base-10
            length (int, optional): The amount of characters a page has. Defaults to None.

        Returns:
            str: A generated page in the library of babel based on the page number.
        """        

        # Set to default length if none is given
        if length == None:
            length = self.page_size
        
        result = self.rotations_to_base_29(page_number, length=length)
        
        # Add a '\n' after every 80 characters. Found here: https://stackoverflow.com/a/31040944/8902440
        result = [x for y in (result[i:i+80] + [29] * (i < len(result) - 2) for i in range(0, len(result), 80)) for x in y]
        
        return ''.join([self.alfabet[x] for x in result])

    def FillZero(self, total_length: int, short_input_list: List[int]):
        """Pad zero's to the `total_length`.

        Args:
            total_length (int): The maxium length of the intended list.
            short_input_list (List[int]): The input list withouth the desired length.

        Returns:
            List[int]: The `short_input_list`, with padded zero's in front.
        """        
        while len(short_input_list) < total_length:
            short_input_list.append(0)
        return short_input_list

    def rotations_to_base_29(self, rotations: int, length: int = 4) -> List[int]:
        """Convert the number of rotations (usually page number) to a base-29 representation

        Args:
            rotations (int): The number of revolutions the last wheel has to be spun, or the page number
            length (int, optional): The length of the output array, will be padded with zero's. Defaults to 4.

        Returns:
            List[int]: A base-29 representation of the page_number
        """        
        
        if rotations == 0:
            return self.FillZero(length, [])
        alfabet_numbers = []
        while rotations:
            rotations, r = divmod(rotations, self.alfabet_size)
            alfabet_numbers.append(r)
        alfabet_numbers = self.FillZero(length, alfabet_numbers)
        alfabet_numbers.reverse()
        return alfabet_numbers


    def calculate_rotations(self, input_base: List[str], output_base: int = 29):
        """Calculate the number of rotations needed to achieve the given input.

        Args:
            input_base (List[str]): A base-`output_base` representation of a string of characters
            output_base (int, optional): The number of characters the output alfabet contains (See `self.lookup_alfabet`). Defaults to 29.

        Returns:
            int: total rotations or pages needed to find the input
        """        
        arr = [int(i) for i in input_base]
        arr.reverse()
        position_pointer = 0
        total_rotations = 0
        for digit in arr:
            total_rotations += digit * (output_base ** position_pointer)
            position_pointer += 1
        return total_rotations

    # def nth(self, input_list):
    #     outputt = []
    #     for digit in input_list:
    #         outputt.append(self.calculate_rotations(digit))
    #     return outputt    

    def string_to_base(self, input_str: str) -> List[str]:
        """Convert the `input_str` to a base-29 list of numbers

        Args:
            input_str (str): The string to be converted to base-29 numbers

        Returns:
            List[str]: The input_str in base-29 numbers
        """        
        base_29_output = []
        for s in input_str:
            base_29_output.append(str(self.lookup_alfabet[s]))
        return base_29_output

    def random_base(self, base_number: int = 29, length: int = 10) -> str:
        """Generate a random number in the given base and length. Retrieved from here: https://stackoverflow.com/a/70584044/8902440

        Args:
            base_number (int, optional): The desired base type. Max value is 36. Defaults to 29.
            length (int, optional): The desired length of the base number. Defaults to 10.

        Returns:
            str: A random base-[base_number] number of length `length`.
        """        
        alfabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return "".join(random.choices(alfabet[:base_number], k=length))



    def number_to_base29(self, number: int) -> str:
        return np.base_repr(number, 29)
    
    def base29_to_number(self, base_29: str) -> int:
        return int(base_29, 29)

    def number_of_possible_occurences(self, text_length: int, sub_length: int) -> int:
        # def nu_of_po_oc(text_length, sub_length):
        return (text_length + 1) - sub_length

    def number_of_containing_pages(self, page_length: int, sub_length: int) -> int:
        #def nu_of_co_pa(page_length, sub_length):
        one_page = self.alfabet_size ** (page_length - sub_length)
        return one_page * self.number_of_possible_occurences(page_length, sub_length)