import tensorflow
hello = tensorflow.constant('string')
session = tensorflow.Session()
value = session.run(hello)
print(value)
a = tensorflow.constant(10)
b = tensorflow.constant(32)
value = session.run(a + b)
print(value)
session.close()
