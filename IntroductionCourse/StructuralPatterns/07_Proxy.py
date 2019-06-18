import time


class Producer:
    """Define the 'resource-intensive' object to instantiate"""
    def produce(self):
        print("Producer is working hard!")

    def meet(self):
        print("Producer has time to meet you")


class Proxy:

    """Define the 'relatively less resource-intensive' proxy to instantiate as a middleman"""

    def __init__(self):
        self.occupied = 'No'
        self.producer = None

    def produce(self):
        """Check if producer is available"""

        print("Artist checking if Producer is available...")

        if self.occupied == "No":
            self.producer = Producer()
            time.sleep(2)
            self.producer.meet()
        else:
            time.sleep(2)
            print("Producer is busy")

#Instantiate a Proxy

p = Proxy()

p.produce()

#Change the state to 'occupied'
p.occupied = 'yes'

p.produce()