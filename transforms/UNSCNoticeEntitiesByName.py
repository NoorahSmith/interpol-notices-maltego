# Required Imports
from maltego_trx.maltego import MaltegoMsg, MaltegoTransform
from maltego_trx.transform import DiscoverableTransform
from .common import *

class UNSCNoticeEntitiesByName(DiscoverableTransform):

	@classmethod
	def create_entities(cls, request: MaltegoMsg, response: MaltegoTransform):
	
		# Obtain Target Information from Entity
		request_firstname = request.getProperty("firstname")
		if bool(request_firstname) == False:
			request_firstname = ''
			
		request_lastname = request.getProperty("lastname")
		if bool(request_lastname) == False:
			request_lastname = ''
		
		# Search for Target Information via Interpol UNSC Notice API
		url = 'https://ws-public.interpol.int/notices/v1/un?&name=' + request_lastname + '&forename=' + request_firstname
		
		api_response = requests.get(url)
		notices = api_response.json()
		notices = (notices['_embedded']['notices'])
		
		# Iterate through all returned UNSC Notices
		for notice_data in notices:
			notice_entity = response.addEntity("yourorganization.InterpolUNSCNotice")
			create_notice_entity(notice_entity, notice_data)


