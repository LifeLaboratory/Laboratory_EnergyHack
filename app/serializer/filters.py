def is_denied_action(item):
    denied_actions = [-1, -2]
    return item['to'] in denied_actions


def is_open_program_action(item):
    return item.get('category') == 'open_file'


def is_click_action(item):
    return item.get('category') == 'click'


def is_cycle_action(item):
    return item.get('category') == 'cycle'


def is_save_value_action(item):
    return item.get('category') == 'save_value'


def is_condition_action(item):
    return item.get('category') == 'condition'


def is_amount_receipts(item):
    return item.get('category') == 'amount_receipts'


def is_fill_field(item):
    return item.get('category') == 'fill_field'


def is_category_exists(item):
    return item.get('category')

def is_property_exists(item):
    return 'property' in item