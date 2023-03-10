import uaddress
import uaddressformat as formatter

types = {
  
    'Country': '',
    'RegionType': '',
    'Region': '',
    'CountyType': '',
    'County': '',
    'SubLocalityType': '',
    'SubLocality': '',
    'LocalityType': '',
    'Locality': '',
    'StreetType': '',
    'Street': '',
    'HousingType': '',
    'Housing': '',
    'HostelType': '',
    'Hostel': '',
    'HouseNumberType': '',
    'HouseNumber': '',
    'HouseNumberAdditionally': '',
    'SectionType': '',
    'Section': '',
    'ApartmentType': '',
    'Apartment': '',
    'RoomType': '',
    'Room': '',
    'Sector': '',
    'EntranceType': '',
    'Entrance': '',
    'FloorType': '',
    'Floor': '',
    'PostCode': '',
    'Manually': '',
    'NotAddress': '',
    'Comment': '',
    'AdditionalData': ''

}

def formatStr(item):

    if item == 'RegionType':
        types[item] = formatter.RegionType(types[item], types['Region'])
    
    if item == 'Locality':
     
        locality = formatter.Locality(types['LocalityType'], types['Locality'])

        types['LocalityType'] = locality['type']
        types['Locality'] = locality['name']
        
    if item == 'Street':
        street = types['Street']

        result = formatter.Street(street)

        if result:
            types['Street'] = result

        result = formatter.Street(street, True)

        if result:
            types['StreetType'] = result
        else:
            types['StreetType'] = formatter.StreetType(types['StreetType'])

    if item == 'Housing':
        types[item] = formatter.Housing(types[item])

        if not types['HousingType']:
            types['HousingType'] = formatter.Housing(types[item], True)

    if item == 'EntranceType':
        types[item] = formatter.EntranceType(types[item], True)

    if item == 'HouseNumberType':
        types[item] = formatter.HouseNumberType(types[item], types['HouseNumber'])

    if item == 'HouseNumber':
        
        house = formatter.HouseNumber(types['HouseNumber'], types['HouseNumberAdditionally'])
    
        types['HouseNumber'] = house['house']
        types['HouseNumberAdditionally'] = house['additionally']
    
    if item == 'Apartment':
        data = formatter.ApartmentType(types['Apartment'], True)

        if type(data) is dict:
            types['Apartment'] = data['number']
            types['ApartmentType'] = data['type']

        if not types['ApartmentType'] and types['Apartment']:
            types['ApartmentType'] = formatter.ApartmentType(types['ApartmentType'])


parse_address = uaddress.parse('обл. Киев, м. Киев, РУСАНІВСЬКА НАБЕР., буд. 10, кв. 66, підʼїзд 3,  поверх 2')

for item in parse_address:
                
    if types[item[1]] and types[item[1]].lower() != item[0].lower():
        types[item[1]] += " " + item[0]
    else:
        types[item[1]] = item[0] 

for item in types:
    formatStr(item)

print('---------------------------------------------')
print("{:<30} {:<1} {:<30}".format('Type', '|','String'))
print('---------------------------------------------')

for k, v in types.items():
    print("{:<30} {:<1} {:<30}".format(k, '|', v))

print('---------------------------------------------')

