def convert_tuple(list_dicts: list[dict]) -> tuple:
    return tuple((dict_.get('id'), dict_.get('name'),) for dict_ in list_dicts)
