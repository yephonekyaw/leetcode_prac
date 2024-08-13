from collections import deque

def canVisitAllRooms(rooms):
    unlocked_rooms = deque([r for r in rooms[0]])
    visited_rooms = [False] * len(rooms)
    visited_rooms[0] = True
    while unlocked_rooms:
        key = unlocked_rooms.popleft()
        if not visited_rooms[key]:
            for r in rooms[key]:
                unlocked_rooms.append(r)
            visited_rooms[key] = True
    return all(visited_rooms)

def main():
    rooms = [[1],[2],[3],[]]
    print(canVisitAllRooms(rooms))

main()