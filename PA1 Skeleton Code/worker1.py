from xmlrpc.server import SimpleXMLRPCServer
import sys

# Storage of data
data_table = {}


def load_data(group):
    # TODO load data based which portion it handles (am or nz)
    pass


def getbyname(name):
    # TODO
    return {
        'error': False,
        'result': [name]
    }

def getbylocation(location):
    # TODO
    return {
        'error': False,
        'result': [location]
    }

def getbyyear(location, year):
    # TODO
    return {
        'error': False,
        'result': [location, year]
    }

def main():
    port = 23001
    server = SimpleXMLRPCServer(("localhost", port))
    print(f"Listening on port {port}...")

    # TODO register RPC functions
    server.register_function(getbylocation)
    server.register_function(getbyname)
    server.register_function(getbyyear)
    server.serve_forever()

if __name__ == '__main__':
    main()