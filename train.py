#! /usr/bin/python
#-*- coding:utf-8 -*-

import numpy as np
import setup, caffe

caffe.set_mode_gpu()

model = "./model/solver.prototxt"
solver = caffe.SGDSolver(model)

last_iter_time = str(15000)
weights = "./result/deepid2_iter_" + last_iter_time + ".caffemodel"
state = "./result/deepid2_iter_" + last_iter_time + ".solverstate"
solver.net.copy_from(weights)
solver.restore(state)

for i in xrange(500):
	solver.step(100)

