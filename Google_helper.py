
"""
This module is used to call the Google maps API to find travel distances/times and compute the polyline between waypoints for visualization purposes.

Since we only have so many API calls in our free quota, this was done with efficiency in mind.

Your API key must be supplied in the function calls, please do not modify this file directly.

Author: Wesley
"""
from datetime import datetime
import time
import responses
import googlemaps
import numpy as np
import polyline

"""
This calls the Google Maps Distance Matrix API on all pairwise combinations of a supplied list of M addresses, and computes an MxM matrix for distances and times.

Input: List of addresses

Output: Distance Matrix, Time Matrix
"""
def getGoogleTimeDistance(addresses, api_key):
    gmaps = googlemaps.Client(key=api_key)

    curDate = datetime.now()

    time_matrix = np.array([[0] * len(addresses)] * len(addresses))
    distance_matrix = np.array([[0] * len(addresses)] * len(addresses))

    # Iterate through all possible address combinations.
    for i in range(0, len(addresses)):
        for j in range(0, len(addresses)):

            # Do not calculate distance for the same address
            if i == j:
                continue
           
            # Call Google API and get response.
            result = gmaps.distance_matrix(addresses[i], addresses[j], mode='driving', units='metric',traffic_model='best_guess', departure_time=curDate)

            # Index to relevant part of response JSON File.
            curElement = result['rows'][0]['elements'][0]

            # Update matrices
            distance_matrix[i][j] = curElement['distance']['value']
            time_matrix[i][j] = curElement['duration']['value']

    return time_matrix, distance_matrix

"""
This calls the Google Directions API to get the polyline between each sequential pair of waypoints in a supplied list of addresses. They are then combined into a single polyline for the run.

It is done this way because the Google Directions API finds the optimum route between two points and is not capable of doing so with a large number of waypoints.

Uses the polyline Python library.

Input: A list of addreses that corresponds to the optimum route.

Output: A list of latitude/longitude tuples used to form the polyline.
"""
def getPolyline(addresses, api_key):
    gmaps = googlemaps.Client(key=api_key)
    curDate = datetime.now()

    polyline_coords = []
    for i in range(0, len(addresses) - 1):
        result = gmaps.directions(origin = addresses[i], destination = addresses[i+1], mode='driving',units= 'metric', traffic_model='best_guess', departure_time = curDate)

        for x in result[0]['legs'][0]['steps']:
            polyline_coords.extend(polyline.decode(x['polyline']['points']))

    return polyline_coords