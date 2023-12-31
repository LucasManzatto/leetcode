# Generated by CodiumAI

import pytest
from structures.linked_list import SinglyLinkedList


class TestLinkedList:
    @pytest.mark.parametrize(
        "initial_values, expected_result",
        [([1, 2, 3], [1, 2, 3]), ("a", ["a"]), [1, [1]]],
    )
    def test_initialize_singly_linked_list_with_single_value(
        self, initial_values, expected_result
    ):
        # Arrange
        linked_list = SinglyLinkedList(initial_values)
        expected_list = SinglyLinkedList(expected_result)

        # Assert
        assert linked_list == expected_list

    @pytest.mark.parametrize(
        "initial_values, value_to_append, expected_result",
        [([1, 2, 3], 4, [1, 2, 3, 4])],
    )
    def test_append_value_to_end_of_linked_list(
        self, initial_values, value_to_append, expected_result
    ):
        # Arrange
        linked_list = SinglyLinkedList(initial_values)
        expected_list = SinglyLinkedList(expected_result)

        # Act
        linked_list.append(value_to_append)

        # Assert
        assert linked_list == expected_list

    @pytest.mark.parametrize(
        "initial_values, value_to_prepend, expected_result",
        [([1, 2, 3], 0, [0, 1, 2, 3]), (["a"], "b", ["b", "a"])],
    )
    def test_prepend_value_to_front_of_linked_list(
        self, initial_values, value_to_prepend, expected_result
    ):
        # Arrange
        linked_list = SinglyLinkedList(initial_values)
        expected_list = SinglyLinkedList(expected_result)

        # Act
        linked_list.push(value_to_prepend)

        # Assert
        assert linked_list == expected_list

    @pytest.mark.parametrize(
        "initial_values, expected_result",
        [([1, 2, 3], 3), (["a", "b", "c"], "c")],
    )
    def test_get_last_node_of_linked_list(self, initial_values, expected_result):
        # Arrange
        linked_list = SinglyLinkedList(initial_values)

        # Act
        result = linked_list.last_node().val

        # Assert
        assert result == expected_result

    @pytest.mark.parametrize(
        "initial_values, expected_result",
        [
            ([1, 2, 3], 2),
            ([1, 2, 3, 4], 3),
            ([1, 2, 3, 4, 5], 3),
            ([1], 1),
            ([1, 2], 2),
        ],
    )
    def test_get_middle_node_of_linked_list(self, initial_values, expected_result):
        # Arrange
        linked_list = SinglyLinkedList(initial_values)

        # Act
        result = linked_list.middle_node().val

        # Assert
        assert result == expected_result

    # Reverse the order of nodes in the linked list
    @pytest.mark.parametrize(
        "initial_values, expected_result",
        [([1, 2, 3], [3, 2, 1]), (["a", "b", "c"], ["c", "b", "a"])],
    )
    def test_reverse_order_of_nodes_in_linked_list(
        self, initial_values, expected_result
    ):
        # Arrange
        linked_list = SinglyLinkedList(initial_values)
        expected_list = SinglyLinkedList(expected_result)

        # Act
        linked_list.reverse()

        # Assert
        assert linked_list == expected_list

    def test_initialize_singly_linked_list_with_none(self):
        # Arrange & Act & Assert
        with pytest.raises(ValueError):
            SinglyLinkedList(None)

    def test_append_none_to_linked_list(self):
        # Arrange
        linked_list = SinglyLinkedList([1, 2, 3])

        # Act & Assert
        with pytest.raises(ValueError):
            linked_list.append(None)

    def test_extend_linked_list_with_non_iterable_value(self):
        # Arrange
        linked_list = SinglyLinkedList([1, 2, 3])

        # Act & Assert
        with pytest.raises(ValueError):
            linked_list.extend(4)

    def test_get_middle_node_of_linked_list_with_cycle(self):
        # Arrange
        linked_list = SinglyLinkedList([1, 2, 3])
        linked_list.last_node().next = linked_list.root

        # Act & Assert
        with pytest.raises(ValueError):
            linked_list.middle_node()

    def test_linked_list_has_cycle(self):
        # Arrange
        linked_list = SinglyLinkedList([1, 2, 3, 4, 5])
        linked_list.last_node().next = linked_list.root

        # Assert
        assert linked_list.has_cycle()

    def test_linked_list_iterable(self):
        # Arrange
        linked_list = SinglyLinkedList([1, 2, 3])
        expected_result = [1, 2, 3]

        # Act
        result = list(linked_list)

        # Assert
        assert result == expected_result

    def test_copy_creates_copy_of_original_linked_list(self):
        # Arrange
        linked_list = SinglyLinkedList([1, 2, 3, 4, 5])

        # Act
        copy_linked_list = linked_list.copy()
        copy_linked_list.append(6)
        # Assert
        assert copy_linked_list != linked_list

    def test_insert_value_at_index_0_in_non_empty_linked_list(self):
        linked_list = SinglyLinkedList([1, 2, 3, 4, 5])
        linked_list.insert(6, 0)
        assert linked_list.to_string() == "[6, 1, 2, 3, 4, 5]"

    # Inserting a value at the end of a non-empty linked list
    def test_insert_value_at_end_of_non_empty_linked_list(self):
        linked_list = SinglyLinkedList([1, 2, 3, 4, 5])
        linked_list.insert(6, len(linked_list))
        assert linked_list.to_string() == "[1, 2, 3, 4, 5, 6]"

    # Inserting a value at a middle index of a non-empty linked list
    def test_insert_value_at_middle_index_of_non_empty_linked_list(self):
        linked_list = SinglyLinkedList([1, 2, 3, 4, 5])
        linked_list.insert(6, 2)
        assert linked_list.to_string() == "[1, 2, 6, 3, 4, 5]"

    # Inserting a value at an index greater than the length of the linked list
    def test_insert_value_at_index_greater_than_length_of_linked_list(self):
        linked_list = SinglyLinkedList([1, 2, 3, 4, 5])
        with pytest.raises(IndexError):
            linked_list.insert(6, len(linked_list) + 1)

    # Inserting a value at a negative index
    def test_insert_value_at_negative_index(self):
        linked_list = SinglyLinkedList([1, 2, 3, 4, 5])
        with pytest.raises(IndexError):
            linked_list.insert(6, -1)

    # Inserting a value at index 0 in an empty linked list
    def test_insert_value_at_index_0_in_empty_linked_list(self):
        linked_list = SinglyLinkedList([])
        expected_list = SinglyLinkedList([1])

        linked_list.insert(1, 0)
        assert linked_list == expected_list

    def test_size_of_linked_list(self):
        linked_list = SinglyLinkedList([])
        expected_value = 1

        linked_list.insert(1, 0)

        assert len(linked_list) == expected_value

        linked_list = SinglyLinkedList([1])
        expected_value = 1

        assert len(linked_list) == expected_value
