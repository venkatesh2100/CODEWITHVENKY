# Input: plants = [2, 2, 3, 3], capacity = 5
# Output: 14
# Explanation: Start at the river with a full watering can:
# - Walk to plant 0 (1 step) and water it. Watering can has 3 units of water.
# - Walk to plant 1 (1 step) and water it. Watering can has 1 unit of water.
# - Since you cannot completely water plant 2, walk back to the river to refill(2 steps).
# - Walk to plant 2 (3 steps) and water it. Watering can has 2 units of water.
# - Since you cannot completely water plant 3, walk back to the river to refill(3 steps).
# - Walk to plant 3 (4 steps) and water it.
# Steps needed = 1 + 1 + 2 + 3 + 3 + 4 = 14.
import re
from typing import List


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:

        s = 0
        river = capacity
        while x < len(plants):
            if plants[x] >= capacity:
                capacity -= plants[x]
                x += 1
                s += 1
            else:
                s += (2 * x) + 1
                capacity = river

        return s
