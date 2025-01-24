import pickle
import sys
import json

with open(sys.argv[1], "rb") as f:
    stations_loc = pickle.load(f)
print(json.dumps(stations_loc, indent=2).encode().decode("unicode-escape"))
