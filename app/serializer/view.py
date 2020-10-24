from app.serializer.helpers import *


def get_open_program_fields(nda_item):
    data = get_field_from_nda(nda_item, 'file_path')
    return {'file_path': data}


def get_click_fields(nda_item):
    return {'object': get_field_from_nda(nda_item, 'object')}


def get_save_value_fields(nda_item):
    return {
        'object': get_field_from_nda(nda_item, 'object'),
        'value': get_field_from_nda(nda_item, 'value'),
        'source': get_field_from_nda(nda_item, 'source')
    }


def get_condition_fields(nda_item):
    return {
        "value": get_field_from_nda(nda_item, 'value')
    }

# def get_cycle_fields(nda_item):
#     data = {
#         'object': get_field_from_nda(nda_item, 'object'),
#         'for': generate_child_steps(nda)
#     }
#     return data