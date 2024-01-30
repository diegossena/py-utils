
def list_move(list: list, oldIndex: int, newIndex: int):
  list.insert(newIndex, list.pop(oldIndex))


def list_split(list: list, chunk_size: int):
  return [list[i:i + chunk_size] for i in range(0, len(list), chunk_size)]


def list_intersection(list1: list, list2: list):
  return [value for value in list1 if value in list2]
