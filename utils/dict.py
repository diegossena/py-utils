def dict_pick(dict: dict, keys: list[str]):
  return {key: dict[key] for key in keys}


def dict_omit(dict: dict, keys: list[str]):
  return {key: dict[key] for key in dict if key not in keys}
