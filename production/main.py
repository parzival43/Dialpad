
from machine import ADC, Pin
import time

adc = ADC(Pin(26))

BUTTON_LEVELS = {
    "BTN1": 8000,
    "BTN2": 16000,
    "BTN3": 24000,
    "BTN4": 32000,
    "BTN5": 40000,
    "BTN6": 48000,
}

TOLERANCE = 2500
SAMPLE_COUNT = 8
DEBOUNCE_MS = 35
POLL_MS = 5


def read_adc():
    total = 0
    for _ in range(SAMPLE_COUNT):
        total += adc.read_u16()
        time.sleep_ms(1)
    return total // SAMPLE_COUNT


def identify_button(value):
    if value < 1500:
        return None

    closest_name = None
    closest_error = None

    for name, target in BUTTON_LEVELS.items():
        error = abs(value - target)
        if closest_error is None or error < closest_error:
            closest_name = name
            closest_error = error

    if closest_error is not None and closest_error <= TOLERANCE:
        return closest_name

    return None


stable_button = None
candidate_button = None
candidate_since = time.ticks_ms()

