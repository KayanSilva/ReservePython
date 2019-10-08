import tensonflow as tf
from matplotlib import pyplot as plt
import numpy as np

x = tf.Variable(3, name="x")
y = tf.Variable(4, name="y")
f = x*x*y+y+2

init = tf.global_variables_initializer()

with tf.Session() as sess:
    init.run()
    result = t.eval()
print(result)
