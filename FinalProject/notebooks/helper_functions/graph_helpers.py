import math


class Stop:
    def __init__(self, ID, lat, lon, numInterval):
        self.id = ID
        self.lat = lat
        self.lon = lon
        self.connections = {}
        self.walking = {}
        self.numInterval = numInterval
        self.probs = [(0, 0) for x in range(numInterval)]
    
    def addConnection(self, conn, times, tripID):
        if conn in self.connections.keys():
            self.connections[conn].append((times, tripID))
        else:
            #print('hi')
            self.connections[conn] = [(times, tripID)]
            
    def setTimes(self, conn, times):
        self.connections[conn] = times
    
    def removeEdge(self, conn, times, tripID):
        if conn in self.connections.keys():
            ind = -1
            for i in range(len(self.connections[conn])):
                if self.connections[conn][i][1] == tripID:
                    ind = i
            if ind == -1:
                print("trip not found")
            self.connections[conn].pop(ind)
        else:
            print("connection not found")
            
    def removeConnection(self, conn):
        self.connections[conn] = []
    
    def toString(self):
        res = '\t stop ' + str(self.id) + ": \n"
        for key, val in self.connections:
            res += '\t \t ' + key + 'at times ' + val.toString()
        return res
    
    def walkTo(self, conn, walkTime):
        if conn in self.walking.keys():
            return
        else:
            self.walking[conn] = walkTime
            
    def getWalk(self):
        return self.walking
    
    def addProbList(self, probs):
        if(len(probs) != self.numInterval):
            print("length mismatch")
        else:
            self.probs = probs
    def addProb(self, index, mean, std):
        if(index >= self.numInterval):
            print("index out of bound")
        else:
            self.probs[index] = (mean, std)
            
    def getProbList(self):
        return self.probs
    
    def getProb(self, index):
        if(index >= self.numInterval):
            print("index out of bound")
        else:
            return self.probs[index]
    
    def getAllConnections(self):
        return self.connections.keys()
    def getTimes(self, conn):
        if conn not in self.connections.keys():
            print("Connections not found")
            return None
        else:
            return self.connections[conn]
    def getLoc(self):
        return self.lat, self.lon

    def getID(self):
        return self.id
    
    """Need to implement all the getters"""
    

    
class Network:
    def __init__(self, numInterval):
        self.stops = {}
        self.numStops = 0
        self.numInterval = numInterval
        
    def isIn(self, ID):
        if ID in self.stops:
            return True
        else:
            return False
        
    def addStop(self, ID, lat, lon):
        self.numStops += 1
        newStop = Stop(ID, lat, lon, self.numInterval)
        self.stops[ID] = newStop
        return newStop
    
    def getStop(self, ID):
        if ID in self.stops.keys():
            return self.stops[ID]
        else:
            print('stop not found ' + str(ID))
            print(ID)
            return None
        
    def getAllTime(self, s, t):
        return self.stops[s].getTimes(t)
    
    def setTime(self, s, t, times):
        self.stops[s].setTimes(t, times)
        
    def addProbList(self, stop, probs):
        self.stops[stop].addProbList(probs)
    
    def addProb(self, stop, mean, std):
        self.stops[stop].addProb(mean, std)
    
    
    def addEdge(self, source, dest, time, tripID):
        self.stops[source].addConnection(dest, time, tripID)
        
    def addWalkEdge(self, source, dest, walkTime):
        self.stops[source].walkTo(dest, walkTime)
        
    def toString(self):
        res = 'Number of stops: ' + str(self.numStops) + '\n'
        for key, val in self.stops:
            res += 'Stop ' + key + ' connectecd to: ' + val.toString()
            
    def removeConnection(self, s, t):
        self.stops[s].removeConnection(t)
            
    def removeEdge(self, s, t, time, tripID):
        self.stops[s].removeEdge(t, time, tripID)
    
    def getAllStops(self):
        return self.stops.keys()
    def getNumStop(self):
        return self.numStops
    

def isFullTrip(seq):
    for i in range(len(seq) - 1):
        if int(seq[i + 1]) - int(seq[i]) is not 1:
            return False
    return True


def all_same_length(stop, seq, arr, dept):
    return (stop == seq) and (seq == arr) and (arr == dept)


def calc_dist(lat_1, lat_2, lon_1, lon_2):
    R = 6371 
    dLat = math.radians(lat_1 - lat_2)
    dLon = math.radians(lon_1 - lon_2)
    a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(math.radians(lat_2)) \
        * math.cos(math.radians(lat_1)) * math.sin(dLon/2) * math.sin(dLon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c
    return d * 1000