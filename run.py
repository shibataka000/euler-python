# coding: utf-8

import argparse
import importlib


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("problem_number")
    args = parser.parse_args()

    path_to_module = "problems.problem{}".format(args.problem_number.zfill(3))
    problem = importlib.import_module(path_to_module)

    ans = problem.solve()
    print(ans)
