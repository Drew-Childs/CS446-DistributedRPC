from xmlrpc.server import SimpleXMLRPCServer
import sys
import json

# Storage of data
data_table = {}


def load_data(group):
    global data_table
    file = open("data-" + group + ".json")
    data_table = json.load(file)


def getbyname(name):
    response = {}
    error = False

    try:
        # searching through dictionary to find name that matches and add it to response
        for item in data_table:
            if (name == item):
                response.update({item : data_table[item]})
    except:
        # If error occurs while trying to do any of this, sets error status to True
        error = True

    # Return response to master
    return {
        'error': error,
        'result': response
    }


def getbylocation(location):
    response = {}
    error = False

    try:
        # Searching through dictionary to find location that matches and add it to response
        for item in data_table:
            if (data_table[item]["location"] == location):
                response.update({item : data_table[item]})
    except:
        # If error occurs while trying to do any of this, sets error status to True
        error = True

    # Return response to master
    return {
        'error': error,
        'result': response
    }


def getbyyear(location, year):
    response = {}
    error = False

    try:
        # Searching through dictionary to find location and year that matches and add it to response
        for item in data_table:
            if (data_table[item]["location"] == location and data_table[item]["year"] == year):
                response.update({item : data_table[item]})
    except:
        # If error occurs while trying to do any of this, sets error status to True
        error = True

    # Return response to master
    return {
        'error': error,
        'result': response
    }


def main():
    # Doing input validation of command line arguments
    if (len(sys.argv) < 3 or (sys.argv[2] != "am" and sys.argv[2] != "nz")):
        print('Usage: worker.py <port> <group: am or nz>')
        sys.exit(0)

    # Initial server setup
    port = int(sys.argv[1])
    group = sys.argv[2]
    server = SimpleXMLRPCServer(("localhost", port))
    print(f"Listening on port {port}...")

    load_data(group)

    # Registering RPC functions and starting server
    server.register_function(getbylocation)
    server.register_function(getbyname)
    server.register_function(getbyyear)
    server.serve_forever()

if __name__ == '__main__':
    main()