import serial.tools.list_ports


def main() -> None:
    ports = serial.tools.list_ports.comports()
    for p in ports:
        print(f"{p.description} : {p.name} : '{p.hwid}'")


if __name__ == "__main__":
    main()