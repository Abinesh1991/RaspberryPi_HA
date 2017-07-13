import googlemaps
from datetime import datetime
import gtts_test
gmaps = googlemaps.Client(key="")
now = datetime.now()
src = "Koramangala"
dest = "Ejipura"
def getTravelTime(src,dest):
    resultSet = gmaps.distance_matrix(src,dest,mode="transit",departure_time=now)
    # {u'status': u'OK', u'rows': [{u'elements': [{u'duration': {u'text': u'6 hours 30 mins', u'value': 23400},
    #                                              u'distance': {u'text': u'81.7 km', u'value': 81654}, u'status': u'OK'}]}],
    #  u'origin_addresses': [u'Ooty, Tamil Nadu, India'], u'destination_addresses': [u'Coimbatore, Tamil Nadu, India']}
    source = resultSet["origin_addresses"][0]
    destination = resultSet["destination_addresses"][0]
    time_taken = resultSet["rows"][0]["elements"][0]["duration"]["text"]
    txt = "Time Taken from "+src+" to  "+dest+" is " + time_taken
    gtts_test.convertTxt(txt,"en")
    gtts_test.getSpeech()



# print gmaps.directions("ooty","coimbatore",mode="transit",transit_mode="car",departure_time=now)
# geocode_result = gmaps.geocode('Koramanaga')
#
# directions_result = gmaps.directions("Sydney Town Hall",
#                                      "Parramatta, NSW",
#                                      mode="transit",
#                                      departure_time=now)
# print directions_result
# print directions_result
