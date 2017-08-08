import xml.etree.ElementTree as ET
import csv

tree = ET.parse("c:\Users\p2739075\Desktop\on_char_lineups_cable_20170725.xml")
root = tree.getroot()

Lineups_data = open('c:\Users\p2739075\Desktop\LineupsData.csv', 'w')
csvwriter = csv.writer(Lineups_data)
lineups_head = []

count = 0
for member in root.findall('Lineups'):
       lineups = []
       headend_list = []
       marketIds_list = []
       postalCodes_list = []
       location_list = []
       lineupdevice_list = []
       if count == 0:
           headend = member.find('headend').tag
           lineups_head.append(headend)
           msoid = member.find('msoid').tag
           lineups_head.append(msoid)
           marketIds = member.find('marketIds').tag
           lineups_head.append(marketIds)
           postalCodes = member[postalCodes].tag
           lineups_head.append(postalCodes)
           location = member.find('location').tag
           lineups_head.append(location)
           lineupdevice = member[lineupdevice].tag
           lineups_head.append(lineupdevice)

           csvwriter.writerow(lineups_head)
           count = count + 1

       headend = member.find('headend').text
       lineups.append(headend)
       msoid = member.find('msoid').text
       lineups.append(msoid)
       marketIds = member.find('marketIds').text
       lineups.append(marketIds)
       postalCodes = member.find('postalCodes').text
       lineups.append(postalCodes)
       location = member.find('location').text
       lineups.append(location
       #lineupdevice = member.find('lineupdevice').text
       #lineups.append(lineupdevice)
       #prgSvcId = member.find('prgSvcId').text
       #lineups.append(prgSvcId)
       
	   csvwriter.writerow(lineups)
Lineups_data.close()

