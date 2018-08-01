## hapipy

### Overview Here

A python wrapper around HubSpot's APIs. Docs for this wrapper can be found [here](https://github.com/HubSpot/hapipy/wiki/hapipy-documentation).

General API reference documentation can be found [here](https://docs.hubapi.com).

### Installation
pip install git+https://github.com/new-player/hapipy.git

### Sample Code
from hapi.contacts import ContactsClient
`
api_key = 'Your API Key'

contact_client = ContactsClient(api_key=api_key)

data = {}
data['properties'] = []
data['properties'].append({
	'property': 'email',
	'value': 'testing@email.com'
	})

data['properties'].append({
	'property': 'firstname',
	'value': 'testing user'
	})

data['properties'].append({
	'property': 'phone',
	'value': '09876543210'
	})

contact_client.create_a_contact(data=data)
`

Reference:
[https://github.com/CBitLabs/hapipy](https://github.com/CBitLabs/hapipy)
