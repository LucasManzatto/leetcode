import pytest

from structures.queue import Queue


@pytest.fixture
def empty_queue():
    return Queue()


@pytest.fixture
def filled_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    return queue


@pytest.mark.parametrize(
    "enqueue_values, expected_front, expected_back",
    [([1], 1, 1), ([1, 2, 3], 1, 3)],
)
def test_enqueue(empty_queue, enqueue_values, expected_front, expected_back):
    for val in enqueue_values:
        empty_queue.enqueue(val)
    assert empty_queue.front() == expected_front
    assert empty_queue.back() == expected_back


@pytest.mark.parametrize(
    "dequeue_count, expected_front, expected_back",
    [(1, 2, 3), (2, 3, 3), (3, None, None)],
)
def test_dequeue(filled_queue, dequeue_count, expected_front, expected_back):
    for _ in range(dequeue_count):
        filled_queue.dequeue()
    assert filled_queue.front() == expected_front
    assert filled_queue.back() == expected_back


@pytest.mark.parametrize(
    "initial_values, is_empty_result", [([], True), ([1, 2, 3], False), ([1], False)]
)
def test_is_empty(empty_queue, initial_values, is_empty_result):
    for val in initial_values:
        empty_queue.enqueue(val)
    assert empty_queue.is_empty() == is_empty_result


@pytest.mark.parametrize(
    "initial_values, expected_str", [([], "[]"), ([1, 2, 3], "[3, 2, 1]")]
)
def test_str(empty_queue, initial_values, expected_str):
    for val in initial_values:
        empty_queue.enqueue(val)
    assert str(empty_queue) == expected_str


@pytest.mark.parametrize(
    "initial_values, expected_len", [([], 0), ([1, 2, 3], 3), ([1], 1)]
)
def test_len(empty_queue, initial_values, expected_len):
    for val in initial_values:
        empty_queue.enqueue(val)
    assert len(empty_queue) == expected_len
