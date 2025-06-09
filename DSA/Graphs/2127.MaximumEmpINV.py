from collections import deque
from copyreg import dispatch_table


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:

        # TODO: Using Graph dataStructure Mapping EveryOne's Fav Person ..Find the possible Cycle and Max it out.
        num_people = len(favorite)
        reversed_graph = [[] for _ in range(num_people)]

    # HACK: reversed_graph building LOL
        for Person in range(num_people):
            reversed_graph[favorite[Person]].append(Person)

        longest_cycle = 0
        two_cycle_inv = 0
        visited = [False] * num_people

    # HACK: ALL longest_cycle
        for Person in range(num_people):
            if not visited[Person]:

                visited_person = {}
                current_person = Person
                disance = 0
                while True:
                    if visited[current_person]:
                        break
                    visited[current_person] = True
                    visited_person[current_person] = disance
                    disance += 1
                    next_person = favorite[current_person]

                    if next_person in visited_person:
                        cycle_len = disance - visited_person[next_person]
                        longest_cycle = max(longest_cycle, cycle_len)

                        if cycle_len == 2:
                            visited_nodes = {current_person, next_person}
                            two_cycle_inv += (2 + self._bfs(next_person, visited_nodes, reversed_graph) + self._bfs(
                                current_person, visited_nodes, reversed_graph))

                            break
                    current_person = next_person

        return max(longest_cycle, two_cycle_inv)

    def _bfs(self, start_node: int, visted_node: set, reversed_graph):

        que = deque([(start_node, 0)])
        max_distance = 0
        while que:
            curr, curr_distance = que.popleft()

            for nei in reversed_graph[curr]:
                if nei in visted_node:
                    continue
                visted_node.add(nei)
                que.append((nei, curr_distance+1))
                max_distance = max(max_distance, curr_distance+1)
        return max_distance
