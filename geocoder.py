# https://developers.google.com/maps/documentation/geocoding/start
# https://andrewpwheeler.wordpress.com/2016/04/05/using-the-google-geocoding-api-with-python/
# https://stackoverflow.com/questions/3277503/in-python-how-do-i-read-a-file-line-by-line-into-a-list
# https://www.guru99.com/reading-and-writing-files-in-python.html
# https://community.esri.com/thread/196611-what-is-best-way-to-handle-files-in-python
#
# Python 2.7

import config
import urllib, json, time, os, errno

def GoogGeoAPI(address,api=config.api_key,delay=0):
  base = r"https://maps.googleapis.com/maps/api/geocode/json?"
  addP = "address=" + address.replace(" ","+")
  GeoUrl = base + addP + "&key=" + api
  response = urllib.urlopen(GeoUrl)
  jsonRaw = response.read()
  jsonData = json.loads(jsonRaw)
  if jsonData['status'] == 'OK':
    resu = jsonData['results'][0]
    finList = [resu['formatted_address'],resu['geometry']['location']['lat'],resu['geometry']['location']['lng'],resu['geometry']['location_type']]
  else:
    finList = [None,None,None,None]
  time.sleep(delay) #in seconds
  return finList

def loadlist(fname):
  with open(fname) as f:
    filelist = [line.rstrip('\n\r') for line in f]
  return filelist
  

try:
  wf = open('geocoding_result.txt', 'a+')   
except IOError as e:
  print(os.strerror(e.errno))

addresses = loadlist('addresses.txt')

# try:
start_from = 2918
starting = start_from - 1
count = starting

for addr in addresses[starting:]:
  count +=1
  georesult = GoogGeoAPI(address=addr)
  resultline = str(count) + '; ' + str(georesult[0]) + '; ' + str(georesult[1]) + '; ' + str(georesult[2]) + '; ' + str(georesult[3]) + '\n'
  print(resultline)
  wf.write(resultline)

print('Success!')

# except Exception as e:
#   print(e)

# finally:
wf.close()

####### integrate the below to allow user to choose method and records


try:
  wf = open('geocoding_result.txt', 'a+')   
except IOError as e:
  print(os.strerror(e.errno)) 

addresses = loadlist('addresses.txt')
address_file_line_number = [4895]

for n in address_file_line_number:
  count = n
  georesult = GoogGeoAPI(address=addresses[n-1])
  resultline = str(count) + '; ' + str(georesult[0]) + '; ' + str(georesult[1]) + '; ' + str(georesult[2]) + '; ' + str(georesult[3]) + '\n'
  print(resultline)
  wf.write(resultline)

print('Success!')

# except Exception as e:
#   print(e)

# finally:
wf.close()

# lines added to copy-paste to command line.  Remove to use this script outside the Python CLI

problem_linenums_incl_0TH_St = [27, 239, 240, 264, 531, 749, 852, 958, 965, 1040, 1042, 1046, 1074, 1076, 1113, 1118, 1119, 1132, 1202, 1207, 1209, 1214, 1243, 1245, 1436, 1442, 1451, 1575, 1992, 1993, 1994, 1999, 2014, 2017, 2098, 2263, 2506, 2522, 2525, 2526, 2527, 2540, 2541, 2557, 3734, 3780, 3806, 3809, 3837, 3986, 4000, 4002, 4009, 4083, 4108, 4167, 4215, 4226, 4227, 4269, 4310, 4312, 4496, 4818, 4853, 4906]
problem_linenums_without_0TH_St = [958, 965, 1575, 2098, 3734, 3780, 3806, 3809, 3837, 3986, 4000, 4002, 4009, 4083, 4108, 4167, 4215, 4226, 4227, 4269, 4310, 4312, 4496, 4818, 4853, 4906]
# the above were fixed and added to the results file.

problem_linenum_range_interp = [12, 114, 249, 260, 443, 664, 757, 758, 761, 764, 816, 945, 973, 1058, 1315, 1455, 1483, 1515, 1528, 1544, 1558, 1575, 1841, 1891, 1946, 1982, 2054, 2121, 2259, 2260, 2262, 2365, 2384, 2450, 2631, 2796, 2976, 3124, 3324, 3365, 3632, 3634, 3639, 3682, 3699, 3700, 3726, 3744, 3802, 3848, 3947, 4053, 4089, 4498, 4525, 4538, 4567, 4570, 4597, 4733, 4777, 4813, 4851, 4856, 4868, 4875, 4888, 4894, 4895, 4905]











