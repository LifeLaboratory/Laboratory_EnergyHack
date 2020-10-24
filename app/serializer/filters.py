def is_denied_action(item):
    denied_actions = [-1, -2]
    return item['to'] in denied_actions


def is_open_program_action(item):
    return item.get('action') == 'open_file'


def is_click_action(item):
    return item.get('action') == 'click'


def is_cycle_action(item):
    return item.get('action') == 'cycle'


def is_save_value_action(item):
    return item.get('action') == 'save_value'


def is_condition_action(item):
    return item.get('action') == 'condition'


def is_amount_receipts(item):
    return item.get('action') == 'amount_receipts'


def is_action_exists(item):
    return item.get('action')
