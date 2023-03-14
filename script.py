from data import *
from Tree_Node import TreeNode
from add_Tree_Node import add_Tree_Node
from festival_type import festival_type
from find_artists import find_artists
from choose_artist import choose_artist
from find_festivals import find_festivals

#create Tree
root_node = TreeNode("Music Festivals")

camping_node = TreeNode('Camping')
camping_node.set_parent(root_node)
root_node.add_child(camping_node)

non_camping_node = TreeNode('Non-Camping')
non_camping_node.set_parent(root_node)
root_node.add_child(non_camping_node)

firefly_node = TreeNode("Firefly Festival")
firefly_node.set_parent(camping_node)
camping_node.add_child(firefly_node)

bonnaroo_node = TreeNode("Bonnaroo")
bonnaroo_node.set_parent(camping_node)
camping_node.add_child(bonnaroo_node)

coachella_node = TreeNode("Coachella")
coachella_node.set_parent(camping_node)
camping_node.add_child(coachella_node)

lollapalooza_node = TreeNode("Lollapalooza")
lollapalooza_node.set_parent(non_camping_node)
non_camping_node.add_child(lollapalooza_node)

shaky_knees_node = TreeNode("Shaky Knees")
shaky_knees_node.set_parent(non_camping_node)
non_camping_node.add_child(shaky_knees_node)

hangout_fest_node = TreeNode("Hangout Fest")
hangout_fest_node.set_parent(non_camping_node)
non_camping_node.add_child(hangout_fest_node)

boston_calling_node = TreeNode("Boston Calling")
boston_calling_node.set_parent(non_camping_node)
non_camping_node.add_child(boston_calling_node)

lightning_in_a_bottle_node = TreeNode("Lightning in a Bottle")
lightning_in_a_bottle_node.set_parent(camping_node)
camping_node.add_child(lightning_in_a_bottle_node)

for artist in firefly:
    add_Tree_Node(artist, firefly_node)
for artist in bonnaroo:
    add_Tree_Node(artist, bonnaroo_node)
for artist in coachella:
    add_Tree_Node(artist, coachella_node)
for artist in lollapalooza:
    add_Tree_Node(artist, lollapalooza_node)
for artist in shaky_knees:
    add_Tree_Node(artist, shaky_knees_node)
for artist in hangout_fest:
    add_Tree_Node(artist, hangout_fest_node)
for artist in boston_calling:
    add_Tree_Node(artist, boston_calling_node)
for artist in lightning_in_a_bottle:
    add_Tree_Node(artist, lightning_in_a_bottle_node)

#Welcome user
print('''       
                      *****************                   
                   ****************  **                       
                ****************     ** 
              **                     ** 
              **                     ** 
              **                     ** 
              **                     ** 
              **                @@@@ **
              **               @@@@@@** 
         @@@@ **               @@@@@@**           
        @@@@@@**                @@@@
        @@@@@@**
         @@@@
         ''')

name = input('Welcome to the Music Festival Recommendation Tool!\nThis program will help you find which festivals your favorite artist is playing at.\nWhat is your name: ')

def run_program(root_node, camping_node, non_camping_node, name):
    #choose if you want to search for camping, non-camping, or both types of festivals
    festival_type_node = festival_type(root_node, camping_node, non_camping_node, name)

    #find matching artists based on user search
    possible_artist_matches = find_artists(festival_type_node)

    #choose artist from matches
    chosen_artist = choose_artist(possible_artist_matches, festival_type_node)

    #find fistivals based on chosen artist and festival type
    find_festivals(festival_type_node, chosen_artist)

def search_quit(root_node, camping_node, non_camping_node, name):
    search_again = input('Do you want to start a new search?  Type "yes" to seach or "no" to quit: ').lower()
    while search_again not in ['yes', 'no']:
        search_again = input('Please type "yes" to search or "no" to quit: ').lower()
    if search_again == 'yes':
        run_program(root_node, camping_node, non_camping_node, name)
        search_quit(root_node, camping_node, non_camping_node, name)
    else:
        print(f'Thank You {name} for using the Music Festival Recommendation Tool!\nHave a wonderful day :)')
        quit()

run_program(root_node, camping_node, non_camping_node, name)
search_quit(root_node, camping_node, non_camping_node, name)
