from floodsystem.geo import station_by_distance
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
from haversine import haversine

list = build_station_list() 

def test_call():
    ordered = []
    p = (0,0)
    ordered = station_by_distance(list, p)

def test_order():
    ordered = []
    p = (0,0)
    ordered = station_by_distance(list, p)
    i = 1
    sub = 0 
    while i < (len(ordered) -1):
        if(ordered[i][1] > ordered[i - 1][1]):
            sub = 1
        i += 1
    assert sub == 1

def test_distance():
    in_distance = []
    in_distance = stations_within_radius(list, (52.2053, 0.1218), 10)
    everything_good = True
    if 'Boscadjack' in in_distance:
        everything_good = False
    assert everything_good == True
