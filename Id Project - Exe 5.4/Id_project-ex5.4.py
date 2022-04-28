class IDIterator:    
    """
    This class return the next valid id values from the id that entered.
    """
    def __init__(self, id_number):
        """
        This method sets initial values.
        :param id_number: the id number
        :type id_number: int
        :return: None
        :rtype: None
        """
        self._id = id_number
    
    def __iter__(self):
        """
        This method returns a reference to the iterator.
        :return: the `self` object
        :rtype: __main__.IDIterator
        """
        return self
    
    def __next__(self):
        """ 
        This method calculating the next valid id from the id that entered.
        :return: the next valid id
        :rtype: int
        :raise: StopIteration: raises an Exception
        """
        while True:
            self._id += 1
            
            if self._id > 999999999:
                raise StopIteration
            elif check_id_valid(self._id):        
                return self._id

class IllegalId(Exception):
    """
    This class is an Exception that raise when the id is illegal.
    """
    def __init__(self, id_number):
        """
        This method sets initial values.
        :param id_number: the id number
        :type id_number: int
        :return: None
        :rtype: None        
        """
        self._id_number = id_number
    
    def __str__(self):
        """
        This method appeared when print the class.
        :return: That the id is illegal
        :rtype: str
        """
        return "The Id ({0}) is illegal!".format(self._id_number)


def id_generator(id_num):
    """
    This function return the next valid id values from the id that entered.
    :param id_num: the id number
    :type id_num: int
    :return: the next valid id 
    :rtype: int
    """
    for i in range(id_num, 1000000000):
        if check_id_valid(i):        
            yield i

def check_id_valid(id_number):
    """
    This function checks if the id is valid.
    :param id_number: the id number
    :type id_number: int
    :return: if the id is valid
    :rtype: bool
    :raise: IllegalId: raises an Exception
    """
    id_digits_list = list(map(int, str(id_number)))
    
    if len(id_digits_list) == 9:
        id_check = (id_digits_list[i - 1] * 2 if i % 2 == 0 else id_digits_list[i - 1] for i in range(1, len(id_digits_list) + 1))
        id_check_fix = (i // 10 + i % 10 for i in id_check)
        return sum(id_check_fix) % 10 == 0
    else:
        raise IllegalId(id_number)


def main():
    generator = id_generator(123456780)
    
    try:    
        for i in range(10):
            print(next(generator))
    
    except IllegalId as e:
        print(e)
    
    except StopIteration:
        print('StopIteration Exception')
    
    except:
        print('An Exception appeared')

if __name__ == '__main__':
    main()
#work!