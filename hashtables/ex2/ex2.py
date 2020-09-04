#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    dict = {}
    route = []

    for ticket in tickets: # Fill in dictionary
        if ticket.source not in dict:
            dict[ticket.source] = ticket.destination
            if ticket.source == "NONE": # Find the first route and add to routes
                route.append(ticket.destination)
    
    current = route[0]
    while current is not "NONE":
        route.append(dict[current]) # Call dictionary and retrieve the value/destination of the key/source. (Adds next destination to end of route array)
        current = dict[current] # Sets the destination as current

    return route
