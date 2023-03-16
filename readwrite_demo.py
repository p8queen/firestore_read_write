
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore 

cred = credentials.Certificate("netninja-auth.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

#write

doc_ref = db.collection(u'stocks')
doc_ref.document(u'ggal').set({
    u'ticket': u'GGAL',
    u'open': 243.9,
    u'close': 244.70,
    u'date': u'11/22/2022'
})

doc_ref.document(u'appl').set({
    u'ticket': u'APPL',
    u'open': 143.9,
    u'close': 144.70,
    u'date': u'11/22/2022'
})

#delete
#doc_ref.document('obnn81tUNymf0n9VqmEw').delete()


#read
stocks_ref = db.collection(u'stocks')
docs = stocks_ref.stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')

