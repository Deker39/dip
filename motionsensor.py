import traceback

from gpiozero import MotionSensor

pir = MotionSensor(16)


def get_sensor():
    try:
        if pir.motion_detected:
            return 1
    except Exception as e:
        traceback.print_exc()
        return "Error: %s. Cannot detect  person " % e
