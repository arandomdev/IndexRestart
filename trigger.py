import enum
import json
import pathlib
import time
import webbrowser

import serial.tools.list_ports

BAUD_RATE = 9600
PACKET_SIZE = 1


class Command(enum.Enum):
    Trigger = b"T"
    Heartbeat = b"H"
    ACK = b"A"


def main() -> None:
    config = json.loads(pathlib.Path(__file__).with_name("config.json").read_text())
    hwid = config["hwid"]

    # Get port name
    ports = serial.tools.list_ports.comports()
    target = next((p for p in ports if p.hwid == hwid), None)
    if target is None:
        raise RuntimeError("Unable to find device with hardware ID")

    # Trigger
    with serial.Serial(target.device, BAUD_RATE, timeout=4) as ser:
        ser.write(Command.Trigger.value)
        packet = ser.read(PACKET_SIZE)
        if Command(packet) != Command.ACK:
            raise RuntimeError("Did not get a ACK response")

    time.sleep(5)

    # Open SteamVR
    webbrowser.open("steam://rungameid/250820")


if __name__ == "__main__":
    main()
