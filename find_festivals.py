def find_festivals(starting_node, artist_choice):
    matching_festivals = []
    nodes_to_visit = [starting_node]
    while len(nodes_to_visit) > 0:
        current_node = nodes_to_visit.pop()
        nodes_to_visit += current_node.children
        if current_node.value.lower() == artist_choice:
            matching_festivals.append(current_node.get_parent().value)
    print(f'{artist_choice.title()} will be playing at the following festivals:')
    print('\n'.join(matching_festivals))
