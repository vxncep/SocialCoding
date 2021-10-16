import re
from requests import get

regexValidator = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
regexValidator2 = "^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$"

var1 = True

while var1:
    ipAdd = input("Input IP Address: ")
    def check(Ip):
        if(re.search(regexValidator, Ip)):
            print(" ")
            print('IP Address: ' + ipAdd)
            print('Country: ' + get('https://ipapi.co/'+ipAdd+'/country_name/').text)
            print('Country Code: ' + get('https://ipapi.co/'+ipAdd+'/country_code/').text)
            print('City: ' + get('https://ipapi.co/'+ipAdd+'/city/').text)
            print('Region: ' + get('https://ipapi.co/'+ipAdd+'/region/').text)
            print('Geolocation: ' + get('https://ipapi.co/'+ipAdd+'/latlong/').text)
            print('ASN ' + get('https://ipapi.co/'+ipAdd+'/asn/').text)
            print('Postal Code: ' + get('https://ipapi.co/'+ipAdd+'/postal/').text)
            print('Internet Service Provider: ' + get('https://ipapi.co/'+ipAdd+'/org/').text)
        elif(re.search(regexValidator2, Ip)):
            print(" ")
            print('IP Address: ' + ipAdd)
            print('Country: ' + get('https://ipapi.co/'+ipAdd+'/country_name/').text)
            print('Country Code: ' + get('https://ipapi.co/'+ipAdd+'/country_code/').text)
            print('City: ' + get('https://ipapi.co/'+ipAdd+'/city/').text)
            print('Region: ' + get('https://ipapi.co/'+ipAdd+'/region/').text)
            print('Geolocation: ' + get('https://ipapi.co/'+ipAdd+'/latlong/').text)
            print('ASN: ' + get('https://ipapi.co/'+ipAdd+'/asn/').text)
            print('Postal Code: ' + get('https://ipapi.co/'+ipAdd+'/postal/').text)
            print('Internet Service Provider: ' + get('https://ipapi.co/'+ipAdd+'/org/').text)
        else:
            print("IP address is invalid.")

    if __name__ == '__main__' :
        check(ipAdd)

        response = True
        while response:
            print(" ")
            var2 = input("Try again?[Y/N]: ")
            print(" ")
            
            if var2 == 'Y' or var2 == 'y':
                var1 = True
                break
            elif var2 == 'n' or var2 == 'N':
                var1 = False
                break
            else:
                print("Error! Please Try Again.")
                response

             