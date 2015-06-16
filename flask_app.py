#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

SRC = '/home/codio/workspace/src/'

@app.before_first_request
def empty_output_files():
    # TODO blank out all the output files
    print('hook before first request')
    pass


def run_tests_and_output_results(exercise_dir):

    command = 'python3 {}tests.py'.format(exercise_dir)

    test = subprocess.Popen(
        command, 
        shell=True, 
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )

    stdout, stderr = test.communicate()

    output_fname = '{}output.txt'.format(exercise_dir)
    with open(output_fname, 'wb') as fp:
        # fp.write(stdout)
        fp.write(stderr)


@app.route("/hi")
def hi():

    ex_dir = '{}hi/'.format(SRC)
    run_tests_and_output_results(ex_dir)

    return 'ok'


@app.route("/hi_name")
def hi_name():

    ex_dir = '{}hi_name/'.format(SRC)
    run_tests_and_output_results(ex_dir)

    return 'ok'



if __name__ == "__main__":
    
    import logging
    app_log = '/home/codio/app.log'
    logging.basicConfig(filename=app_log,level=logging.DEBUG)

    app.run(
        host='0.0.0.0', 
        port=9500,
        debug=True,
    )
