# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from .station import MonitoringStation
from haversine import haversine

def station_by_distance(stations, p):
    station_data = []
    for station in stations:
        station_data += station.name, haversine(station.coord, p)
        tuple_data = [x for x in zip(*[iter(station_data)]*2)]
        tuple_data = sorted_by_key(tuple_data, 1)
    return tuple_data