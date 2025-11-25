'''
Everything about dictionary that is needed to know 

A dictionary is an unordered(but insertion ordered  after >= 3.7 version), mutable,
hashmap, collection of key value pairs.

think of it is as :
           "fast lookup for keys values"

'''

# creating dictionary
# d = {}
# d = {"a": 1, "b": 2}
# d = dict(a=1, b=2)
# d = dict([("a", 1), ("b", 2)])


# access
# d["key"] --> returns value but give error on no value
# d.get("key", default=None) --> returns value but if no value then default value is given

# insert/update
# d["x"] = 10


# clear() --> empty the whole dictionary
# d.clear()

# copy() --> returns a shallows copy of the dictionary
# d2 = d1.copy()

# items() --> returns a view of all key value pairs
# d.items()

# keys() --> returns a view of all keys
# d.keys()

# pop() --> remove the key and returns its value.
# d.pop("a")

# popitem() --> removes and returns the last key value pairs (feature add after python 3.7)
# d.popitem()

# setdefault() --> if key exists returns its value but if key not found  then insert default value and return default
# d.setdefault("a", 10)

# update() --> updates dictionary with another dictionary or key value list
# d.update({"a": 2})

# values() --> returns all values
# d.value()

# python 3.7+ new operators 

# merge dicts 
# d1 = {"a": 1}
# d2 = {"b": 2}
# d3 = d1 | d2

# merge in place
# d1 = {"a": 2}
# d2 |= {"b": 5}


# collison handling is done using open addressing and perturbation algorithm making lookup very fast
# ordered and unordered dictionary both exist in python
# dictionary is highly used in caching

# dictionary internals
# dict grows using the pwer of 2 size table

# learn while going advance
# very advanced: __missing__ in custom dict subclass and monkey patching dict for custom behavior

#