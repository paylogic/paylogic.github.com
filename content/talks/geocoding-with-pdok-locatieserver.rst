:slug: geocoding-with-pdok-locatieserver
:speaker: willy-tadema
:year: 2019
:title: Geocoding with PDOK LocatieServer

The Dutch National Spatial Data Infrastructure (PDOK) is a central
facility for unlocking geodatasets of national importance. This is
actual and reliable information for both the public and private
sector, and it's free! PDOK provides API's, for instance
LocatieServer. LocatieServer is a very powerfull geocoding
service. Upon request it will return the location of an adress,
street, place, neighbourhood, highway number, hectometer marker, and
so on. Major advantage of LocatieServer compared to other geocoding
services like Google and OpenStreetMap, is that it will also return
the *official* adresses and names. Moreover it will return unique
identifiers to link the search results to other sources of information
within government. Also the data are updated frequently. For instance,
adresses are updated daily. In my talk I'll explain how you can make
your own API requests to LocatieServer from within your Python
project.
