"""
(a, b) = (회의시작시간, 회의종료시간)
한 회의실에서 하는 회의의 시간은 서로 겹치지 않도록 해야 하고, 회의실은 최대한 조금만 사용해야 한다.
* (1, 2) (2, 3) 과 같은 형태도 가능하다.

우선 naive하게 생각하면, 회의실마다 회의 종료 시각을 확인해서, 현재 시작할 회의와 겹치지 않으면 ㄱㄱ
"""


import sys
from heapq import heappush, heappop
from typing import List, Tuple, Optional


class MeetingRoom:
    last_meeting_ends_at: int
    
    def __init__(self, last_meeting_ends_at: int):
        self.last_meeting_ends_at = last_meeting_ends_at
    
    def __lt__(self, other):
        return self.last_meeting_ends_at < other.last_meeting_ends_at


n: int
schedules: List[Tuple[int, int]] = []
meeting_rooms: List[MeetingRoom] = []


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        schedules.append((a, b))
    
    schedules.sort(key=lambda x: (x[0], x[1]))
    
    for start, end in schedules:
        if not meeting_rooms:
            heappush(meeting_rooms, MeetingRoom(end))
            continue
        
        if meeting_rooms[0].last_meeting_ends_at <= start:
            heappop(meeting_rooms)
        
        heappush(meeting_rooms, MeetingRoom(end))
    
    print(len(meeting_rooms))
