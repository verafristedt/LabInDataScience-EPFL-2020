

class Node:
    def __init__(self, curr, prev, time, elapsed, visited, parent, trip, walk, arrival):
        self.curr = curr
        self.prev = prev
        self.time = time
        self.elapsed = elapsed
        self.visited = visited
        self.parent = parent
        self.trip = trip
        self.walk = walk
        self.arrival = arrival
        
    def feasible(self, n):
        return self.time <= n.time

    
def transfer_time(trip_1, trip_2):
    if trip_1 is trip_2:
        return 0
    else:
        return 2
    

def reconstructPath(n):
    path = []
    c = n
    
    count = 0
    arr = None
    
    while c is not None:
        d = {'stop': c.curr, 'time': c.time, 'trip': c.trip, 'arrival': arr, 'walk': c.walk}
        arr = c.arrival
        path.append(d)
        c = c.parent
        count += 1
        
    return path


def find_children(network, n, final_arr):
    stop_id = n.curr
    time = n.time
    visited = n.visited
    

    stop = network.getStop(stop_id)
    if stop is None:
        print("Right here")
        return None

    connections = stop.getAllConnections()

    children = []

    for connection in connections:
        timeTable = stop.getTimes(connection)
        if connection is n.prev:
            continue

        f = []

        for entry in timeTable:
            if entry[1] == n.trip:
                if entry[0][1] <= time:
                    f.append(entry)
            else:
                if entry[0][1] + 120 <= time:
                    f.append(entry)

        f.sort(key=lambda tup:tup[0][0])
        if len(f) < 2:
            nodes = f
        else:
            l = len(f)
            nodes = [f[l - 2], f[l - 1]]

        for node in nodes:
            depart_time = node[0][0]
            arrival_time = node[0][1]
            elapsed = final_arr - depart_time
            n_visited = set()
            n_visited.update(visited)
            n_visited.add(connection)
            n_node = Node(curr=connection, 
                          prev = stop_id, 
                          elapsed = elapsed, 
                          trip = node[1], 
                          visited = n_visited, 
                          parent = n, 
                          time = depart_time, 
                          arrival = arrival_time,
                          walk = False)
            children.append(n_node)

    if not n.walk:
        withinWalking = stop.getWalk()
        for connection, walkTime in withinWalking.items():
            elapsed = n.elapsed + (walkTime * 60)
            n_time = time - (walkTime * 60)
            n_visited = set()
            n_visited.update(visited)
            n_visited.add(connection)
            
            n_node = Node(curr = connection, 
                          prev = stop_id,
                          time = n_time, 
                          elapsed = final_arr - n_time,
                          trip = None, 
                          visited = n_visited,
                          parent = n,
                          walk = True, 
                          arrival = None)
            children.append(n_node)
    return children
    
    


def samePath(p1, p2):
    if len(p1) is not len(p2):
        return False
    for i in range(len(p1)):
        n1 = p1[i]
        n2 = p2[i] 
        if (not(n1['stop'] is n2['stop'])) or (not (n1['trip'] is n2['trip'])) or (not(n1['time'] is n2['time'])) or (not(n1['arrival'] is n2['arrival'])):
            if not n1['walk'] == n2['walk']:
                #print('index at: ' + str(i))
                return False
        
    return True


def notIn(path, B):
    for p in B:
        if samePath(path, p):
            return False
        
    return True


