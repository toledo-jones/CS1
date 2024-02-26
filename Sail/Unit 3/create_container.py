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
        position: int = None) -> Collection:

    # Adds the item differently based on the container type
    match container:

        case list():
            # For type checking only
            container: list

            # Add the item to the end in this case
            container.append(item)

            # Add item completed
            return container

        case set():
            container: set

        case tuple():
            container: tuple

        case dict():
            container: dict
