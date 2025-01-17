from app.serializer.filters import *
from app.serializer.view import *


def serialize(data):
    structure = []
    link_data_array = data.get('linkDataArray')
    node_data_array = data.get('nodeDataArray')

    for action_key in get_graph_route(link_data_array):
        if is_denied_action(action_key):
            continue

        new_item = {"category": get_action_by_id(node_data_array, action_key)}
        nda_item = get_nda_data_by_action(node_data_array, action_key)

        if not is_category_exists(nda_item):
            continue

        if is_open_program_action(new_item):
            new_item.update(get_open_program_props(nda_item))

        if is_click_action(nda_item):
            new_item.update(get_click_props(nda_item))

        if is_cycle_action(nda_item):
            pass

        if is_save_value_action(nda_item):
            new_item.update(get_fill_field_props(nda_item))

        if is_condition_action(nda_item):
            new_item.update(get_condition_props(nda_item))

        if is_fill_field(nda_item):
            new_item.update(get_fill_field_props(nda_item))

        structure.append(new_item)
    return structure


if __name__ == '__main__':
    data = get_json()
    serialize(data)
