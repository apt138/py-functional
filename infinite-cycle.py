from itertools import cycle
import time


def traffic_signal_simulation():
    tl_config = [
        ("🔴", 2),
        ("🟢", 2),
        ("🟡", 1),
    ]
    while True:
        state = cycle(tl_config)
        color, duration = next(state)
        print(f"Traffic signal is {color}")
        time.sleep(duration)
