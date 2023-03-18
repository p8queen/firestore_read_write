
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime, date
from pytz import timezone 

cred = credentials.Certificate("netninja-auth.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

collectionId = 'SPXW230317'
doc_ref = db.collection(collectionId)

#read query

query = doc_ref.order_by(
    u'timestamp', direction=firestore.Query.DESCENDING).limit(9)
docs = query.stream()

docs2_ref = db.collection(collectionId)
query = docs2_ref.order_by("timestamp").limit_to_last(9)
results = query.get()

#read all 
# docs = doc_ref.stream()
zone = 'US/Eastern'
for doc in docs:
    data = doc.to_dict()
    dateTimestamp = datetime.fromtimestamp(data['timestamp'], tz=timezone(zone))
    print(f'{doc.id} => {data}', dateTimestamp)

print(' ------------------  ')
for doc in results:
    data = doc.to_dict()
    dateTimestamp = datetime.fromtimestamp(data['timestamp'], tz=timezone(zone))
    print(f'{doc.id} => {data}', dateTimestamp)

print(' ---- query where  --------  ')
# Note: Use of CollectionRef stream() is prefered to get()
query = doc_ref.order_by(u'timestamp').where(u'Strike',u'==',3960)
qdocs = query.stream()

for doc in qdocs:
    data = doc.to_dict()
    dateTimestamp = datetime.fromtimestamp(data['timestamp'], tz=timezone(zone))
    print(f'{doc.id} => {data}', dateTimestamp)