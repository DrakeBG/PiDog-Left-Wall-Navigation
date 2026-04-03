#!/usr/bin/env python3
import time
from pidog import Pidog
from pidog.preset_actions import bark

t = time.time()
my_dog = Pidog()
my_dog.do_action('stand', speed=80)
my_dog.wait_all_done()
time.sleep(.1)

DANGER_DISTANCE = 20

stand = my_dog.legs_angle_calculation([[0, 80], [0, 80], [30, 75], [30, 75]])

def patrol():
    distance = round(my_dog.read_distance(), 2)
    print(f"distance: {distance} cm", end="", flush=True)

    # CASE 1: Danger detected ahead
    if 0 < distance < DANGER_DISTANCE:
        print("\033[0;31m DANGER !\033[m")
        my_dog.body_stop()
        head_yaw = my_dog.head_current_angles[0]

        my_dog.rgb_strip.set_mode('bark', 'red', bps=2)
        my_dog.tail_move([[0]], speed=80)
        my_dog.legs_move([stand], speed=70)

        # STEP 2: Pan Head Left to check for a side wall
        print("Status: Panning Left to scan...")
        my_dog.head_move([[15, 0, 0]], immediately=True, speed=60)
        time.sleep(0.1)

        # Re-read distance while looking left
        side_distance = round(my_dog.read_distance(), 2)
        # STEP 3: Logic Branching based on side scan
        if side_distance < DANGER_DISTANCE:
            # Wall detected on the left -> Turn Right to avoid it
            print(f"Left wall detected ({side_distance}cm). Rotating RIGHT.")
            my_dog.do_action('turn_right', step_count=1, speed=90)
        else:
            # No wall on the left -> Turn Left to find a path
            print(f"No left wall ({side_distance}cm). Rotating LEFT.")
            my_dog.do_action('turn_left', step_count=1, speed=90)

        # Reset head
        my_dog.head_move([[0, 0, 0]], immediately=True, speed=60)
        time.sleep(0.1)
        my_dog.wait_all_done()
        bark(my_dog, [head_yaw, 0, 0])

        # REMOVED: The 'while distance < DANGER_DISTANCE' loop has been deleted
        # so the dog returns to the main patrol loop immediately.

    # CASE 2: Path is safe
    else:
        print(" - Path Clear")
        my_dog.rgb_strip.set_mode('breath', 'white', bps=0.5)
        my_dog.do_action('forward', step_count=2, speed=98)
        my_dog.do_action('shake_head', step_count=1, speed=80)
        my_dog.do_action('wag_tail', step_count=5, speed=99)

if __name__ == "__main__":
    try:
        while True:
            patrol()
            time.sleep(0.01)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\033[31mERROR: {e}\033[m")
    finally:
        my_dog.close()
