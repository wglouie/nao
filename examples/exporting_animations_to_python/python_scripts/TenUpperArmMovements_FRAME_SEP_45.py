#! /usr/bin/env python
#-*- coding: utf-8 -*-
#
# MACHINE: Ubuntu 16.04_x64 with Python 2.7.13
# MACHINE: Ubuntu 14.04_x64 with Python 2.7.6
# NAO VERSION: V4 T14
# NAOQI: naoqi 2.1.4.13 with python_naoqi-2.1.4.13-linux64
#
# Miguel P. Xochicale [http://mxochicale.github.io]
# Doctoral Researcher in Human-Robot Interaction
# University of Birmingham, U.K. (2014-2018)



##############################################################
# UPPER ARM MOTION DATA
##############################################################

# To export an animation, go to the
# 1. Timeline Editor
# 2. Export Motion to Clipboard
# 3. Python
# 4. bezier
#
#


# # Choregraphe bezier export in Python.
# from naoqi import ALProxy
# names = list()
# times = list()
# keys = list()
#
#
# try:
#   # uncomment the following line and modify the IP if you use this script outside Choregraphe.
#   # motion = ALProxy("ALMotion", IP, 9559)
#   motion = ALProxy("ALMotion")
#   motion.angleInterpolationBezier(names, times, keys)
# except BaseException, err:
#   print err




UpperArmMovements = [
	# names.append("HeadPitch")
	# times.append([1.8, 3.6, 5.4, 6.8, 8.6, 10.4, 12.2, 14, 15.8, 17.6, 19.4, 21.2, 23.2, 25, 26.8, 28.6, 30.4, 32.2, 34, 35.8, 37.6, 39.4])
	# keys.append([[-0.199461, [3, -0.6, 0], [3, 0.6, 0]], [-0.199461, [3, -0.6, 0], [3, 0.6, 0]], [-0.204064, [3, -0.6, 0], [3, 0.466667, 0]], [-0.199461, [3, -0.466667, 0], [3, 0.6, 0]], [-0.204064, [3, -0.6, 0], [3, 0.6, 0]], [-0.199461, [3, -0.6, 0], [3, 0.6, 0]], [-0.204064, [3, -0.6, 0], [3, 0.6, 0]], [-0.199461, [3, -0.6, 0], [3, 0.6, 0]], [-0.204064, [3, -0.6, 0], [3, 0.6, 0]], [-0.199461, [3, -0.6, 0], [3, 0.6, 0]], [-0.204064, [3, -0.6, 0], [3, 0.6, 0]], [-0.199461, [3, -0.6, 0], [3, 0.666667, 0]], [-0.204064, [3, -0.666667, 0], [3, 0.6, 0]], [-0.199461, [3, -0.6, 0], [3, 0.6, 0]], [-0.204064, [3, -0.6, 0], [3, 0.6, 0]], [-0.199461, [3, -0.6, 0], [3, 0.6, 0]], [-0.204064, [3, -0.6, 0], [3, 0.6, 0]], [-0.199461, [3, -0.6, 0], [3, 0.6, 0]], [-0.204064, [3, -0.6, 0], [3, 0.6, 0]], [-0.199461, [3, -0.6, 0], [3, 0.6, 0]], [-0.204064, [3, -0.6, 0], [3, 0.6, 0]], [-0.199461, [3, -0.6, 0], [3, 0, 0]]])
	["HeadPitch",
	[1.8, 3.6, 5.4, 6.8, 8.6, 10.4, 12.2, 14, 15.8, 17.6, 19.4, 21.2, 23.2, 25, 26.8, 28.6, 30.4, 32.2, 34, 35.8, 37.6, 39.4],
	[
	[-0.199461, [3, -0.6, 0], [3, 0.6, 0]], [-0.199461, [3, -0.6, 0], [3, 0.6, 0]], [-0.204064, [3, -0.6, 0], [3, 0.466667, 0]], [-0.199461, [3, -0.466667, 0], [3, 0.6, 0]], [-0.204064, [3, -0.6, 0], [3, 0.6, 0]], [-0.199461, [3, -0.6, 0], [3, 0.6, 0]], [-0.204064, [3, -0.6, 0], [3, 0.6, 0]], [-0.199461, [3, -0.6, 0], [3, 0.6, 0]], [-0.204064, [3, -0.6, 0], [3, 0.6, 0]], [-0.199461, [3, -0.6, 0], [3, 0.6, 0]], [-0.204064, [3, -0.6, 0], [3, 0.6, 0]], [-0.199461, [3, -0.6, 0], [3, 0.666667, 0]],
	[-0.204064, [3, -0.666667, 0], [3, 0.6, 0]], [-0.199461, [3, -0.6, 0], [3, 0.6, 0]], [-0.204064, [3, -0.6, 0], [3, 0.6, 0]], [-0.199461, [3, -0.6, 0], [3, 0.6, 0]], [-0.204064, [3, -0.6, 0], [3, 0.6, 0]], [-0.199461, [3, -0.6, 0], [3, 0.6, 0]], [-0.204064, [3, -0.6, 0], [3, 0.6, 0]], [-0.199461, [3, -0.6, 0], [3, 0.6, 0]], [-0.204064, [3, -0.6, 0], [3, 0.6, 0]], [-0.199461, [3, -0.6, 0], [3, 0, 0]]
	]
	],

	# names.append("HeadYaw")
	# times.append([1.8, 3.6, 5.4, 6.8, 8.6, 10.4, 12.2, 14, 15.8, 17.6, 19.4, 21.2, 23.2, 25, 26.8, 28.6, 30.4, 32.2, 34, 35.8, 37.6, 39.4])
	# keys.append([[0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.466667, 0]], [0, [3, -0.466667, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.666667, 0]], [0, [3, -0.666667, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0, 0]]])
	#
	["HeadYaw",
	[1.8, 3.6, 5.4, 6.8, 8.6, 10.4, 12.2, 14, 15.8, 17.6, 19.4, 21.2, 23.2, 25, 26.8, 28.6, 30.4, 32.2, 34, 35.8, 37.6, 39.4],
	[
	[0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.466667, 0]], [0, [3, -0.466667, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.666667, 0]], [0, [3, -0.666667, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]],
	[0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0, 0]]
	]
	],


	# names.append("LElbowRoll")
	# times.append([1.8, 3.6, 5.4, 6.8, 8.6, 10.4, 12.2, 14, 15.8, 17.6, 19.4, 21.2, 23.2, 25, 26.8, 28.6, 30.4, 32.2, 34, 35.8, 37.6, 39.4])
	# keys.append([[-0.782298, [3, -0.6, 0], [3, 0.6, 0]], [-0.308291, [3, -0.6, 0], [3, 0.6, 0]], [-0.406468, [3, -0.6, 0], [3, 0.466667, 0]], [-0.308291, [3, -0.466667, 0], [3, 0.6, 0]], [-0.406468, [3, -0.6, 0], [3, 0.6, 0]], [-0.308291, [3, -0.6, 0], [3, 0.6, 0]], [-0.406468, [3, -0.6, 0], [3, 0.6, 0]], [-0.308291, [3, -0.6, 0], [3, 0.6, 0]], [-0.406468, [3, -0.6, 0], [3, 0.6, 0]], [-0.308291, [3, -0.6, 0], [3, 0.6, 0]], [-0.406468, [3, -0.6, 0], [3, 0.6, 0]], [-0.308291, [3, -0.6, 0], [3, 0.666667, 0]], [-0.406468, [3, -0.666667, 0], [3, 0.6, 0]], [-0.308291, [3, -0.6, 0], [3, 0.6, 0]], [-0.406468, [3, -0.6, 0], [3, 0.6, 0]], [-0.308291, [3, -0.6, 0], [3, 0.6, 0]], [-0.406468, [3, -0.6, 0], [3, 0.6, 0]], [-0.308291, [3, -0.6, 0], [3, 0.6, 0]], [-0.406468, [3, -0.6, 0], [3, 0.6, 0]], [-0.308291, [3, -0.6, 0], [3, 0.6, 0]], [-0.406468, [3, -0.6, 0.0790012], [3, 0.6, -0.0790012]], [-0.782298, [3, -0.6, 0], [3, 0, 0]]])
	["LElbowRoll",
	[1.8, 3.6, 5.4, 6.8, 8.6, 10.4, 12.2, 14, 15.8, 17.6, 19.4, 21.2, 23.2, 25, 26.8, 28.6, 30.4, 32.2, 34, 35.8, 37.6, 39.4],
	[
	[-0.782298, [3, -0.6, 0], [3, 0.6, 0]], [-0.308291, [3, -0.6, 0], [3, 0.6, 0]], [-0.406468, [3, -0.6, 0], [3, 0.466667, 0]], [-0.308291, [3, -0.466667, 0], [3, 0.6, 0]], [-0.406468, [3, -0.6, 0], [3, 0.6, 0]], [-0.308291, [3, -0.6, 0], [3, 0.6, 0]], [-0.406468, [3, -0.6, 0], [3, 0.6, 0]], [-0.308291, [3, -0.6, 0], [3, 0.6, 0]], [-0.406468, [3, -0.6, 0], [3, 0.6, 0]], [-0.308291, [3, -0.6, 0], [3, 0.6, 0]], [-0.406468, [3, -0.6, 0], [3, 0.6, 0]],
	[-0.308291, [3, -0.6, 0], [3, 0.666667, 0]], [-0.406468, [3, -0.666667, 0], [3, 0.6, 0]], [-0.308291, [3, -0.6, 0], [3, 0.6, 0]], [-0.406468, [3, -0.6, 0], [3, 0.6, 0]], [-0.308291, [3, -0.6, 0], [3, 0.6, 0]], [-0.406468, [3, -0.6, 0], [3, 0.6, 0]], [-0.308291, [3, -0.6, 0], [3, 0.6, 0]], [-0.406468, [3, -0.6, 0], [3, 0.6, 0]], [-0.308291, [3, -0.6, 0], [3, 0.6, 0]], [-0.406468, [3, -0.6, 0.0790012], [3, 0.6, -0.0790012]], [-0.782298, [3, -0.6, 0], [3, 0, 0]]
	]
	],


	# names.append("LElbowYaw")
	# times.append([1.8, 3.6, 5.4, 6.8, 8.6, 10.4, 12.2, 14, 15.8, 17.6, 19.4, 21.2, 23.2, 25, 26.8, 28.6, 30.4, 32.2, 34, 35.8, 37.6, 39.4])
	# keys.append([[-1.23645, [3, -0.6, 0], [3, 0.6, 0]], [-0.366667, [3, -0.6, 0], [3, 0.6, 0]], [-0.630516, [3, -0.6, 0], [3, 0.466667, 0]], [-0.366667, [3, -0.466667, 0], [3, 0.6, 0]], [-0.630516, [3, -0.6, 0], [3, 0.6, 0]], [-0.366667, [3, -0.6, 0], [3, 0.6, 0]], [-0.630516, [3, -0.6, 0], [3, 0.6, 0]], [-0.366667, [3, -0.6, 0], [3, 0.6, 0]], [-0.630516, [3, -0.6, 0], [3, 0.6, 0]], [-0.366667, [3, -0.6, 0], [3, 0.6, 0]], [-0.630516, [3, -0.6, 0], [3, 0.6, 0]], [-0.366667, [3, -0.6, 0], [3, 0.666667, 0]], [-0.630516, [3, -0.666667, 0], [3, 0.6, 0]], [-0.366667, [3, -0.6, 0], [3, 0.6, 0]], [-0.630516, [3, -0.6, 0], [3, 0.6, 0]], [-0.366667, [3, -0.6, 0], [3, 0.6, 0]], [-0.630516, [3, -0.6, 0], [3, 0.6, 0]], [-0.366667, [3, -0.6, 0], [3, 0.6, 0]], [-0.630516, [3, -0.6, 0], [3, 0.6, 0]], [-0.366667, [3, -0.6, 0], [3, 0.6, 0]], [-0.630516, [3, -0.6, 0.144963], [3, 0.6, -0.144963]], [-1.23645, [3, -0.6, 0], [3, 0, 0]]])
	["LElbowYaw",
	[1.8, 3.6, 5.4, 6.8, 8.6, 10.4, 12.2, 14, 15.8, 17.6, 19.4, 21.2, 23.2, 25, 26.8, 28.6, 30.4, 32.2, 34, 35.8, 37.6, 39.4],
	[
	[-1.23645, [3, -0.6, 0], [3, 0.6, 0]], [-0.366667, [3, -0.6, 0], [3, 0.6, 0]], [-0.630516, [3, -0.6, 0], [3, 0.466667, 0]], [-0.366667, [3, -0.466667, 0], [3, 0.6, 0]], [-0.630516, [3, -0.6, 0], [3, 0.6, 0]], [-0.366667, [3, -0.6, 0], [3, 0.6, 0]], [-0.630516, [3, -0.6, 0], [3, 0.6, 0]], [-0.366667, [3, -0.6, 0], [3, 0.6, 0]], [-0.630516, [3, -0.6, 0], [3, 0.6, 0]], [-0.366667, [3, -0.6, 0], [3, 0.6, 0]], [-0.630516, [3, -0.6, 0], [3, 0.6, 0]],
	[-0.366667, [3, -0.6, 0], [3, 0.666667, 0]], [-0.630516, [3, -0.666667, 0], [3, 0.6, 0]], [-0.366667, [3, -0.6, 0], [3, 0.6, 0]], [-0.630516, [3, -0.6, 0], [3, 0.6, 0]], [-0.366667, [3, -0.6, 0], [3, 0.6, 0]], [-0.630516, [3, -0.6, 0], [3, 0.6, 0]], [-0.366667, [3, -0.6, 0], [3, 0.6, 0]], [-0.630516, [3, -0.6, 0], [3, 0.6, 0]], [-0.366667, [3, -0.6, 0], [3, 0.6, 0]], [-0.630516, [3, -0.6, 0.144963], [3, 0.6, -0.144963]], [-1.23645, [3, -0.6, 0], [3, 0, 0]]
	]
	],


	# names.append("LHand")
	# times.append([1.8, 3.6, 5.4, 6.8, 8.6, 10.4, 12.2, 14, 15.8, 17.6, 19.4, 21.2, 23.2, 25, 26.8, 28.6, 30.4, 32.2, 34, 35.8, 37.6, 39.4])
	# keys.append([[0.3532, [3, -0.6, 0], [3, 0.6, 0]], [0.6588, [3, -0.6, -0.0752], [3, 0.6, 0.0752]], [0.8044, [3, -0.6, 0], [3, 0.466667, 0]], [0.6588, [3, -0.466667, 0], [3, 0.6, 0]], [0.8044, [3, -0.6, 0], [3, 0.6, 0]], [0.6588, [3, -0.6, 0], [3, 0.6, 0]], [0.8044, [3, -0.6, 0], [3, 0.6, 0]], [0.6588, [3, -0.6, 0], [3, 0.6, 0]], [0.8044, [3, -0.6, 0], [3, 0.6, 0]], [0.6588, [3, -0.6, 0], [3, 0.6, 0]], [0.8044, [3, -0.6, 0], [3, 0.6, 0]], [0.6588, [3, -0.6, 0], [3, 0.666667, 0]], [0.8044, [3, -0.666667, 0], [3, 0.6, 0]], [0.6588, [3, -0.6, 0], [3, 0.6, 0]], [0.8044, [3, -0.6, 0], [3, 0.6, 0]], [0.6588, [3, -0.6, 0], [3, 0.6, 0]], [0.8044, [3, -0.6, 0], [3, 0.6, 0]], [0.6588, [3, -0.6, 0], [3, 0.6, 0]], [0.8044, [3, -0.6, 0], [3, 0.6, 0]], [0.6588, [3, -0.6, 0], [3, 0.6, 0]], [0.8044, [3, -0.6, 0], [3, 0.6, 0]], [0.3532, [3, -0.6, 0], [3, 0, 0]]])
	#
	["LHand",
	[1.8, 3.6, 5.4, 6.8, 8.6, 10.4, 12.2, 14, 15.8, 17.6, 19.4, 21.2, 23.2, 25, 26.8, 28.6, 30.4, 32.2, 34, 35.8, 37.6, 39.4],
	[
	[0.3532, [3, -0.6, 0], [3, 0.6, 0]], [0.6588, [3, -0.6, -0.0752], [3, 0.6, 0.0752]], [0.8044, [3, -0.6, 0], [3, 0.466667, 0]], [0.6588, [3, -0.466667, 0], [3, 0.6, 0]], [0.8044, [3, -0.6, 0], [3, 0.6, 0]], [0.6588, [3, -0.6, 0], [3, 0.6, 0]], [0.8044, [3, -0.6, 0], [3, 0.6, 0]], [0.6588, [3, -0.6, 0], [3, 0.6, 0]], [0.8044, [3, -0.6, 0], [3, 0.6, 0]], [0.6588, [3, -0.6, 0], [3, 0.6, 0]], [0.8044, [3, -0.6, 0], [3, 0.6, 0]], [0.6588, [3, -0.6, 0], [3, 0.666667, 0]],
	[0.8044, [3, -0.666667, 0], [3, 0.6, 0]], [0.6588, [3, -0.6, 0], [3, 0.6, 0]], [0.8044, [3, -0.6, 0], [3, 0.6, 0]], [0.6588, [3, -0.6, 0], [3, 0.6, 0]], [0.8044, [3, -0.6, 0], [3, 0.6, 0]], [0.6588, [3, -0.6, 0], [3, 0.6, 0]], [0.8044, [3, -0.6, 0], [3, 0.6, 0]], [0.6588, [3, -0.6, 0], [3, 0.6, 0]], [0.8044, [3, -0.6, 0], [3, 0.6, 0]], [0.3532, [3, -0.6, 0], [3, 0, 0]]
	]
	],


	# names.append("LShoulderPitch")
	# times.append([1.8, 3.6, 5.4, 6.8, 8.6, 10.4, 12.2, 14, 15.8, 17.6, 19.4, 21.2, 23.2, 25, 26.8, 28.6, 30.4, 32.2, 34, 35.8, 37.6, 39.4])
	# keys.append([[-0.783916, [3, -0.6, 0], [3, 0.6, 0]], [-1.1214, [3, -0.6, 0], [3, 0.6, 0]], [-1.09839, [3, -0.6, 0], [3, 0.466667, 0]], [-1.1214, [3, -0.466667, 0], [3, 0.6, 0]], [-1.09839, [3, -0.6, 0], [3, 0.6, 0]], [-1.1214, [3, -0.6, 0], [3, 0.6, 0]], [-1.09839, [3, -0.6, 0], [3, 0.6, 0]], [-1.1214, [3, -0.6, 0], [3, 0.6, 0]], [-1.09839, [3, -0.6, 0], [3, 0.6, 0]], [-1.1214, [3, -0.6, 0], [3, 0.6, 0]], [-1.09839, [3, -0.6, 0], [3, 0.6, 0]], [-1.1214, [3, -0.6, 0], [3, 0.666667, 0]], [-1.09839, [3, -0.666667, 0], [3, 0.6, 0]], [-1.1214, [3, -0.6, 0], [3, 0.6, 0]], [-1.09839, [3, -0.6, 0], [3, 0.6, 0]], [-1.1214, [3, -0.6, 0], [3, 0.6, 0]], [-1.09839, [3, -0.6, 0], [3, 0.6, 0]], [-1.1214, [3, -0.6, 0], [3, 0.6, 0]], [-1.09839, [3, -0.6, 0], [3, 0.6, 0]], [-1.1214, [3, -0.6, 0], [3, 0.6, 0]], [-1.09839, [3, -0.6, -0.0230104], [3, 0.6, 0.0230104]], [-0.783916, [3, -0.6, 0], [3, 0, 0]]])
	["LShoulderPitch",
	[1.8, 3.6, 5.4, 6.8, 8.6, 10.4, 12.2, 14, 15.8, 17.6, 19.4, 21.2, 23.2, 25, 26.8, 28.6, 30.4, 32.2, 34, 35.8, 37.6, 39.4],
	[
	[-0.783916, [3, -0.6, 0], [3, 0.6, 0]], [-1.1214, [3, -0.6, 0], [3, 0.6, 0]], [-1.09839, [3, -0.6, 0], [3, 0.466667, 0]], [-1.1214, [3, -0.466667, 0], [3, 0.6, 0]], [-1.09839, [3, -0.6, 0], [3, 0.6, 0]], [-1.1214, [3, -0.6, 0], [3, 0.6, 0]], [-1.09839, [3, -0.6, 0], [3, 0.6, 0]], [-1.1214, [3, -0.6, 0], [3, 0.6, 0]], [-1.09839, [3, -0.6, 0], [3, 0.6, 0]], [-1.1214, [3, -0.6, 0], [3, 0.6, 0]], [-1.09839, [3, -0.6, 0], [3, 0.6, 0]], [-1.1214, [3, -0.6, 0], [3, 0.666667, 0]],
	[-1.09839, [3, -0.666667, 0], [3, 0.6, 0]], [-1.1214, [3, -0.6, 0], [3, 0.6, 0]], [-1.09839, [3, -0.6, 0], [3, 0.6, 0]], [-1.1214, [3, -0.6, 0], [3, 0.6, 0]], [-1.09839, [3, -0.6, 0], [3, 0.6, 0]], [-1.1214, [3, -0.6, 0], [3, 0.6, 0]], [-1.09839, [3, -0.6, 0], [3, 0.6, 0]], [-1.1214, [3, -0.6, 0], [3, 0.6, 0]], [-1.09839, [3, -0.6, -0.0230104], [3, 0.6, 0.0230104]], [-0.783916, [3, -0.6, 0], [3, 0, 0]]
	]
	],


	# names.append("LShoulderRoll")
	# times.append([1.8, 3.6, 5.4, 6.8, 8.6, 10.4, 12.2, 14, 15.8, 17.6, 19.4, 21.2, 23.2, 25, 26.8, 28.6, 30.4, 32.2, 34, 35.8, 37.6, 39.4])
	# keys.append([[0.184038, [3, -0.6, 0], [3, 0.6, 0]], [-0.29457, [3, -0.6, 0], [3, 0.6, 0]], [0.800706, [3, -0.6, 0], [3, 0.466667, 0]], [-0.29457, [3, -0.466667, 0], [3, 0.6, 0]], [0.800706, [3, -0.6, 0], [3, 0.6, 0]], [-0.29457, [3, -0.6, 0], [3, 0.6, 0]], [0.800706, [3, -0.6, 0], [3, 0.6, 0]], [-0.29457, [3, -0.6, 0], [3, 0.6, 0]], [0.800706, [3, -0.6, 0], [3, 0.6, 0]], [-0.29457, [3, -0.6, 0], [3, 0.6, 0]], [0.800706, [3, -0.6, 0], [3, 0.6, 0]], [-0.29457, [3, -0.6, 0], [3, 0.666667, 0]], [0.800706, [3, -0.666667, 0], [3, 0.6, 0]], [-0.29457, [3, -0.6, 0], [3, 0.6, 0]], [0.800706, [3, -0.6, 0], [3, 0.6, 0]], [-0.29457, [3, -0.6, 0], [3, 0.6, 0]], [0.800706, [3, -0.6, 0], [3, 0.6, 0]], [-0.29457, [3, -0.6, 0], [3, 0.6, 0]], [0.800706, [3, -0.6, 0], [3, 0.6, 0]], [-0.29457, [3, -0.6, 0], [3, 0.6, 0]], [0.800706, [3, -0.6, 0], [3, 0.6, 0]], [0.184038, [3, -0.6, 0], [3, 0, 0]]])
	#
	["LShoulderRoll",
	[1.8, 3.6, 5.4, 6.8, 8.6, 10.4, 12.2, 14, 15.8, 17.6, 19.4, 21.2, 23.2, 25, 26.8, 28.6, 30.4, 32.2, 34, 35.8, 37.6, 39.4],
	[
	[0.184038, [3, -0.6, 0], [3, 0.6, 0]], [-0.29457, [3, -0.6, 0], [3, 0.6, 0]], [0.800706, [3, -0.6, 0], [3, 0.466667, 0]], [-0.29457, [3, -0.466667, 0], [3, 0.6, 0]], [0.800706, [3, -0.6, 0], [3, 0.6, 0]], [-0.29457, [3, -0.6, 0], [3, 0.6, 0]], [0.800706, [3, -0.6, 0], [3, 0.6, 0]], [-0.29457, [3, -0.6, 0], [3, 0.6, 0]], [0.800706, [3, -0.6, 0], [3, 0.6, 0]], [-0.29457, [3, -0.6, 0], [3, 0.6, 0]], [0.800706, [3, -0.6, 0], [3, 0.6, 0]], [-0.29457, [3, -0.6, 0], [3, 0.666667, 0]],
	[0.800706, [3, -0.666667, 0], [3, 0.6, 0]], [-0.29457, [3, -0.6, 0], [3, 0.6, 0]], [0.800706, [3, -0.6, 0], [3, 0.6, 0]], [-0.29457, [3, -0.6, 0], [3, 0.6, 0]], [0.800706, [3, -0.6, 0], [3, 0.6, 0]], [-0.29457, [3, -0.6, 0], [3, 0.6, 0]], [0.800706, [3, -0.6, 0], [3, 0.6, 0]], [-0.29457, [3, -0.6, 0], [3, 0.6, 0]], [0.800706, [3, -0.6, 0], [3, 0.6, 0]], [0.184038, [3, -0.6, 0], [3, 0, 0]]
	]
	],


	# names.append("LWristYaw")
	# times.append([1.8, 3.6, 5.4, 6.8, 8.6, 10.4, 12.2, 14, 15.8, 17.6, 19.4, 21.2, 23.2, 25, 26.8, 28.6, 30.4, 32.2, 34, 35.8, 37.6, 39.4])
	# keys.append([[0.00455999, [3, -0.6, 0], [3, 0.6, 0]], [0.260738, [3, -0.6, -0.066729], [3, 0.6, 0.066729]], [0.404934, [3, -0.6, 0], [3, 0.466667, 0]], [0.260738, [3, -0.466667, 0], [3, 0.6, 0]], [0.404934, [3, -0.6, 0], [3, 0.6, 0]], [0.260738, [3, -0.6, 0], [3, 0.6, 0]], [0.404934, [3, -0.6, 0], [3, 0.6, 0]], [0.260738, [3, -0.6, 0], [3, 0.6, 0]], [0.404934, [3, -0.6, 0], [3, 0.6, 0]], [0.260738, [3, -0.6, 0], [3, 0.6, 0]], [0.404934, [3, -0.6, 0], [3, 0.6, 0]], [0.260738, [3, -0.6, 0], [3, 0.666667, 0]], [0.404934, [3, -0.666667, 0], [3, 0.6, 0]], [0.260738, [3, -0.6, 0], [3, 0.6, 0]], [0.404934, [3, -0.6, 0], [3, 0.6, 0]], [0.260738, [3, -0.6, 0], [3, 0.6, 0]], [0.404934, [3, -0.6, 0], [3, 0.6, 0]], [0.260738, [3, -0.6, 0], [3, 0.6, 0]], [0.404934, [3, -0.6, 0], [3, 0.6, 0]], [0.260738, [3, -0.6, 0], [3, 0.6, 0]], [0.404934, [3, -0.6, 0], [3, 0.6, 0]], [0.00455999, [3, -0.6, 0], [3, 0, 0]]])
	["LWristYaw",
	[1.8, 3.6, 5.4, 6.8, 8.6, 10.4, 12.2, 14, 15.8, 17.6, 19.4, 21.2, 23.2, 25, 26.8, 28.6, 30.4, 32.2, 34, 35.8, 37.6, 39.4],
	[
	[0.00455999, [3, -0.6, 0], [3, 0.6, 0]], [0.260738, [3, -0.6, -0.066729], [3, 0.6, 0.066729]], [0.404934, [3, -0.6, 0], [3, 0.466667, 0]], [0.260738, [3, -0.466667, 0], [3, 0.6, 0]], [0.404934, [3, -0.6, 0], [3, 0.6, 0]], [0.260738, [3, -0.6, 0], [3, 0.6, 0]], [0.404934, [3, -0.6, 0], [3, 0.6, 0]], [0.260738, [3, -0.6, 0], [3, 0.6, 0]], [0.404934, [3, -0.6, 0], [3, 0.6, 0]], [0.260738, [3, -0.6, 0], [3, 0.6, 0]], [0.404934, [3, -0.6, 0], [3, 0.6, 0]],
	[0.260738, [3, -0.6, 0], [3, 0.666667, 0]], [0.404934, [3, -0.666667, 0], [3, 0.6, 0]], [0.260738, [3, -0.6, 0], [3, 0.6, 0]], [0.404934, [3, -0.6, 0], [3, 0.6, 0]], [0.260738, [3, -0.6, 0], [3, 0.6, 0]], [0.404934, [3, -0.6, 0], [3, 0.6, 0]], [0.260738, [3, -0.6, 0], [3, 0.6, 0]], [0.404934, [3, -0.6, 0], [3, 0.6, 0]], [0.260738, [3, -0.6, 0], [3, 0.6, 0]], [0.404934, [3, -0.6, 0], [3, 0.6, 0]], [0.00455999, [3, -0.6, 0], [3, 0, 0]]
	]
	],


	# names.append("RElbowRoll")
	# times.append([1.8, 3.6, 5.4, 6.8, 8.6, 10.4, 12.2, 14, 15.8, 17.6, 19.4, 21.2, 23.2, 25, 26.8, 28.6, 30.4, 32.2, 34, 35.8, 37.6, 39.4])
	# keys.append([[0.771643, [3, -0.6, 0], [3, 0.6, 0]], [0.257754, [3, -0.6, 0], [3, 0.6, 0]], [0.331386, [3, -0.6, 0], [3, 0.466667, 0]], [0.257754, [3, -0.466667, 0], [3, 0.6, 0]], [0.331386, [3, -0.6, 0], [3, 0.6, 0]], [0.257754, [3, -0.6, 0], [3, 0.6, 0]], [0.331386, [3, -0.6, 0], [3, 0.6, 0]], [0.257754, [3, -0.6, 0], [3, 0.6, 0]], [0.331386, [3, -0.6, 0], [3, 0.6, 0]], [0.257754, [3, -0.6, 0], [3, 0.6, 0]], [0.331386, [3, -0.6, 0], [3, 0.6, 0]], [0.257754, [3, -0.6, 0], [3, 0.666667, 0]], [0.331386, [3, -0.666667, 0], [3, 0.6, 0]], [0.257754, [3, -0.6, 0], [3, 0.6, 0]], [0.331386, [3, -0.6, 0], [3, 0.6, 0]], [0.257754, [3, -0.6, 0], [3, 0.6, 0]], [0.331386, [3, -0.6, 0], [3, 0.6, 0]], [0.257754, [3, -0.6, 0], [3, 0.6, 0]], [0.331386, [3, -0.6, 0], [3, 0.6, 0]], [0.257754, [3, -0.6, 0], [3, 0.6, 0]], [0.331386, [3, -0.6, -0.0736319], [3, 0.6, 0.0736319]], [0.771643, [3, -0.6, 0], [3, 0, 0]]])
	["RElbowRoll",
	[1.8, 3.6, 5.4, 6.8, 8.6, 10.4, 12.2, 14, 15.8, 17.6, 19.4, 21.2, 23.2, 25, 26.8, 28.6, 30.4, 32.2, 34, 35.8, 37.6, 39.4],
	[
	[0.771643, [3, -0.6, 0], [3, 0.6, 0]], [0.257754, [3, -0.6, 0], [3, 0.6, 0]], [0.331386, [3, -0.6, 0], [3, 0.466667, 0]], [0.257754, [3, -0.466667, 0], [3, 0.6, 0]], [0.331386, [3, -0.6, 0], [3, 0.6, 0]], [0.257754, [3, -0.6, 0], [3, 0.6, 0]], [0.331386, [3, -0.6, 0], [3, 0.6, 0]], [0.257754, [3, -0.6, 0], [3, 0.6, 0]], [0.331386, [3, -0.6, 0], [3, 0.6, 0]], [0.257754, [3, -0.6, 0], [3, 0.6, 0]], [0.331386, [3, -0.6, 0], [3, 0.6, 0]], [0.257754, [3, -0.6, 0], [3, 0.666667, 0]],
	[0.331386, [3, -0.666667, 0], [3, 0.6, 0]], [0.257754, [3, -0.6, 0], [3, 0.6, 0]], [0.331386, [3, -0.6, 0], [3, 0.6, 0]], [0.257754, [3, -0.6, 0], [3, 0.6, 0]], [0.331386, [3, -0.6, 0], [3, 0.6, 0]], [0.257754, [3, -0.6, 0], [3, 0.6, 0]], [0.331386, [3, -0.6, 0], [3, 0.6, 0]], [0.257754, [3, -0.6, 0], [3, 0.6, 0]], [0.331386, [3, -0.6, -0.0736319], [3, 0.6, 0.0736319]], [0.771643, [3, -0.6, 0], [3, 0, 0]]
	]
	],

	# names.append("RElbowYaw")
	# times.append([1.8, 3.6, 5.4, 6.8, 8.6, 10.4, 12.2, 14, 15.8, 17.6, 19.4, 21.2, 23.2, 25, 26.8, 28.6, 30.4, 32.2, 34, 35.8, 37.6, 39.4])
	# keys.append([[1.27318, [3, -0.6, 0], [3, 0.6, 0]], [1.00626, [3, -0.6, 0.0800236], [3, 0.6, -0.0800236]], [0.793036, [3, -0.6, 0], [3, 0.466667, 0]], [1.00626, [3, -0.466667, 0], [3, 0.6, 0]], [0.793036, [3, -0.6, 0], [3, 0.6, 0]], [1.00626, [3, -0.6, 0], [3, 0.6, 0]], [0.793036, [3, -0.6, 0], [3, 0.6, 0]], [1.00626, [3, -0.6, 0], [3, 0.6, 0]], [0.793036, [3, -0.6, 0], [3, 0.6, 0]], [1.00626, [3, -0.6, 0], [3, 0.6, 0]], [0.793036, [3, -0.6, 0], [3, 0.6, 0]], [1.00626, [3, -0.6, 0], [3, 0.666667, 0]], [0.793036, [3, -0.666667, 0], [3, 0.6, 0]], [1.00626, [3, -0.6, 0], [3, 0.6, 0]], [0.793036, [3, -0.6, 0], [3, 0.6, 0]], [1.00626, [3, -0.6, 0], [3, 0.6, 0]], [0.793036, [3, -0.6, 0], [3, 0.6, 0]], [1.00626, [3, -0.6, 0], [3, 0.6, 0]], [0.793036, [3, -0.6, 0], [3, 0.6, 0]], [1.00626, [3, -0.6, 0], [3, 0.6, 0]], [0.793036, [3, -0.6, 0], [3, 0.6, 0]], [1.27318, [3, -0.6, 0], [3, 0, 0]]])
	#
	["RElbowYaw",
	[1.8, 3.6, 5.4, 6.8, 8.6, 10.4, 12.2, 14, 15.8, 17.6, 19.4, 21.2, 23.2, 25, 26.8, 28.6, 30.4, 32.2, 34, 35.8, 37.6, 39.4],
	[
	[1.27318, [3, -0.6, 0], [3, 0.6, 0]], [1.00626, [3, -0.6, 0.0800236], [3, 0.6, -0.0800236]], [0.793036, [3, -0.6, 0], [3, 0.466667, 0]], [1.00626, [3, -0.466667, 0], [3, 0.6, 0]], [0.793036, [3, -0.6, 0], [3, 0.6, 0]], [1.00626, [3, -0.6, 0], [3, 0.6, 0]], [0.793036, [3, -0.6, 0], [3, 0.6, 0]], [1.00626, [3, -0.6, 0], [3, 0.6, 0]], [0.793036, [3, -0.6, 0], [3, 0.6, 0]], [1.00626, [3, -0.6, 0], [3, 0.6, 0]], [0.793036, [3, -0.6, 0], [3, 0.6, 0]], [1.00626, [3, -0.6, 0], [3, 0.666667, 0]],
	[0.793036, [3, -0.666667, 0], [3, 0.6, 0]], [1.00626, [3, -0.6, 0], [3, 0.6, 0]], [0.793036, [3, -0.6, 0], [3, 0.6, 0]], [1.00626, [3, -0.6, 0], [3, 0.6, 0]], [0.793036, [3, -0.6, 0], [3, 0.6, 0]], [1.00626, [3, -0.6, 0], [3, 0.6, 0]], [0.793036, [3, -0.6, 0], [3, 0.6, 0]], [1.00626, [3, -0.6, 0], [3, 0.6, 0]], [0.793036, [3, -0.6, 0], [3, 0.6, 0]], [1.27318, [3, -0.6, 0], [3, 0, 0]]
	]
	],

	# names.append("RHand")
	# times.append([1.8, 3.6, 5.4, 6.8, 8.6, 10.4, 12.2, 14, 15.8, 17.6, 19.4, 21.2, 23.2, 25, 26.8, 28.6, 30.4, 32.2, 34, 35.8, 37.6, 39.4])
	# keys.append([[0.312, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.466667, 0]], [0.6736, [3, -0.466667, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.666667, 0]], [0.6736, [3, -0.666667, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.312, [3, -0.6, 0], [3, 0, 0]]])
	#
	["RHand",
	[1.8, 3.6, 5.4, 6.8, 8.6, 10.4, 12.2, 14, 15.8, 17.6, 19.4, 21.2, 23.2, 25, 26.8, 28.6, 30.4, 32.2, 34, 35.8, 37.6, 39.4],
	[
	[0.312, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.466667, 0]], [0.6736, [3, -0.466667, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.666667, 0]],
	[0.6736, [3, -0.666667, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.312, [3, -0.6, 0], [3, 0, 0]]
	]
	],

	# names.append("RShoulderPitch")
	# times.append([1.8, 3.6, 5.4, 6.8, 8.6, 10.4, 12.2, 14, 15.8, 17.6, 19.4, 21.2, 23.2, 25, 26.8, 28.6, 30.4, 32.2, 34, 35.8, 37.6, 39.4])
	# keys.append([[-0.754686, [3, -0.6, 0], [3, 0.6, 0]], [-1.00319, [3, -0.6, 0.0230104], [3, 0.6, -0.0230104]], [-1.0262, [3, -0.6, 0], [3, 0.466667, 0]], [-1.00319, [3, -0.466667, 0], [3, 0.6, 0]], [-1.0262, [3, -0.6, 0], [3, 0.6, 0]], [-1.00319, [3, -0.6, 0], [3, 0.6, 0]], [-1.0262, [3, -0.6, 0], [3, 0.6, 0]], [-1.00319, [3, -0.6, 0], [3, 0.6, 0]], [-1.0262, [3, -0.6, 0], [3, 0.6, 0]], [-1.00319, [3, -0.6, 0], [3, 0.6, 0]], [-1.0262, [3, -0.6, 0], [3, 0.6, 0]], [-1.00319, [3, -0.6, 0], [3, 0.666667, 0]], [-1.0262, [3, -0.666667, 0], [3, 0.6, 0]], [-1.00319, [3, -0.6, 0], [3, 0.6, 0]], [-1.0262, [3, -0.6, 0], [3, 0.6, 0]], [-1.00319, [3, -0.6, 0], [3, 0.6, 0]], [-1.0262, [3, -0.6, 0], [3, 0.6, 0]], [-1.00319, [3, -0.6, 0], [3, 0.6, 0]], [-1.0262, [3, -0.6, 0], [3, 0.6, 0]], [-1.00319, [3, -0.6, 0], [3, 0.6, 0]], [-1.0262, [3, -0.6, 0], [3, 0.6, 0]], [-0.754686, [3, -0.6, 0], [3, 0, 0]]])
	["RShoulderPitch",
	[1.8, 3.6, 5.4, 6.8, 8.6, 10.4, 12.2, 14, 15.8, 17.6, 19.4, 21.2, 23.2, 25, 26.8, 28.6, 30.4, 32.2, 34, 35.8, 37.6, 39.4],
	[
	[-0.754686, [3, -0.6, 0], [3, 0.6, 0]], [-1.00319, [3, -0.6, 0.0230104], [3, 0.6, -0.0230104]], [-1.0262, [3, -0.6, 0], [3, 0.466667, 0]], [-1.00319, [3, -0.466667, 0], [3, 0.6, 0]], [-1.0262, [3, -0.6, 0], [3, 0.6, 0]], [-1.00319, [3, -0.6, 0], [3, 0.6, 0]], [-1.0262, [3, -0.6, 0], [3, 0.6, 0]], [-1.00319, [3, -0.6, 0], [3, 0.6, 0]], [-1.0262, [3, -0.6, 0], [3, 0.6, 0]], [-1.00319, [3, -0.6, 0], [3, 0.6, 0]], [-1.0262, [3, -0.6, 0], [3, 0.6, 0]], [-1.00319, [3, -0.6, 0], [3, 0.666667, 0]],
	[-1.0262, [3, -0.666667, 0], [3, 0.6, 0]], [-1.00319, [3, -0.6, 0], [3, 0.6, 0]], [-1.0262, [3, -0.6, 0], [3, 0.6, 0]], [-1.00319, [3, -0.6, 0], [3, 0.6, 0]], [-1.0262, [3, -0.6, 0], [3, 0.6, 0]], [-1.00319, [3, -0.6, 0], [3, 0.6, 0]], [-1.0262, [3, -0.6, 0], [3, 0.6, 0]], [-1.00319, [3, -0.6, 0], [3, 0.6, 0]], [-1.0262, [3, -0.6, 0], [3, 0.6, 0]], [-0.754686, [3, -0.6, 0], [3, 0, 0]]
	]
	],

	# names.append("RShoulderRoll")
	# times.append([1.8, 3.6, 5.4, 6.8, 8.6, 10.4, 12.2, 14, 15.8, 17.6, 19.4, 21.2, 23.2, 25, 26.8, 28.6, 30.4, 32.2, 34, 35.8, 37.6, 39.4])
	# keys.append([[-0.289967, [3, -0.6, 0], [3, 0.6, 0]], [-0.691876, [3, -0.6, 0], [3, 0.6, 0]], [0.309826, [3, -0.6, 0], [3, 0.466667, 0]], [-0.691876, [3, -0.466667, 0], [3, 0.6, 0]], [0.309826, [3, -0.6, 0], [3, 0.6, 0]], [-0.691876, [3, -0.6, 0], [3, 0.6, 0]], [0.309826, [3, -0.6, 0], [3, 0.6, 0]], [-0.691876, [3, -0.6, 0], [3, 0.6, 0]], [0.309826, [3, -0.6, 0], [3, 0.6, 0]], [-0.691876, [3, -0.6, 0], [3, 0.6, 0]], [0.309826, [3, -0.6, 0], [3, 0.6, 0]], [-0.691876, [3, -0.6, 0], [3, 0.666667, 0]], [0.309826, [3, -0.666667, 0], [3, 0.6, 0]], [-0.691876, [3, -0.6, 0], [3, 0.6, 0]], [0.309826, [3, -0.6, 0], [3, 0.6, 0]], [-0.691876, [3, -0.6, 0], [3, 0.6, 0]], [0.309826, [3, -0.6, 0], [3, 0.6, 0]], [-0.691876, [3, -0.6, 0], [3, 0.6, 0]], [0.309826, [3, -0.6, 0], [3, 0.6, 0]], [-0.691876, [3, -0.6, 0], [3, 0.6, 0]], [0.309826, [3, -0.6, 0], [3, 0.6, 0]], [-0.289967, [3, -0.6, 0], [3, 0, 0]]])
	["RShoulderRoll",
	[1.8, 3.6, 5.4, 6.8, 8.6, 10.4, 12.2, 14, 15.8, 17.6, 19.4, 21.2, 23.2, 25, 26.8, 28.6, 30.4, 32.2, 34, 35.8, 37.6, 39.4],
	[
	[-0.289967, [3, -0.6, 0], [3, 0.6, 0]], [-0.691876, [3, -0.6, 0], [3, 0.6, 0]], [0.309826, [3, -0.6, 0], [3, 0.466667, 0]], [-0.691876, [3, -0.466667, 0], [3, 0.6, 0]], [0.309826, [3, -0.6, 0], [3, 0.6, 0]], [-0.691876, [3, -0.6, 0], [3, 0.6, 0]], [0.309826, [3, -0.6, 0], [3, 0.6, 0]], [-0.691876, [3, -0.6, 0], [3, 0.6, 0]], [0.309826, [3, -0.6, 0], [3, 0.6, 0]], [-0.691876, [3, -0.6, 0], [3, 0.6, 0]], [0.309826, [3, -0.6, 0], [3, 0.6, 0]],
	[-0.691876, [3, -0.6, 0], [3, 0.666667, 0]], [0.309826, [3, -0.666667, 0], [3, 0.6, 0]], [-0.691876, [3, -0.6, 0], [3, 0.6, 0]], [0.309826, [3, -0.6, 0], [3, 0.6, 0]], [-0.691876, [3, -0.6, 0], [3, 0.6, 0]], [0.309826, [3, -0.6, 0], [3, 0.6, 0]], [-0.691876, [3, -0.6, 0], [3, 0.6, 0]], [0.309826, [3, -0.6, 0], [3, 0.6, 0]], [-0.691876, [3, -0.6, 0], [3, 0.6, 0]], [0.309826, [3, -0.6, 0], [3, 0.6, 0]], [-0.289967, [3, -0.6, 0], [3, 0, 0]]
	]
	],

	# names.append("RWristYaw")
	# times.append([1.8, 3.6, 5.4, 6.8, 8.6, 10.4, 12.2, 14, 15.8, 17.6, 19.4, 21.2, 23.2, 25, 26.8, 28.6, 30.4, 32.2, 34, 35.8, 37.6, 39.4])
	# keys.append([[0.0705221, [3, -0.6, 0], [3, 0.6, 0]], [-0.428028, [3, -0.6, 0.113005], [3, 0.6, -0.113005]], [-0.607505, [3, -0.6, 0], [3, 0.466667, 0]], [-0.428028, [3, -0.466667, 0], [3, 0.6, 0]], [-0.607505, [3, -0.6, 0], [3, 0.6, 0]], [-0.428028, [3, -0.6, 0], [3, 0.6, 0]], [-0.607505, [3, -0.6, 0], [3, 0.6, 0]], [-0.428028, [3, -0.6, 0], [3, 0.6, 0]], [-0.607505, [3, -0.6, 0], [3, 0.6, 0]], [-0.428028, [3, -0.6, 0], [3, 0.6, 0]], [-0.607505, [3, -0.6, 0], [3, 0.6, 0]], [-0.428028, [3, -0.6, 0], [3, 0.666667, 0]], [-0.607505, [3, -0.666667, 0], [3, 0.6, 0]], [-0.428028, [3, -0.6, 0], [3, 0.6, 0]], [-0.607505, [3, -0.6, 0], [3, 0.6, 0]], [-0.428028, [3, -0.6, 0], [3, 0.6, 0]], [-0.607505, [3, -0.6, 0], [3, 0.6, 0]], [-0.428028, [3, -0.6, 0], [3, 0.6, 0]], [-0.607505, [3, -0.6, 0], [3, 0.6, 0]], [-0.428028, [3, -0.6, 0], [3, 0.6, 0]], [-0.607505, [3, -0.6, 0], [3, 0.6, 0]], [0.0705221, [3, -0.6, 0], [3, 0, 0]]])
	["RWristYaw",
	[1.8, 3.6, 5.4, 6.8, 8.6, 10.4, 12.2, 14, 15.8, 17.6, 19.4, 21.2, 23.2, 25, 26.8, 28.6, 30.4, 32.2, 34, 35.8, 37.6, 39.4],
	[
	[0.0705221, [3, -0.6, 0], [3, 0.6, 0]], [-0.428028, [3, -0.6, 0.113005], [3, 0.6, -0.113005]], [-0.607505, [3, -0.6, 0], [3, 0.466667, 0]], [-0.428028, [3, -0.466667, 0], [3, 0.6, 0]], [-0.607505, [3, -0.6, 0], [3, 0.6, 0]], [-0.428028, [3, -0.6, 0], [3, 0.6, 0]], [-0.607505, [3, -0.6, 0], [3, 0.6, 0]], [-0.428028, [3, -0.6, 0], [3, 0.6, 0]], [-0.607505, [3, -0.6, 0], [3, 0.6, 0]], [-0.428028, [3, -0.6, 0], [3, 0.6, 0]], [-0.607505, [3, -0.6, 0], [3, 0.6, 0]],
	[-0.428028, [3, -0.6, 0], [3, 0.666667, 0]], [-0.607505, [3, -0.666667, 0], [3, 0.6, 0]], [-0.428028, [3, -0.6, 0], [3, 0.6, 0]], [-0.607505, [3, -0.6, 0], [3, 0.6, 0]], [-0.428028, [3, -0.6, 0], [3, 0.6, 0]], [-0.607505, [3, -0.6, 0], [3, 0.6, 0]], [-0.428028, [3, -0.6, 0], [3, 0.6, 0]], [-0.607505, [3, -0.6, 0], [3, 0.6, 0]], [-0.428028, [3, -0.6, 0], [3, 0.6, 0]], [-0.607505, [3, -0.6, 0], [3, 0.6, 0]], [0.0705221, [3, -0.6, 0], [3, 0, 0]]
	]
	]

]









##############################################################
# MOTION DATA LISTS
##############################################################


ArmMovementList = [UpperArmMovements]

##############################################################





import argparse
from naoqi import ALProxy
from pprint import pprint

def main(robotIP, PORT=9559):
    """ Simple code to test above motion data. """
    # Choregraphe simplified export in Python.
    motion  = ALProxy("ALMotion", robotIP, PORT)
    posture = ALProxy("ALRobotPosture", robotIP, PORT)

	# testList = upArms
    # testList = leftArmMovementList
    testList = ArmMovementList

    bezier = True

    motion.wakeUp()
    # posture.goToPosture("StandInit", 0.8)


    for i in range(len(testList)):
        names = list()
        times = list()
        keys = list()

        for n, t, k in testList[i]:
            names.append(n)
            times.append(t)
            keys.append(k)

        if bezier:
            motion.angleInterpolationBezier(names, times, keys)
        else:
            motion.angleInterpolation(names, keys, times, True)


    # Go to rest position
    motion.rest()



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="169.254.199.42", help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559, help="Robot port number")
    args = parser.parse_args()
    main(args.ip, args.port)
