#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import json
import os

import pandas


def load_json(path):
    with open(_build_path(path), "r") as conf:
        return json.load(conf)


def load_tsv(path):
    return pandas.read_csv.load(_build_path(path))


def _build_path(path):
    dir = os.getcwd()
    abspath = os.path.abspath(os.path.join(dir, path))

    if os.path.exists(abspath):
        return abspath
    else:
        raise FileNotFoundError(abspath)


settings_dict = load_json("./config/settings.json")
logfile = settings_dict["logfile"]
