class FlatIterator:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists  # Сохраняем список списков
        self.outer_index = 0  # Индекс для внешнего списка
        self.inner_index = 0  # Индекс для внутреннего списка

    def __iter__(self):
        return self

    def __next__(self):
        # Проходим через все вложенные списки
        while self.outer_index < len(self.list_of_lists):
            inner_list = self.list_of_lists[self.outer_index]
            if self.inner_index < len(inner_list):
                item = inner_list[self.inner_index]
                self.inner_index += 1
                return item
            else:
                # Если внутренний список закончен, переходим к следующему внешнему списку
                self.outer_index += 1
                self.inner_index = 0

        # Если все элементы перебраны, возбуждаем StopIteration
        raise StopIteration


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
