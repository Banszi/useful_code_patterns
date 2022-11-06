from typing import Generator


def make_list_flat(non_flat_list: list) -> Generator:
    '''
        Function convert a non-flat list into one dimension flat list
    '''
    for item in non_flat_list:
        # Check if item in list is iterable
        if hasattr(item, '__iter__'):
            # Recurrence - put here iterable item into the same function
            yield from make_list_flat(item)
        else:
            yield item


if __name__ == '__main__':
    example_non_flat_list = [1, 2, [3, 4], 5, [6, [7, 8, [9]]]]
    flat_list_generator = make_list_flat(example_non_flat_list)

    # Convert generator into list
    flat_list = list(flat_list_generator)
    print(flat_list)