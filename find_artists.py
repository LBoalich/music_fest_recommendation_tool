from data import camping, non_camping

def find_artists(root_node):
    matching_artists = []
    #Get user input for artist search
    artist_input = input('Type the beggining letters of an artist you are interested in seeing to get a list of possible matches: ').lower()
    # moves through each node referenced from self downwards
    nodes_to_visit = [root_node]
    while len(nodes_to_visit) > 0:
        current_node = nodes_to_visit.pop()
        if current_node.value.lower().startswith(artist_input) and current_node.value not in camping and current_node.value not in non_camping and current_node.value != "Camping" and current_node.value != "Non-Camping" and current_node.value != "Music Festivals":
            matching_artists.append(current_node.value)
        nodes_to_visit += current_node.children
    return set(matching_artists)
