from canlib import canlib, Frame

def send_can_message(channel, pgn, spn, data):
    try:
        # Initialize the Kvaser API
        cl = canlib

        # Open the specified channel (replace '0' with the desired channel number)
        ch = cl.openChannel(channel)

        # Set the channel to active
        ch.setBusParams(canlib.canBITRATE_250K)
        ch.setBusOutputControl(canlib.Driver.NORMAL)
        ch.busOn()

        can_id = (pgn << 8) | spn
        # Send the CAN message
        msg = Frame(id_ = 419286321, data=data, flags=canlib.MessageFlag.EXT)
        # msg = Frame(id_ = 419286321, data=data)
        print(msg)
        ch.write(msg)

        print(f"Sent CAN message: id = {can_id}, PGN={pgn}, SPN={spn}, Data={data}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        # Close the channel when done
        ch.busOff()
        ch.close()

if __name__ == "__main__":
    # Specify the channel number (replace '0' with the desired channel)
    channel = 0

    # Define the PGN, SPN, and data
    pgn = 0xFDCD  # Parameter Group Number (16-bit)
    spn = 0xB2F    # Specific Parameter Number (8-bit)
    data = bytearray(b'\x4f\xff\xff\xff\xff\xff\xff\xff')
    # data = [0x4f, 0xff, 0xff, 0xff, 0xff,0xff, 0xff, 0xff]  # Data bytes

    # Send the CAN command
    send_can_message(channel, pgn, spn, data)
