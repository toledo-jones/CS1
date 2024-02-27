from typing import Collection, Sequence

# Supported containers:
MAP = {
    'list': list(),
    'dict': dict(),
    'set': set(),
    'tuple': tuple()
}


def create_container(container_type: str) -> Collection:
    """
    Creates a container of the specified type
    :param container_type: string indicating which container type to return
    :return: Collection (List, Set, Dict or Tuple) based on the specified type
    """
    return MAP[container_type]


def access_item(item: int,
                container: Collection) -> any:
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
    container: Sequence
    return container[item]


def add_item(
        item: any,
        container: Collection,
        position: int = None
) -> Collection:
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
        container: Collection,
        multi: bool = True
) -> Collection:
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
        container: Collection,
        multi: bool = True
) -> Collection:

    # Update item differently based on condition
    match container:

        case list():
            container: list

        case dict():
            container: dict

        case set():
            container: set

        case tuple():
            container: tuple
