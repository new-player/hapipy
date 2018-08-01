from hapi.contacts import ContactsClient

api_key = 'Your API Key'

contact_client = ContactsClient(api_key=api_key)

data = {}
data['properties'] = []
data['properties'].append({
	'property': 'email',
	'value': 'testing@holidayhai.com'
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
