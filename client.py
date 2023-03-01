import xmlrpc.client
import sys

master_port = int(sys.argv[1])
with xmlrpc.client.ServerProxy(f"http://localhost:{master_port}/") as proxy:
    # Preparing RPC call for searching by name
    name = 'xander'
    print(f'Client => Asking for person with {name}')
    result = proxy.getbyname(name)
    print(result)
    print()

    # Preparing RPC call for searching by location
    location = 'Kansas City'
    print(f'Client => Asking for person lived at {location}')
    result = proxy.getbylocation(location)
    print(result)
    print()

    # Preparing RPC call for searching by location and year
    location = 'New York City'
    year = 2002
    print(f'Client => Asking for person lived in {location} in {year}')
    result = proxy.getbyyear(location, year)  
    print(result)
    print()