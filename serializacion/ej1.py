import json
import pickle

class SimpleEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Simple):
            return obj.__dict__  # Serialize Simple objects as their dictionary representation
        return json.JSONEncoder.default(self, obj)
    
class Simple:
    def __init__(self, value=5):
        self.value = value
    
simple = Simple("2")

#ejemplo serialización con json
x = json.dumps(simple, cls=SimpleEncoder)
print(x)

#ejemplo serializacion simple
'''obj2=simple("4")
obj3=simple("2")
#print(obj.__eq__(obj2))
#print(obj.__eq__(obj3))
#print(pickle.dumps(obj))
pickle.dump(obj, open('simple1.pkl', 'wb'))
pickle.dump(obj, open('simple2.pkl', 'wb'), protocol=pickle.HIGHEST_PROTOCOL)
x = pickle.load(open('simple1.pkl','rb'))
y = pickle.load(open('simple2.pkl','rb'))
print(obj2 == x)
assert(obj == x)'''
