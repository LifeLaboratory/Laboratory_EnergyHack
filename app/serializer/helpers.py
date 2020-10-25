import json
from app.serializer.filters import *


def get_json():
    with open('data/example.json', 'r') as f:
        return json.loads(f.read())


def get_nda_data_by_action(nda, action_id):
    for item in nda:
        if item.get('key') == action_id:
            return item


def get_property(nda_item, key):
    if is_property_exists(nda_item):
        item_property = nda_item.get('property')
        return item_property.get(key)


def get_action_by_id(node_data_array, category_id):
    nda_key = node_data_array
    for item in nda_key:
        if category_id == item.get('key'):
            return item['category']


def get_graph_route(link_data_array):
    operation = {}
    for item in link_data_array:
        key = item.get('from')
        value = item.get('to')
        operation[key] = value

    position = operation[-1]
    result_sort = [position]
    while operation[position] != -2:
        position = operation[position]
        result_sort.append(position)
    return result_sort

