import requests
import time
import csv

# Configuration parameters and credentials
print('Upload a csv file to the same directory as this python script')
print('The csv file should only have 1 row, filled with as many serials as you like :).')
csv_name = input('Enter name of the csv file: ')

with open(csv_name, newline='') as f:
    reader = csv.reader(f)
    serials = list(reader)

log = open('log.txt', 'a')
x_cisco_meraki_api_key = input('input your Meraki api key: ')
header = {'X-Cisco-Meraki-API-Key':'{}'.format(x_cisco_meraki_api_key)}

wait = input('Wait time between Device reboots? (in seconds): ')
wait = int(wait)

##The Next 3 lines of code delete this weird gibberish that pops up when reading the first row from a csv file.
# if your first line is failing due to it being cut off the first 3 letters then del or comment out the next 3 lines.
lol = serials[0]
lol = lol[0]
serials[0] = ['{}'.format(lol[3:])]

for serial in serials:
    for serial in serial:
        base = 'https://api-mp.meraki.com/api/v1/devices/{}/reboot'.format(serial)
        r = requests.post(base, verify=False, headers=header)
        log.write('{}   {}'.format(serial,r.text))
        print('{}   {}'.format(serial,r.text))
        time.sleep(wait)

input('check the log or the console output for failures: Enter to close')


log.close()
