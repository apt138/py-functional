from typing import Tuple
import unittest

History = Tuple[Tuple[str], int]


def create_history() -> History:
    # state: history Tuple[str]
    # state: current_index: int
    return ("",), 0


def edit(history: History, text: str) -> History:
    data, current_index = history
    return (*data, text), current_index + 1


def undo(history: History) -> History:
    data, current_index = history
    return data, max(0, current_index - 1)


def redo(history: History) -> History:
    data, current_index = history
    return data, min(len(data) - 1, current_index + 1)


def current_state(history: History) -> str:
    data, current_index = history
    return data[current_index]


class TestTextManagement(unittest.TestCase):

    def setUp(self):
        self.history = create_history()

    def test_create(self):
        data, index = self.history
        self.assertEqual(data, ("",))
        self.assertEqual(index, 0)
        self.assertEqual(current_state(self.history), "")

    def test_edit(self):
        self.history = edit(self.history, "hello")
        data, index = self.history
        self.assertEqual(data, ("", "hello"))
        self.assertEqual(index, 1)
        self.assertEqual(current_state(self.history), "hello")

    def test_undo(self):
        self.history = edit(self.history, "hello")
        self.history = edit(self.history, "hello world")
        self.history = undo(self.history)
        data, index = self.history
        self.assertEqual(index, 1)
        self.assertEqual(current_state(self.history), "hello")

    def test_undo_many(self):
        self.history = edit(self.history, "hello")
        self.history = edit(self.history, "hello world")
        self.history = undo(self.history)
        self.history = undo(self.history)
        self.history = undo(self.history)
        _, index = self.history
        self.assertEqual(index, 0)
        self.assertEqual(current_state(self.history), "")

    def test_redo(self):
        self.history = edit(self.history, "hello")
        self.history = edit(self.history, "hello world")
        self.history = undo(self.history)
        data, index = self.history
        self.assertEqual(index, 1)
        self.assertEqual(current_state(self.history), "hello")
        self.history = redo(self.history)
        _, index = self.history
        self.assertEqual(index, 2)
        self.assertEqual(current_state(self.history), "hello world")

    def test_redo_many(self):
        self.history = edit(self.history, "hello")
        self.history = edit(self.history, "hello world")
        self.history = undo(self.history)
        data, index = self.history
        self.assertEqual(index, 1)
        self.assertEqual(current_state(self.history), "hello")
        self.history = redo(self.history)
        self.history = redo(self.history)
        self.history = redo(self.history)
        _, index = self.history
        self.assertEqual(index, 2)
        self.assertEqual(current_state(self.history), "hello world")


if __name__ == "__main__":
    unittest.main()
