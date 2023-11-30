from typing import Any


class Queue:
    """
    A simple implementation of a queue data structure.
    """

    def __init__(self) -> None:
        """
        Initialize an empty queue.
        """
        self.queue = []

    def enqueue(self, val: Any) -> None:
        """
        Add a value to the back of the queue.

        Parameters:
        - val (Any): The value to be added.
        """
        self.queue = [val] + self.queue

    def dequeue(self) -> None:
        """
        Remove the front element from the queue.
        """
        if self.queue:
            self.queue.pop()

    def front(self) -> Any:
        """
        Get the front element of the queue.

        Returns:
        - Any: The front element.
        """
        if self.queue:
            return self.queue[-1]

    def back(self) -> Any:
        """
        Get the back element of the queue.

        Returns:
        - Any: The back element.
        """
        if self.queue:
            return self.queue[0]

    def is_empty(self) -> bool:
        """
        Check if the queue is empty.

        Returns:
        - bool: True if the queue is empty, False otherwise.
        """
        return not bool(self.queue)

    def __str__(self) -> str:
        """
        Return a string representation of the queue.

        Returns:
        - str: String representation of the queue.
        """
        return str(self.queue)

    def __len__(self) -> int:
        """
        Get the number of elements in the queue.

        Returns:
        - int: The number of elements in the queue.
        """
        return len(self.queue)


# Example usage:
if __name__ == "__main__":
    my_queue = Queue()
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)

    print("Queue:", my_queue)
    print("Front:", my_queue.front())
    print("Back:", my_queue.back())
    print("Is Empty:", my_queue.is_empty())
    print("Queue Length:", len(my_queue))

    my_queue.dequeue()
    print("After Dequeue:", my_queue)
    print("Queue Length:", len(my_queue))
