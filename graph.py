from vertex import Vertex

class Graph:
  def __init__(self):
    self.graph_dict = {}

  def add_vertex(self, node):
    self.graph_dict[node.value] = node

  def add_edge(self, from_node, to_node, weight = 0):
    self.graph_dict[from_node.value].add_edge(to_node.value, weight)
    self.graph_dict[to_node.value].add_edge(from_node.value, weight)

  def explore(self):
    print("Exploring the graph....\n")
    #FILL IN EXPLORE METHOD BELOW
    current_room = "entrance"
    path_total = 0
    print("\nStarting off at the {0}\n".format(current_room))
    while current_room != "treasure room":
      node = self.graph_dict[current_room]
      for connected_room, weight in node.edges.items():
        key = connected_room[0]
        print("enter {0} for {1}: {2} cost".format(key, connected_room, weight))
        valid_choices = [room[0] for room in node.edges.keys()]
        print("\nYou have accumulated: {0} cost".format(path_total))
        choice = input("\nWhich room do you move to? ")
        if choice not in valid_choices:
          print("please select from these letters: {0}".format(valid_choices))
        else:
          for room in node.edges.keys():
            if choice == room[0]:
              current_room = room
              path_total +=node.edges[room]
          print("\n*** You have selected: {0} ***\n".format(current_room))
    print("Made it to the treasure room with {0} cost".format(path_total))
