from typing import List, Tuple, Dict, Set, Union
import typing
n : int = 5

name: str = "Rashi"


def sum(a: int, b: int) -> int:
  return a + b 




# advanced type hint

from typing import List, Tuple, Dict, Set, Union

# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]

# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)

# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}

# union type for variable that can hold multiple types
identifier: Union[int, str] = "ID123"
identifier = 1234 