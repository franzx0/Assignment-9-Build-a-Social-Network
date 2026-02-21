class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
    '''

    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        self.friends.append(friend)


class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''

    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name in self.people:
            print(f"{name} already exists in the network!")
        else:
            self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people and person2_name not in self.people:
            print(f"Friendship not created. {person1_name} and {person2_name} don't exist!")
        elif person1_name not in self.people:
            print(f"Friendship not created. {person1_name} doesn't exist!")
        elif person2_name not in self.people:
            print(f"Friendship not created. {person2_name} doesn't exist!")
        else:
            person1 = self.people[person1_name]
            person2 = self.people[person2_name]
            person1.add_friend(person2)
            person2.add_friend(person1)

    def print_network(self):
        for name, person in self.people.items():
            friends_names = ", ".join([friend.name for friend in person.friends])
            print(f"{name} is friends with: {friends_names}")


# Test
network = SocialNetwork()


network.add_person("Alex")
network.add_person("Jordan")
print(network.people)
network.add_person("Morgan")
network.add_person("Taylor")
network.add_person("Casey")
network.add_person("Riley")

# Test duplicate
network.add_person("Alex")


network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")
network.add_friendship("Jordan", "Johnny")  # "Friendship not created. Johnny doesn't exist!"
network.add_friendship("Morgan", "Casey")
network.add_friendship("Taylor", "Riley")
network.add_friendship("Casey", "Riley")
network.add_friendship("Morgan", "Riley")
network.add_friendship("Alex", "Taylor")

network.print_network()

'''
Alex is friends with: Jordan, Morgan, Taylor
Jordan is friends with: Alex, Taylor
Morgan is friends with: Alex, Casey, Riley
Taylor is friends with: Jordan, Riley, Alex
Casey is friends with: Morgan, Riley
Riley is friends with: Taylor, Casey, Morgan
'''

'''
DESIGN MEMO

The ideal type of representation to use in modeling a social network is the use of graphs. It is natural that they represent the entire relationship energy - people are the nodes, friends are the edges. Relationships traversal is always two-way thus, in case Alex spends time with Jordan, Jordan automatically spends time with Alex, just, as the case is with an undirected graph. The plus graphs are very nice to scale as new people and connections appear, and one does not necessitate a rearrignment of the entire graph.

The simple list would not achieve the goal since, as much as you can store Person objects in the list, there is no internal mechanism that you can use to chart their connections. Each time you wanted to know who to contact or who he or she was friends with you would have to crawl the whole list, and that would constitute O(n) lookups. And a tree? Nor is it so great; trees force you into some narrow parent-children structure, i.e. each node (except the root) has one parent. With social networking where people can have masses of mutual pals and no obvious parent, trees do not cope with many-to-many or many-to-many relationships.

Here, then we are using an adjacency list a dict of Person objects in which the elements of the dict contain a list of friends. It is a compromise between speed and easiness. O (1 ) O (1 ) is added due to dictionary hashing. The cost of making a new friendship is also O(1) since we will simply push a name in the list. To print the entire network, us will cost O(n + e): each word in the network is touched by us once and also there exists the edges which will be touched.

The negative one is that to examine whether two individuals are already friends, one has to traverse through friend list- O(d) where d is the degree of the node. Switching to a set would bring that down to O(1) though sets lose order which may be of an issue to you depending on your needs of order of insertion. A list of clean and good enough will suffice in this project.
'''
