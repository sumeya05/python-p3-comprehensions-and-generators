# list_comprehension.py

def return_evens(seq):
    """
    Return a list of all even numbers in the input sequence.
    
    Args:
        seq (list of int): The input sequence of integers.
        
    Returns:
        list of int: List containing only the even numbers from seq.
    """
    return [x for x in seq if x % 2 == 0]


def make_exclamation(sentences):
    """
    Return a list of sentences with an exclamation mark added to each.
    
    Args:
        sentences (list of str): List of sentence strings.
        
    Returns:
        list of str: List of sentence strings with "!" appended.
    """
    return [s + "!" for s in sentences]
