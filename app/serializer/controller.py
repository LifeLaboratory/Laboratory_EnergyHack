from app.serializer.filters import *
from app.serializer.view import *


def serialize(data):
    structure = []
    link_data_array = data.get('linkDataArray')
    node_data_array = data.get('nodeDataArray')

    for item in link_data_array:
        if is_denied_action(item):
            continue

        action_key = item.get('to')
        new_item = {"action": get_action_by_id(node_data_array, action_key)}

        action = new_item.get('action')
        nda_item = get_nda_data_by_action(node_data_array, action)

        if not is_action_exists(nda_item):
            continue

        if is_open_program_action(new_item):
            new_item.update(get_open_program_fields(nda_item))

        if is_click_action(nda_item):
            new_item.update(get_click_fields(nda_item))

        if is_cycle_action(nda_item):
            pass

        if is_save_value_action(nda_item):
            new_item.update(get_save_value_fields(nda_item))

        if is_condition_action(nda_item):
            new_item.update(get_condition_fields(nda_item))

        structure.append(new_item)
    print(structure)


if __name__ == '__main__':
    data = get_json()
    serialize(data)
