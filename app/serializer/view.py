from app.serializer.helpers import *


def get_open_program_fields(nda_item):
    data = get_property(nda_item, 'file_path')
    return {'file_path': data}


def get_click_fields(nda_item):
    return {'object': get_property(nda_item, 'object')}


def get_fill_field_fields(nda_item):
    object = get_property(nda_item, 'object')
    value = get_property(nda_item, 'value')
    source = get_property(nda_item, 'source')
    data = {'object': object}
    if value:
        data.update({'value': value})

    if source:
        data.update({'source': source})
    return data


def get_condition_fields(nda_item):
    return {
        "value": get_property(nda_item, 'value')
    }

# def get_cycle_fields(nda_item):
#     data = {
#         'object': get_field_from_nda(nda_item, 'object'),
#         'for': generate_child_steps(nda)
#     }
#     return data