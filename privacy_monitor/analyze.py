def process_packets(capture):
    for packet in capture:
        if 'tls' in packet:
            # Process TLS packets
            pass
        if 'http' in packet:
            # Process HTTP packets
            pass