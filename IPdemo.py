#!/usr/bin/python

import yaml
import SoftLayer

credsFile = open("softcreds.yaml",'r')
creds = yaml.load(credsFile)

#print creds['username']
#print creds['api_key']

client = SoftLayer.Client(username=(creds['username']), api_key=(creds['api_key']))

n = 1
#n=n++

while n < 31:
	
	n = n +1
	client['Virtual_Guest'].createObject({
     		'datacenter': {'name': 'mex01'},
        	'hostname': 'jbsampsoWintemp',
        	'domain': 'test.com',
        	'startCpus': 1,
        	'maxMemory': 4096,
        	'hourlyBillingFlag': 'true',
        	'localDiskFlag': 'false',
		'networkComponents': [{'maxSpeed': 1000}],
		'privateNetworkOnlyFlag': 'true',
		'blockDevices': [{'device': '0', 'diskImage': {'capacity': 100}}],
		'operatingSystemReferenceCode': 'WIN_2012-STD_64',
		'primaryBackendNetworkComponent': {'networkVlan': {'id': 773482}},

})

