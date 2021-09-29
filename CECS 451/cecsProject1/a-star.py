# Assignment 1: A * Algorithm
# Alex Banh

# Import these statements so we can take in arguments from the command line
import sys


# Take in the starting city from the command line as a global variable
STARTING_CITY = sys.argv

# Take the values in to make it a global graph
file1 = open("map.txt", "r")
file2 = open("distances.txt", "r")


# Take in the distance file and make a graph from it
def make_distance_graph():
    # Make graph
    g = {}
    # Write into the graph from the text file
    with open("distances.txt", "r") as file:
        # For every line
        for line in file:
            # Split the value at the '-'
            line = line.strip().split("-")
            # Remove whitespace
            node = line[0].strip()
            # Turn the number from a string into an int
            sld = int(line[1].strip())
            # Add to array
            g[node] = sld
        # Return the array of distances from Bucharest as the crow flies
        return g


# Make the graph of a list of list while hoping the distance values
def make_map_graph():
    # Make graph
    g = {}
    # Make graph to hold sub distances from the file
    sub_dist = {}
    with open("map.txt", "r") as file:
        # For each of the lines in the text file
        for line in file:
            # Split value at '-'
            line = line.strip().split('-')
            # Store the name of the city
            city_name = line.pop(0)
            # Make a new graph that has stores the distance from city_name
            # Of each of the cities it is directly connected to
            node = line[0].strip().split(',')
            for length in node:
                # Separate the name of the city from the distance at the '(' after removing the ')'
                location_distance = length.replace(')', '').split('(')
                # Store the name of the city
                location_name = location_distance.pop(0)
                # Turn the number from a string to an int
                distance_value = int(location_distance[0])
                # Set the location_name's distance from city_name as the distance_value
                sub_dist[location_name] = distance_value
            # Store the each of the cities and the distance from it for the current city, city_name
            g[city_name] = sub_dist
            # Clear it for the next city
            sub_dist = {}
        # Return the map of the city as a graph
        return g


# Create global variables that hold the map
GRAPH_DISTANCE = make_distance_graph()
GRAPH_MAP = make_map_graph()


# A star algorithm
def a_star_algorithm(start, end):
    """
        Return List of tuples as a path from your desired location to Bucharest
        :param start - starting town
        :param end - ending town
        :return Heuristic value, path for optimal travel
    """
    # Only import the PriorityQueue() function to save memory/ not have to import the whole library
    # You have to use a Priority Queue for this cause it will automatically move the
    # Queue stack that has the lowest heuristic value to the front
    # The lowest heuristic value is the most efficient and what is measured by the A star algorithm
    from queue import PriorityQueue
    # Create a priority queue and one empty queue of the distances of visited towns by the crow flies
    queue = PriorityQueue()
    visited = {}
    # Add the first value to the priority queue
    # 1st is the distance from first Node to final destination by the crow flies
    # 2nd is the current distance we have travelled
    # 3rd is where we are at currently
    # 4th is an array storing where we went in order
    # Ex) From the example this is how it is stored (Mehadia)
    # priority_queue: { (241, 0, Mehadia, [Mehadia]) }
    queue.put((GRAPH_DISTANCE[start], 0, start, [start]))
    # Add overhead distances to the visited graph
    # Ex) visited places distance by the crow flies
    # visited['Mehadia'] = [241]
    visited[start] = GRAPH_DISTANCE[start]
    # Looping algorithm that returns the path and distance travelled while the priority queue still has values
    while not queue.empty():
        # Basically this sets the variables to what is in the queue
        # From the example with Mehadia - This is the only value in our queue
        # queue: { (241, 0, Mehadia, [Mehadia]) }
        # heurstic = 241, cost = 0, vertex = Mehadia, path = [Mehadia]
        # declared all on one line to save space
        (heuristic_score, distance, vertex, path) = queue.get()
        # Create a view of all the towns that are connected to our current town
        next_nodes = GRAPH_MAP[vertex].keys()
        # When we get to the final node, Bucharest
        if vertex == end:
            # Returns the values for the example Mehadia
            # heuristic = 434, path = ['Mehadia', 'Dobreta', 'Craiova', 'Pitesti', 'Bucharest']
            return distance, path
        # for each of the connected nodes in the next_nodes view, we add
        for connected_nodes in next_nodes:
            # Keep a running total of the distance you travelled
            current_distance_traveled = distance + GRAPH_MAP[vertex][connected_nodes]
            # Keep a running total of the heuristic score
            heuristic_score = current_distance_traveled + GRAPH_DISTANCE[connected_nodes]
            # Add the node to queue if the node seen by the view isn't already part of the visited list
            # OR
            # The node's heuristic score that is stored is greater or equal to the current heuristic score for it
            # This is to check every connection to the city
            if connected_nodes not in visited or visited[connected_nodes] >= heuristic_score:
                # Set the connected node that is seen by the view to the heuristic score
                # Do this every time, it assigns it for the first one from 0
                # OR
                # It changes the current value to the lesser or equal value that is stored
                visited[connected_nodes] = heuristic_score
                # Add it to the queue to go through
                # EX) 1st part of Mediha
                # Adding this to the queue
                # (314, 70, 'Lugoj', [Mediha, Lugoj])
                queue.put((heuristic_score, current_distance_traveled, connected_nodes, path + [connected_nodes]))


def main():
    # Don't store the name of the script (a-star.py)
    arguments_passed = STARTING_CITY[1:]
    # Take the name out of the list and turn it into a string
    name_of_city = str(arguments_passed.pop())
    # End destination
    end = 'Bucharest'

    # If the city inputted is not in the list *CASE SENSITIVE*
    if name_of_city not in GRAPH_MAP:
        print('Not a city on the station')
    # Use a_star_algorithm() to to find the shortest distance
    else:
        print('From city:', name_of_city)
        print('To city: Bucharest')
        # Store the total distance into a distance variable and the optimal route into a List
        total_distance, optimal_path = a_star_algorithm(name_of_city, end)
        # Formatting stuff
        print('Best Route: {}'.format(' - '.join(optimal_path)))
        print('Total Distance:', total_distance)

    # Close the text files
    file1.close()
    file2.close()


if __name__ == '__main__':
    main()
