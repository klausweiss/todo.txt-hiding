#!/usr/bin/env python3
"""
filter incoming lines based on keywords (contexts/projects) we want to hide
"""

from subprocess import getstatusoutput
import sys


def main(todo_sh, to_hide):
    todos = getstatusoutput("{} ls".format(todo_sh))[1].split('\n')
    todos.pop()
    tasks = 0
    for line in todos:
        if all(keyword not in line for keyword in to_hide.split()):
            print(line)
            tasks += 1
    print("TODO: {} of {} tasks shown".format(tasks, len(todos) - 1))
    return True


if __name__ == '__main__':
    status = not main(*sys.argv[1:])
    sys.exit(status)
