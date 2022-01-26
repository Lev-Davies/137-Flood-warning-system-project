from floodsystem.geo import station_by_distance
from floodsystem.stationdata import build_station_list
from haversine import haversine

def test_call():
    ordered = []
    list = build_station_list()
    p = (0,0)
    ordered = station_by_distance(list, p)

def test_order():
    ordered = []
    list = build_station_list()
    p = (0,0)
    ordered = station_by_distance(list, p)
    i = 1
    sub = 0 
    while i < (len(ordered) -1):
        if(ordered[i][1] > ordered[i - 1][1]):
            sub = 1
        i += 1
    assert sub == 1
