#!/usr/bin/python

import getopt
import sys
import re

PATTERN = re.compile(r'^import (.*?(CollectionUtils|MapUtils|StringUtils));$', re.M)
utilMap = {
    'CollectionUtils': 'org.apache.commons.collections4.CollectionUtils',
    'MapUtils': 'org.apache.commons.collections4.MapUtils;',
    'StringUtils': 'org.apache.commons.lang3.StringUtils'
}


class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def check(path):
    with open(path, 'r') as handle:
        content = handle.read()
        m = PATTERN.search(content)
        if m is not None:
            choosenUtil = utilMap.get(m.group(2))
            if m.group(1) != choosenUtil:
                print(Bcolors.FAIL + '[error]' + Bcolors.ENDC + ' you should use ' + Bcolors.OKBLUE + choosenUtil + Bcolors.ENDC + ' in ' + Bcolors.FAIL + path + Bcolors.ENDC)
                sys.exit(1)


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "", [])
    except getopt.GetoptError as err:
        sys.exit(2)
    check(args[0])


if __name__ == "__main__":
    main()
