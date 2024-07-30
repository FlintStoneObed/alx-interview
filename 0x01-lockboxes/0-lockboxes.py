#!/usr/bin/python3

def canUnlockAll(boxes):
    if not boxes:
        return True

    unlocked = {0}
    keys = [0]

    while keys:
        key = keys.pop()
        for k in boxes[key]:
            if k not in unlocked:
                unlocked.add(k)
                keys.append(k)

    return len(unlocked) == len(boxes)

