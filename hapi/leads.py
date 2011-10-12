import time
from base import BaseClient

LEADS_API_VERSION = '1'

def list_to_dict_with_python_case_keys(list_):
    d = {}
    for item in list_:
        d[item] = item
        if item.lower() != item:
            python_variant = item[0].lower() + ''.join([c if c.lower()==c else '_%s'%c.lower() for c in item[1:]])
            d[python_variant] = item

_SORT_OPTIONS = [
    'firstName',
    'lastName',
    'email',
    'address',
    'phone',
    'insertedAt',
    'firstConvertedAt',
    'lastConvertedAt',
    'lastModifiedAt',
    'closedAt']
_SORT_OPTIONS_DICT = list_to_dict_with_python_case_keys(_SORT_OPTIONS)
_TIME_PIVOT_OPTIONS = [
    'insertedAt',
    'firstConvertedAt',
    'lastConvertedAt',
    'lastModifiedAt',
    'closedAt']
_TIME_PIVOT_OPTIONS_DICT = list_to_dict_with_python_case_keys(_TIME_PIVOT_OPTIONS)
_SEARCH_OPTIONS = [
    'search',
    'sort', 
    'dir',
    'max',
    'offset',
    'startTime',
    'stopTime',
    'timePivot',
    'excludeConversionEvents',
    'optout',
    'eligibleForEmail',
    'bounced',
    'isNotImported']
_SEARCH_OPTIONS_DICT = list_to_dict_with_python_case_keys(_SEARCH_OPTIONS)
_BOOLEAN_SEARCH_OPTIONS = [
    'excludeConversionEvents',
    'optout',
    'eligibleForEmail',
    'bounced',
    'isNotImported']


class LeadsClient(BaseClient):
    """
    The hapipy Leads client uses the _make_request method to call the API for data.  It returns a python object translated from the json return
    """

    def get_path(self, subpath):
        return 'leads/v%s/%s' % (LEADS_API_VERSION, subpath)
  
    def get_lead(self, guid, **options):
        return self.get_leads(guid, **options)[0]

    def get_leads(self, *guids, **options):
        """Supports all the search parameters in the API as well as python underscored variants"""
        params = {}
        for i in xrange(len(guids)):
            params['guids[%s]'%i] = guids[i]
        for o in options:
            key = _SEARCH_OPTIONS_DICT.get(o)
            if key:
                params[key] = options[o]
                if o in _BOOLEAN_SEARCH_OPTIONS:
                    params[key] = str(params[key]).lower()
        return self.call('list/', params, **options)
    
    def update_lead(self, guid, update_data=None, **options):
        update_data = update_data or {}
        update_data['guid'] = guid
        return self.call('lead/%s/' % guid, data=update_data, method='PUT', **options)
    
    def get_webhook(self, **options):  #WTF are these 2 methods for?
        return self.call('callback-url', **options)
    
    def register_webhook(self, url, **options):
        return self.call('callback-url', params={'url': url}, data={'url': url}, method='POST', **options)
    
    def close_lead(self, guid, close_time=None, **options):
        self.update_lead(guid, {'closedAt': close_time or int(time.time()*1000)}, **options)
    
