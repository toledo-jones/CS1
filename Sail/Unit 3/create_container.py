from typing import Iterable


def create_container(container_type: str) -> any:
    """
    Creates a container of the specificied type
    :param: container_type: string to turn into a container type
    """
    
    # Supported containers: 
    map = {
        'list': list(),
        'dict': dict(), 
        'set': set(), 
        'tuple': tuple()
    }
    
    # Return relevant container
    return map[container_type]

def access_item(item: any,
                container: Iterable) -> any:
    """
    Access an item in a container

    :param: item: index of ? element to be accessed 
    :param: container: iterable which 
    :returns: value or bool if the container is a set 
    """

    match container:
        case 'list':
            # Element under the item index is returned:
            
        case 'dict':
            pass
        case 'set':
            pass
        case 'tuple': 
            pass