from find_artists import find_artists

def choose_artist(matching_artists, festival_type_node):
    artist_string = '\n'.join(matching_artists).title()

    if len(matching_artists) == 0:
        search_again = input("No artist matched your search.\nType 'yes' to search for a different artist or type 'no' to quit: ").lower()
        while search_again not in ['yes', 'no']:
            search_again = input("Please type either 'yes' or 'no': ").lower()
        if search_again == 'yes':
           return choose_artist(find_artists(festival_type_node), festival_type_node)
        else:
            print('Thank you for using the Music Festival Recommendation Tool!\nHave a wonderful day :)')
            quit()
    else:
        pick_or_search = input(f'The following artists matched your search:\n{artist_string}\nDo you want to pick an artist from this list or search again?\nType "pick" to choose from this list or type "search" to search again: ').lower()

        while pick_or_search not in ['pick', 'search']:
            pick_or_search = input('Please type either "pick", or "search": ').lower()
        if pick_or_search == 'pick':
            artist_choice = input(f'Please type one of the following artists to see which festivals they will be performaing at.\n{artist_string}\n: ').lower()
            while artist_choice not in list(map(str.lower, matching_artists)):
                artist_choice = input(f'Please type one of the following artists:\n{artist_string}\n: ').lower()
            return artist_choice
        else:
             return choose_artist(find_artists(festival_type_node), festival_type_node)
