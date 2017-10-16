import html
import re
import itertools


step0 = indices

# STEP 1: Removing noise: Escaping HTML characters
#step1 = [(step0[i][0], html.unescape(step0[i][1])) for i in range(len(step0))]
step1 = [(step0[i][0], re.sub(r' &\S+', '', step0[i][1])) for i in range(len(step0))]
print(step1[0])

# STEP 2: Removing noise: HTTP links
step2 = [(step0[i][0], re.sub(r' http\S+', '', step1[i][1])) for i in range(len(step1))]
print(step2[0])

# STEP 3: Standardizing: capitalization
step3 = [(step2[i][0], step2[i][1].lower()) for i in range(len(step2))]
print(step3[0])

# STEP 4: Standardizing: punctuation
step4 = [(step3[i][0], re.sub(r'[^\w\s\'&@#]', '', step3[i][1])) for i in range(len(step3))]
print(step4[0])

# STEP 5: Feature selection: tokenization as "bag of words"
tokens = [step4[i][1].split() for i in range(len(step4))]
tokens2 = [i for j in tokens for i in j]
corpus_size = len(tokens2)
print(corpus_size)

wordfreq = [(x,tokens2.count(x)) for x in set(tokens2)]
print(sorted(wordfreq, key=lambda x: -x[1])[0:5])

# STEP 6: Feature selection: hashtags and user tags
hashtags = re.findall(r'#\w+', str(tokens2))
print(hashtags[0:5])
hashtags_freq = sorted([(x, hashtags.count(x)) for x in set(hashtags)], key=lambda x: -x[1])
print(hashtags_freq)

usertags = re.findall(r'@\w+', str(tokens2))
print(usertags[0:30])


'''

# STEP X: Standardizing words (NOT WORKING)
step3 = [".join(".join(s)[:2] for _, s in itertools.groupby(step2[i])) for i in range(len(step2))]


# STEP X: Decoding data (Error: 'str' object has no attribute 'decode')
step2 = [step1[i].decode("utf8").encode('ascii','ignore') \
    for i in range(len(step1))]
print (step2[0])


# STEP X: Splitting attached words (working, but it ruins acronyms)
step4 = [" ".join(re.findall('[A-Z][^A-Z]*', step3[i])) for i in range(len(step3))]
print(step4[0])

'''