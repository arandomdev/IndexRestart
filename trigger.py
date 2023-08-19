import enum
import webbrowser

import serial.tools.list_ports

HWID = "USB VID:PID=2341:8036 SER=6&28CF390B&0&9"
BAUD_RATE = 9600
PACKET_SIZE = 1


class Command(enum.Enum):
    Trigger = b"T"
    Heartbeat = b"H"
    ACK = b"A"


def main() -> None:
    # Get port name
    ports = serial.tools.list_ports.comports()
    target = next((p for p in ports if p.hwid == HWID), None)
    if target is None:
        raise RuntimeError("Unable to find device with hardware ID")

    # Trigger
    with serial.Serial(target.device, BAUD_RATE, timeout=4) as ser:
        ser.write(Command.Trigger.value)
        packet = ser.read(PACKET_SIZE)
        if Command(packet) != Command.ACK:
            raise RuntimeError("Did not get a ACK response")

    # Open SteamVR
    webbrowser.open("steam://rungameid/250820")


if __name__ == "__main__":
    main()
