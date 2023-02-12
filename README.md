# uOttahack 5: Innovapost Challenge
By David Gayowsky, Alfa Budiman, Wesley Howe, and Jordan Lipson

To optimize Innovapost's delivery routes, we have created an algorithm to find the best way to divide deliveries between mail trucks and the fastest route for each of them, factoring in traffic, accidents, road closures, and weather conditions.

ShipPy: Ship faster with ShipPy - your optimal destination awaits!

## How does it work?
Let's say Innovapost has a list of addresses they need to make deliveries to and a certain number of mail trucks available.

We start by converting the addresses to latitude and longitude coordinates, and then use the K-Means clustering algorithm to find the best set of addresses to give each mail truck.

Once each truck has a set of addresses, we use the Metropolis Travelling Salesman algorithm to find the quickest route for each mail truck. This algorithm uses the Google Distance Matrix API to calculate the time it takes to get from each address to each other address. Since this API can factor in traffic conditions, weather, road closures, and accidents when giving you a time estimate, we can take all of these things into account when running our algorithm.

So why not just use Google APIs for everything? Well, Google APIs don't let you optimize routes for multiple vehicles, and they don't let you optimize routes for a large number of waypoints. Our algorithm takes what they can do and expands it to solve bigger problems.

We've also provided a program that allows you to visualize all the routes on an interactive map. It uses Folium and the Google Directions API to show the route for each mail truck.

## What you will need to run our code

To run our code, you will need:

1. A relatively new version of Python with Jupyter notebook support.
2. Google Maps API for Python: https://github.com/googlemaps/google-maps-services-python
3. A Google API key. You can get one by signing up for a free Google Cloud account. Once you do that, place your API key in API_key.txt.
4. You will also need folium, geopy, sklearn, polyline, responses, numpy, and pandas. These can all be installed using pip.
   ALTERNATIVELY, you can just run the command "pip install -r requirements.txt" from within our project folder to install all the needed libraries automatically.

# Running the Code
Route_Finder.ipynb will take a list of addresses and a specified number of mail trucks and output a CSV file for each mail truck containing the optimum route.
You can set the number of trucks and specify the addresses in the notebook file, which also supports reading addresses from a CSV file.

Once the algorithm finishes running and you've found the optimum routes, just run Route_Visualizer.ipynb, and it will show you an interactive map showing the routes for all of your mail trucks.
