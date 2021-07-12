#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import argparse

import logzero

import settings


class Main:
    def __init__(self):
        logzero.logfile(settings.logfile, loglevel=20, maxBytes=1e6, backupCount=3)
        self.logger = logzero.logger

    def main(self, args):
        self.logger.info(args)
        self.execute()

    def execute(self):
        return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", action="version", version=f"{__version__}")
    parser.add_argument("--option", default="option")
    Main().main(parser.parse_args())
