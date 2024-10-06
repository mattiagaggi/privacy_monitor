from capture import start_capture
from decrypt import setup_sslkeylogfile
from analyze import process_packets

def main():
    setup_sslkeylogfile('/path/to/sslkeylog.txt')
    capture = start_capture('eth0', 'tls or http', 60)
    process_packets(capture)

if __name__ == "__main__":
    main()