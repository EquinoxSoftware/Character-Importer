import sys
import xlrd
from rauth import OAuth1Service


obsidianportal = OAuth1Service(
	name='obsidianportal',
	consumer_key = '0fQy0iwCORQWiVyVbDc8',
	consumer_secret = 'rGGVSAvic6lLzIHfJOtfqUA0O5lADeURK6CrxwVa',
	request_token_url='https://www.obsidianportal.com/oauth/request_token',
	access_token_url='https://www.obsidianportal.com/oauth/access_token',
	authorize_url='https://www.obsidianportal.com/oauth/authorize',
	base_url='http://api.obsidianportal.com/v1/)
	
	request_token, request_token_secret = obsidianportal.get_request_token()
	
	authorize_url = obsidianportal.get_authorize_url(request_token)
	
	print 'Visit this URL in your browser' + authorize_url
	pin = raw_input('Enter PIN from browser: '
	session = obsidianportal.get_auth_session(request_token,
									   request_token_secret,
									   method='POST',
									   data={'oauth_verifier': pin})
	
	campaignparams = {'use_slug' : 1}
	campaign = session.get('campaigns/'+sys.argv[3]+'.json',params = campaignparams)
	
	campaign_id = 'the-snake-king-rise'
	character_id = sys.argv[2]
	charparams = {'use_slug' : 1}
	character = session.get('campaigns/' + campaign_id +'characters/'+character_id+'.json', params = charparams)
	
	print character