from typing import List, Dict, Union

# Create good script to create new list, which only contains users from Poland. Try to do it with List Comprehension.

UserType = Dict[str, Union[str, None]]

users = [
    {
        "name": "Kamil",
        "country": "Poland",
    },
    {
        "name": "John",
        "country": "USA",
    },
    {
        "name": "Yeti",
    },
]


def filter_users(users: List[UserType]) -> List[UserType]:
    """
    Filters users from Poland and returns a list of dictionaries.

    :param users: UserType
    :return: UserType
    """
    return [user for user in users if user.get("country") == "Poland"]


# Display sum of first ten elements starting from element 5:
numbers = [1, 5, 2, 3, 1, 4, 1, 23, 12, 2, 3, 1, 2, 31, 23, 1, 2, 3, 1, 23, 1, 2, 3, 123]


def calculate_sum(numbers: List[Union[int, float]]) -> Union[int, float]:
    """
    Calculates the sum of the first ten elements from the list, starting from the fifth index.

    :param numbers: list
    :return: int, float
    """

    return sum(numbers[4:14])


# Fill list with powers of 2, n [1..20]

def filling_list(power: int = 2) -> List[int]:
    """
    Create a list of powers of 2 for values of n in the range from 1 to 20.

    :param power: int
    :return: list
    """
    return [power ** i for i in range(1, 21)]


if __name__ == "__main__":
    print("Filter Users")
    print(filter_users(users=users))
    print()
    print("Calculate Sum")
    print(calculate_sum(numbers=numbers))
    print()
    print("Filling List")
    print(filling_list())
