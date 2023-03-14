def festival_type(root_node, camping_node, non_camping_node, name):
    current_node = root_node
    camping_non_camping = input(f'{name}, if you want to search for camping festivals only, enter "c".\nIf you want to search for non-camping festivals, enter "n".\nOr you can enter "b" to search both types of festivals.\nPlease enter "c", "n", or "b": ').lower()
    while camping_non_camping not in ['c', 'n', 'b']:
        camping_non_camping = input('Please enter either "c", "n", or "b": ').lower()
    if camping_non_camping == 'c':
        current_node = camping_node
    elif camping_non_camping == 'n':
        current_node = non_camping_node
    return current_node