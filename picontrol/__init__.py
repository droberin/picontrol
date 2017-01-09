from time import sleep
import os.path

class PiControl:
    device = None
    comment = "No comment"
    GPIO_pin = None
    miao = "rules"

    def open_drawer(self, sequence=None, drawer_number=1):
        default_drawer_device = "/dev/usb/lp0"
        status = None
        if not sequence:
            print("No sequence found using default")
            if drawer_number is 1:
                sequence = chr(27) + chr(112) + chr(0), chr(50), chr(250)
            else:
                sequence = chr(27) + chr(112) + chr(1), chr(50), chr(250)
        if not self.device:
            print("No device defined, trying default '{}'".format(default_drawer_device))
            self.device = default_drawer_device
        else:
            if not self.device.startswith("/dev/"):
                print("Selected device '{}' is not in /dev/".format(self.device))
                return False

        print("Opening drawer using defined sequence")

        if not os.path.isfile(self.device):
            print("File '{}' not found".format(self.device))
            return False

        try:
            drawer = open(self.device, "wb")
            drawer.write(sequence)
            drawer.flush()
            drawer.close()
            status = True
        except PermissionError:
            print("ERROR: Permission denied trying to use '{}'".format(self.device))
            status = False
        except FileNotFoundError:
            print("ERROR: File not found '{}'".format(self.device))
        finally:
            return status

    def open_door(self, status: int=1, duration: int=4,):
        if not self.GPIO_pin:
            print("Can't open any door without knowing which GPIO port to HIGH")
            return False
        print("Setting pin {} to {} for {} seconds".format(self.GPIO_pin, status,duration))
        # TODO: activate relay
        sleep(duration)
        # TODO: deactivate relay
        return True

    def set_io_pin(self, pin=None,):
        if pin:
            self.GPIO_pin = pin
            print("GPIO Pin set to PIN '{}'".format(str(pin)))
        else:
            print("No GPIO set. Parameter 'pin' was expected")

    def __init__(self, device=None,):
        if device:
            self.device = device
