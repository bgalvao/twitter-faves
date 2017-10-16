import twitter # has to be installed with 'pip install python-twitter'
import pickle
import sys # so as to know the error

with open('creds.pkl', 'rb') as handle:
    creds = pickle.load(handle)

# connect to the twitter api with your twitter app credentials
api = twitter.Api(consumer_key = creds['consumer_key'],\
                  consumer_secret = creds['consumer_secret'],\
                  access_token_key = creds['access_token_key'],\
                  access_token_secret = creds['access_token_secret'])

recent_favs = api.GetFavorites(screen_name='burnie093', count = 200) # this is a list

recent_favs[0].AsDict() # recent_favs[*] is a twitter.models.Status with a method AsDict()
recent_favs[0].AsDict()['text'] # you can now access the dict element text

to_save = [recent_favs[i].AsDict() for i in range(len(recent_favs))] # the request is stored in a separate file using pickle
with open('favs_0.pkl', 'wb') as handle: # 'wb' stands for 'write binary'
    pickle.dump(to_save, handle)
    
with open('favs_0.pkl', 'rb') as handle: # 'rb' stands for 'read binary'
    hi = pickle.load(handle)
hi[0]['text']


maxi = []
f = 0
while True: # will do this four more times, and will probably throw an error at some point
    try:
        favs = api.GetFavorites(screen_name='burnie093', count = 200, max_id = maxi)
        to_save = [favs[i].AsDict() for i in range(len(favs))]
        with open('favs_%d.pkl' % f, 'wb') as handle:
            pickle.dump(to_save, handle)
        
        # prepare for the next iteration
        f += 1
        if maxi == to_save[-1]['id']:
            break
        else:
            maxi = to_save[-1]['id']
    except:
        print(sys.exc_info()[0])
        break
    
texts = []
for i in range(f): # i belongs to [0, 5[
    with open('favs_%d.pkl' % i, 'rb') as handle:
        texts.extend([t['text'] for t in pickle.load(handle)])
print(len(texts))

#id/tweet tuples
indices = []
for i in range(f): # i belongs to [0, 5[
    with open('favs_%d.pkl' % i, 'rb') as handle:
        indices.extend([(t['id'],t['text']) for t in pickle.load(handle)])
print(indices[0])

#id/user tuples
users = []
for i in range(f): # i belongs to [0, 5[
    with open('favs_%d.pkl' % i, 'rb') as handle:
        users.extend([(t['id'],(t['user'])['screen_name']) for t in pickle.load(handle)])
        
print(users[0:3])
