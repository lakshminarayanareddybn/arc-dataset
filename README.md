# arc-dataset

From: https://github.com/fchollet/ARC

Includes a processing script to convert JSON to numpy array.

arc.npz contains two arrays ('training', 'evaluation') with shapes [400, 2, 2, 10, 30, 30]. This is what each axis means:
[number of tasks, train/test, input/output, number of problems, padded vertical axis, padded horizontal axis]
