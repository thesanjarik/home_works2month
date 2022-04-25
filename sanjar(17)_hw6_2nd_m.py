def get_list() -> list:
    return list(range(0, 1_000_000_000, 2))


"""
    what is Binary Search?
    then do Solution for search target in list
"""


class Solution:
    """
        find_target -> YOUR_CODE
    """

    def find_target(self, list, target):
        step = 0
        for i in range(len(list, target)):
            for j in range(i + 1, len(list, target)):
                step += 1
                if list[i] == target[j]:
                    print(i, j, f"Big 0 {step}")


get_list()






