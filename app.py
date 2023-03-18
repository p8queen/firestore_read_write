import yahoo_fin.options as ops
import config
import time 
import numpy
from datetime import datetime, date
from pytz import timezone

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore 

cred = credentials.Certificate("netninja-auth.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
zone = 'US/Eastern'
#expiration_dates = ops.get_expiration_dates("^SPX")

strikes = list(range(3920,4010,10))
collectionId = 'SPXW230317'
doc_ref = db.collection(collectionId)

end = datetime(2023,3,17,17,00,tzinfo=timezone(zone))
ny_time = datetime.now(timezone(zone))

while config.signal=='run' and end>ny_time: 
	ny_time = datetime.now(timezone(zone))
	ny_timestamp = int(round(ny_time.timestamp()))
	df = ops.get_calls("^SPX", '03/17/2023') #"02/23/2023"
	dfV = df[df['Strike'].isin(strikes)]
	array = dfV.to_numpy()
	
	#write
	for i in range(len(array)):
		data = {'timestamp':ny_timestamp,
				'Strike':array[i,2],
				'LastPrice':array[i,3]}
		doc_ref.document().set(data)
	time.sleep(10)




print('end')