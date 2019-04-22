import firebase_admin
import time
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': 'confessite-f11ae',
})

db = firestore.client()


def all_confessions():
    context = {'posts': []}
    users_ref = db.collection(u'Confessions')
    docs = users_ref.get()
    for doc in docs:
        hold = doc.to_dict()
        hold['id'] = doc.id
        context['posts'].append(hold)
    return context
    # returns in the form of a dictionary with one list


def add_confession(content):
    users_ref = db.collection(u'Confessions')
    timestamp = time.gmtime(time.time())
    users_ref.add({
        'Content': str(content),
        'Time': str(str(timestamp[3])+':'+str(timestamp[4])+':'+str(timestamp[5])),
        'Date': (str(timestamp[2])+'/'+str(timestamp[1])+'/'+str(timestamp[0]))
    })


def delete_confession(confession_id):
    db.collection(u'Confessions').document(str(confession_id)).delete()


if __name__ == '__main__':
    print(all_confessions())
