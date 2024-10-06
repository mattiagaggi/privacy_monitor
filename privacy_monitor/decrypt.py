import os

def setup_sslkeylogfile(path):
    os.environ['SSLKEYLOGFILE'] = path