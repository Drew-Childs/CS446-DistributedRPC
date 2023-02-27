from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.client import ServerProxy
import sys


# TODO - figure out way to schedule which worker gets what task
#      - comment code
#      - add error handling (will need to set up default response)

workers = {
    'worker-1': ServerProxy("http://localhost:23001/"),
    'worker-2': ServerProxy("http://localhost:23002/")
}
      
def getbylocation(location):
    # TODO
    return workers.get('worker-1').getbylocation("Testing")


def getbyname(name):
    # TODO
    return workers.get('worker-1').getbyname("Hello")

def getbyyear(location, year):
    # TODO
    return workers.get('worker-1').getbyyear("World", "!") 

def main():
    port = 23000
    server = SimpleXMLRPCServer(("localhost", port))
    print(f"Listening on port {port}...")

    # TODO: register RPC functions
    server.register_function(getbylocation)
    server.register_function(getbyname)
    server.register_function(getbyyear)
    server.serve_forever()


if __name__ == '__main__':
    main()