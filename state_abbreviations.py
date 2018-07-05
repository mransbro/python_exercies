k = ["CA", "NJ", "RI"]
v = ["California", "New Jersey", "Rhode Island"]

{key: value for (key, value) in iterable}


# make sure your solution is assigned to the answer variable so the tests can work!
answer = {k:v for (k,v) in zip(k,v)}
answer1 = {k[i]:v[i] for i in range(0,3)}