class Pro:
    def __init__(self, id):
        self.id = id
        self.act = True

class Bully:
    def __init__(self):
        self.TotalProcess = 0
        self.process = []
        self.initializedProcess = None
     
    def initialiseBully(self):
        self.TotalProcess = int(input("Enter the number of processes: "))
        self.process = [Pro(i) for i in range(self.TotalProcess)]
        self.initializedProcess = int(input("Enter the process ID to initiate the election: "))
     
    def Election(self):
        print("Process no " + str(self.process[self.FetchMaximum()].id) + " fails")
        self.process[self.FetchMaximum()].act = False
        print("Election Initiated by", self.initializedProcess)
 
        old = self.initializedProcess
        newer = old + 1
 
        while True:
            if self.process[newer % self.TotalProcess].act:
                print("Process " + str(self.process[old].id) + " passes Election(" + str(self.process[old].id) + ") to " + str(self.process[newer % self.TotalProcess].id))
                old = newer
            newer = (newer + 1) % self.TotalProcess
            if newer == self.initializedProcess:
                break
 
        print("Process " + str(self.process[self.FetchMaximum()].id) + " becomes coordinator")
        coord = self.process[self.FetchMaximum()].id
 
        old = coord
        newer = (old + 1) % self.TotalProcess
        while True:
            if self.process[newer].act:
                print("Process " + str(self.process[old].id) + " passes Coordinator(" + str(coord) + ") message to process " + str(self.process[newer].id))
                old = newer
            newer = (newer + 1) % self.TotalProcess
            if newer == coord:
                print("End Of Election ")
                break
     
    def FetchMaximum(self):
        maxId = -9999
        ind = 0
        for i in range(self.TotalProcess):
            if self.process[i].act and self.process[i].id > maxId:
                maxId = self.process[i].id
                ind = i
        return ind

def main():
    object = Bully()
    object.initialiseBully()
    object.Election()
 
if __name__ == "__main__":
    main()
