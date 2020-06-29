from typing import List

class Solution:

    reached = set()

    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        delay = 0
        dest = []

        for edge in times:
            source, destination, travel = edge[0], edge[1], edge[2]

            if source == K:
                if destination not in self.reached:
                    dest.append(destination)
                self.reached.add(destination)
                delay = max(delay, travel)

        for new_source in dest:
            delay += self.networkDelayTime(times, N, new_source)
        return delay


if __name__ == '__main__':
    s = Solution()
    print(s.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
