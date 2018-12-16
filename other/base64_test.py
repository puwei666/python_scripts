
#coding=utf-8
import json, base64

def decode1(token):
    print 'token:'+ token
    token = base64.urlsafe_b64decode(token)
    print 'token1:'+ token
    return token

def decode2(token):
    print 'token:'+ token
    token = base64.b64decode(token, '-_')
    print 'token2:'+ token
    return token

def decode3(token):
    print 'token:'+ token
    lens = len(token)
    lenx = lens - (lens % 4 if lens % 4 else 4)
    token = base64.decodestring(token[:lenx])
    print 'token3:'+ token
    return token

token = 'eyJvcGVuSWQiOiJvVGNWNjVaeDF0dlZiRFRRb280LTBwZ3FKZS1vIiwic2NyZXdJZCI6Ind4ZjhlOTg4NmFjOTQ4MGViYSIsInVzZXJJZCI6ImYxYzIyY2IyMzFjNjRhZmU5YmM2OTFhNGViNzg3MTMxIn0.'
token = 'eyJvcGVuSWQiOiJvVGNWNjVUbnVBbmJNNTMwSWU4WUN0VTYxbnZRIiwic2NyZXdJZCI6Ind4ZjhlOTg4NmFjOTQ4MGViYSIsInVzZXJJZCI6IjQxNzhlMjMzZjYxYzQ2NTY5N2FhZGJiZTIzZWNjN2Q1In0.'

#token1 = decode1(token)

#token2 = decode2(token)

token3 = decode3(token)


