from google.cloud import firestore

def connect_to_db():
    db = firestore.Client()
    return db

def construct_user(complete_poke_ids, id, points, user_credentials):
    # Get user fields
    db = connect_to_db()
    doc_ref = db.collection(u'Users').docuemnt(u'user_model')
    doc_ref.set(
        u'complete_pokes_ids'
    )

def construct_org(poke_ids, reward_ids, user_ids, org_id):
    db = connect_to_db()
    org_ref = db.collection(u'Orgs').document(u'orgs_model').get().to_dict()
    print(org_ref)
    org_ref['poke_ids'] = poke_ids
    org_ref['reward_ids'] = reward_ids
    org_ref['user_ids'] = user_ids

    # Add org to table
    db.collection(u'Orgs').document(org_id).set(org_ref)

def get_user_from_id(user_id):
    db = connect_to_db()
    user_ref = db.collection(u'Users').document(u'{}'.format(user_id))
    # Returns none of there is no user in the db with such an id
    return user_ref

# def add_user(user):

def get_all_elements():
    db = connect_to_db()
    all_fields = dict()

    all_org_info = db.collection(u'Orgs')
    orgs = all_org_info.stream()

    for org in orgs:
        all_fields[org.id] = org.to_dict()

    return all_fields

if __name__ == '__main__':
    print(get_all_elements())