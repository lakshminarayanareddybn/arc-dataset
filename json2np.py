import os
import numpy as np
import json
import glob

def pad_to(image, dims):
    pad_width = tuple((0, d - i) for d, i in zip(dims, image.shape))
    return np.pad(image+1, pad_width)

data = {}

for split in ['training', 'evaluation']:
    tasks = []
    for training_file_name in glob.glob('{}/*.json'.format(split)):
        with open(training_file_name) as f:
            task = json.load(f)
        task_np = np.zeros((2, 2, 10, 30, 30), dtype=np.uint8)
        for i, problem in enumerate(task['train']):
            input = pad_to(np.array(problem['input'], dtype=np.uint8), (30, 30))
            output = pad_to(np.array(problem['output'], dtype=np.uint8), (30, 30))
            task_np[0, 0, i] = input
            task_np[0, 1, i] = output
        for i, problem in enumerate(task['test']):
            input = pad_to(np.array(problem['input'], dtype=np.uint8), (30, 30))
            output = pad_to(np.array(problem['output'], dtype=np.uint8), (30, 30))
            task_np[1, 0, i] = input
            task_np[1, 1, i] = output
        tasks.append(task_np)
    data[split] = np.array(tasks, dtype=np.uint8)

np.savez_compressed("arc.npz", **data)
