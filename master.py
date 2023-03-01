from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.client import ServerProxy
import string
import sys


workers = {
    'worker-1': ServerProxy("http://localhost:23001/"),
    'worker-2': ServerProxy("http://localhost:23002/")
}

      
def getbylocation(location):
    response = {}
    error = False

    try:
        # Calling RPC functions in either of the workers and recording response
        worker1_result = workers.get('worker-1').getbylocation(location)
        worker2_result = workers.get('worker-2').getbylocation(location)

        # Adding response of both workers and passing up any error response from workers
        response.update(worker1_result["result"])
        if (worker1_result["error"]):
            error = worker1_result["error"]
        response.update(worker2_result["result"])
        if (worker2_result["error"]):
            error = worker2_result["error"]
    except:
        # If error occurs while trying to do any of this, sets error status to True
        error = True

    # Return response to client
    return {
        "error": error,
        "result": response
    }


def getbyname(name):
    response = {}
    error = False

    try:
        # Sorting which worker to call based on name input
        if (ord(name[0]) in range(ord('a'), ord('n'))):
            response.update(workers.get('worker-1').getbyname(name))
        elif (ord(name[0]) in range(ord('n'), ord('z'))):
            response.update(workers.get('worker-2').getbyname(name))
    except:
        # If error occurs while trying to do any of this, sets error status to True
        error = True

    # Return response to client
    return {
        "error": error,
        "result": response
    }
    

def getbyyear(location, year):
    response = {}
    error = False

    try:
        # Calling RPC functions in either of the workers and recording response
        worker1_result = workers.get('worker-1').getbyyear(location, year)
        worker2_result = workers.get('worker-2').getbyyear(location, year)

        # Adding response of both workers and passing up any error response from workers
        response.update(worker1_result["result"])
        if (worker1_result["error"]):
            error = worker1_result["error"]
        response.update(worker2_result["result"])
        if (worker2_result["error"]):
            error = worker2_result["error"]
    except:
        # If error occurs while trying to do any of this, sets error status to True
        error = True

    # Return response to client
    return {
        "error": error,
        "result": response
    }
  

def main():
    # Getting initial port/server info
    port = int(sys.argv[1])
    server = SimpleXMLRPCServer(("localhost", port))
    print(f"Listening on port {port}...")

    # Registering RPC functions and starting server
    server.register_function(getbylocation)
    server.register_function(getbyname)
    server.register_function(getbyyear)
    server.serve_forever()


if __name__ == '__main__':
    main()