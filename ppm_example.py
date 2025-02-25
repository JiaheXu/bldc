from pyvesc import VESC
import time

# serial port that VESC is connected to. Something like "COM3" for windows and as below for linux/mac
serial_port = '/dev/ttyACM0'


# a function to show how to use the class with a with-statement
def run_motor_using_with():
    with VESC(serial_port=serial_port) as motor:
        print("Firmware: ", motor.get_firmware_version())
        motor.set_duty_cycle(0.02)

        # run motor and print out rpm for ~2 seconds
        for i in range(300):
            time.sleep(0.01)
            # print(motor.get_measurements().rpm)
            motor.set_rpm(100000)


# a function to show how to use the class as a static object.
def run_motor_as_object():
    motor = VESC(serial_port=serial_port)
    print("Firmware: ", motor.get_firmware_version())

    # sweep servo through full range
    for i in range(100000):
        time.sleep(0.05)
        mul = i // 100
        val = 0.0
        if(mul % 2 == 0):
            val = (i%100)
        else:
            val = 100 - (i%100)
        val = val / 100
        #print(val)
        motor.set_servo( val )
        #motor.set_servo(int(1000))
        
    # IMPORTANT: YOU MUST STOP THE HEARTBEAT IF IT IS RUNNING BEFORE IT GOES OUT OF SCOPE. Otherwise, it will not
    #            clean-up properly.
    motor.stop_heartbeat()


def time_get_values():
    with VESC(serial_port=serial_port) as motor:
        start = time.time()
        motor.get_measurements()
        stop = time.time()
        print("Getting values takes ", stop-start, "seconds.")


if __name__ == '__main__':
    # run_motor_using_with()
    run_motor_as_object()
    time_get_values()
