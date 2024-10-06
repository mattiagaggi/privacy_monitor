import pyshark

def start_capture(interface, display_filter, duration):
    capture = pyshark.LiveCapture(interface=interface, display_filter=display_filter)
    capture.sniff(timeout=duration)
    return capture