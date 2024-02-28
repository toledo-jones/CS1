from typing import Union

# Supported containers:
MAP = {
    'list': list(),
    'dict': dict(),
    'set': set(),
    'tuple': tuple()
}


def create_container(container_type: str) -> Union[list, dict, set, tuple]:
    """
    Creates a container of the specified type
    :param container_type: string indicating which container type to return
    :return: Collection (List, Set, Dict or Tuple) based on the specified type
    """
    return MAP[container_type]


def access_item(item: int,
                container: Union[list, dict, set, tuple]) -> any:
    """
    Access an item in a container

    :param item: index of ? element to be accessed
    :param container: collection to be accessed
    :returns: value or bool if the container is a set 
    """

    # Collection is a Set() which does not support __getitem__
    if isinstance(container, set):
        # Return bool if the item is in the set
        return item in container

    # Collection must be a List, Tuple or Dict, return value at index/key
    container: Union[list, dict, set, tuple]
    return container[item]


def add_item(
        item: any,
        container: Union[list, dict, set, tuple],
        position: int = None
) -> Union[list, dict, set, tuple]:
    # Adds the item differently based on the container type
    match container:

        case list():
            # For type checking only
            container: list

            if position is not None:
                container.insert(position, item)
                return container

            # Add the item to the end in this case
            container.append(item)

            # Add item completed
            return container

        case set():
            container: set

            # Add item to the end of set
            container.add(item)

            return container

        case tuple():
            container: tuple

            new_container = list(container)

            if position is not None:
                new_container.insert(position, item)

            else:
                new_container.append(item)

            container = tuple(new_container)

            return container

        case dict():
            container: dict

            if isinstance(item, tuple):
                if len(item) == 2:
                    container[item[0]] = item[1]
                    return container

            container[item] = None
            return container


def remove_item(
        item: any,
        container: Union[list, dict, set, tuple],
        multi: bool = True
) -> Union[list, dict, set, tuple]:
    # Removes the item differently based on the container type
    match container:

        case list():
            container: list
            occurrences = 0
            for i in container:
                if i == item:
                    container.remove(i)
                    occurrences += 1
                if not multi and occurrences == 1:
                    return container
            return container

        case dict():
            container: dict
            del container[item]
            return container

        case set():
            container: set
            container.remove(item)
            return container

        case tuple():
            container: tuple
            container = list(container)
            container = remove_item(item, container, multi)
            return tuple(container)


def update_item(
        orig_item: any,
        new_item: any,
        container: Union[list, dict, set, tuple],
        multi: bool = True
) -> Union[list, dict, set, tuple]:
    # Update item differently based on condition
    match container:

        case list():
            container: list

            for index, item in enumerate(container):
                if item == orig_item:
                    container[index] = new_item
                    if not multi:
                        return container
            return container

        case dict():
            container: dict

            if isinstance(new_item, tuple):
                if len(new_item) == 2:
                    del container[orig_item]
                    container[new_item[0]] = new_item[1]
                    return container

            container[orig_item] = new_item

            return container

        case set():
            container: set

            container.remove(orig_item)
            container.add(new_item)
            return container

        case tuple():

            return tuple(
                update_item(
                    orig_item,
                    new_item,
                    list(container),
                    multi))


def convert_container(
        container: Union[list, dict, set, tuple],
        container_type: str
) -> Union[list, dict, set, tuple]:

    new_container = create_container(container_type)

    # This actually made me want to puke lol

    match container:
        case list():
            container: list
            match new_container:
                case list():
                    new_container: list
                    return container

                case dict():
                    new_container: dict

                    for item in container:
                        if isinstance(item, tuple):
                            if len(item) == 2:
                                new_container[item[0]] = item[1]
                            else:
                                new_container[item] = None
                        else:
                            new_container[item] = None
                    return new_container

                case set():
                    new_container: set
                    return set(container)

                case tuple():
                    new_container: tuple
                    return tuple(container)

        case dict():
            container: dict
            match new_container:
                case list():
                    new_container: list

                case dict():
                    new_container: dict

                case set():
                    new_container: set

                case tuple():
                    new_container: tuple

        case set():
            container: set
            match new_container:
                case list():
                    new_container: list

                case dict():
                    new_container: dict

                case set():
                    new_container: set

                case tuple():
                    new_container: tuple

        case tuple():
            container: tuple
            match new_container:
                case list():
                    new_container: list

                case dict():
                    new_container: dict

                case set():
                    new_container: set

                case tuple():
                    new_container: tuple



# assert convert_container([1, (2, 'a'), 3, (4, 'b')], 'dict') == \
#        {1: None, 2: 'a', 3: None, 4: 'b'}
# assert convert_container([1, 2, 3, 4], 'set') == {1, 2, 3, 4}
# assert convert_container([1, 2, 3, 4], 'tuple') == \
#        (1, 2, 3, 4)
#
# orig_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
# new_list = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# assert sorted(convert_container(orig_dict, 'list')) == new_list
#
# orig_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
# new_set = {(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')}
# assert convert_container(orig_dict, 'set') == new_set
#
# orig_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
# ref_tuple = ((1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'))
# new_tuple = convert_container(orig_dict, 'tuple')
# assert type(new_tuple) is tuple
# assert tuple(sorted(new_tuple)) == ref_tuple
#
# assert sorted(convert_container({1, 2, 3, 4}, 'list')) == [1, 2, 3, 4]
#
# assert convert_container({1, 2, 3, 4}, 'dict') == \
#        {1: None, 2: None, 3: None, 4: None}
#
# assert convert_container({1, (2, 'a'), 3, (4, 'b')}, 'dict') == \
#        {1: None, 2: 'a', 3: None, 4: 'b'}
#
# new_tuple = convert_container({1, 2, 3, 4}, 'tuple')
# assert type(new_tuple) is tuple
# assert tuple(sorted(new_tuple)) == \
#        (1, 2, 3, 4)
#
# assert convert_container((1, 2, 3, 4), 'list') == \
#        [1, 2, 3, 4]
# assert convert_container((1, 2, 3, 4), 'dict') == \
#        {1: None, 2: None, 3: None, 4: None}
# assert convert_container((1, (2, 'a'), 3, (4, 'b')), 'dict') == \
#        {1: None, 2: 'a', 3: None, 4: 'b'}
# assert convert_container((1, 2, 3, 4), 'set') == {1, 2, 3, 4}