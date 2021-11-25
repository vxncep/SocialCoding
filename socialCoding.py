import re
import json
from requests import get

class IpGeoLocation:

    def check(Ip):

        regexValidator = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
        regexValidator2 = "^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$"

        if(re.search(regexValidator, Ip)):
            loc = get('https://ipapi.co/'+Ip+'/json/')
            ipDetails = loc.json()
            print(" ")
            print('IP Address: ' + Ip)
            print ('Country: ' +ipDetails['country_name'])
            print ('Country Code: ' +ipDetails['country_code'])
            print ('City: ' +ipDetails['city'])
            print ('Region: ' +ipDetails['region'])
            print ('Geolocation: ' +str(ipDetails['latitude']) +', '+str(ipDetails['longitude']))
            print ('ASN ' +ipDetails['asn'])
            print ('Postal Code: ' +ipDetails['postal'])
            print ('Internet Service Provider: ' +ipDetails['org'])
            return True
        elif(re.search(regexValidator2, Ip)):
            loc = get('https://ipapi.co/'+Ip+'/json/')
            ipDetails = loc.json()
            print(" ")
            print('IP Address: ' + Ip)
            print ('Country: ' +ipDetails['country_name'])
            print ('Country Code: ' +ipDetails['country_code'])
            print ('City: ' +ipDetails['city'])
            print ('Region: ' +ipDetails['region'])
            print ('Geolocation: ' +str(ipDetails['latitude']) +', '+str(ipDetails['longitude']))
            print ('ASN ' +ipDetails['asn'])
            print ('Postal Code: ' +ipDetails['postal'])
            print ('Internet Service Provider: ' +ipDetails['org'])
            return True
        else:
            print("IP address is invalid.")
            return False

    # response = True
    # while response == True:
    #     ipAdd = input("Input IP Address: ")
    #     check(ipAdd)
    #     print(" ")
    #     var2 = input("Try again?[Y/N]: ")
    #     print(" ")
        
    #     if var2 == 'Y' or var2 == 'y':
    #         response = True
    #     elif var2 == 'n' or var2 == 'N':
    #         response = False
    #     else:
    #         print("Error! Please Try Again.")