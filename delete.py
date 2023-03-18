import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("netninja-auth.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

collectionId = 'SPXW230317'
doc_ref = db.collection(collectionId)

#delete
#doc_ref.document('obnn81tUNymf0n9VqmEw').delete()


#read
docs = doc_ref.stream()
for doc in docs:
    doc_ref.document(doc.id).delete()
    
