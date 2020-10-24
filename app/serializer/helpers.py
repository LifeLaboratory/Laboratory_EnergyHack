import json


def get_json():
    with open('data/example.json', 'r') as f:
        return json.loads(f.read())


def get_nda_data_by_action(nda, action):
    for item in nda:
        if item.get('action') == action:
            return item


def get_field_from_nda(nda_item, key):
    return nda_item.get(key)


def get_action_by_id(node_data_array, action_id):
    nda_key = node_data_array
    for item in nda_key:
        if action_id == item.get('key'):
            return item['action']