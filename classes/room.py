from typing import List


class Room:
    def __init__(
        self, room_number: int, available: bool, subjects: List[str], capacity: int = 0
    ) -> None:
        self.room_number = room_number
        self.available = available
        self.subjects = subjects
        self.capacity = capacity

    def __repr__(self) -> str:
        return f"Room: room_number={self.room_number}, available={self.available}, subjects={self.subjects}, capacity={self.capacity}"

    def get_room_number(self):
        return self.room_number
