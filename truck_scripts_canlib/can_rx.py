from canlib import canlib
import binascii

def extract_pgn_from_id(input_decimal):
    # Convert the decimal input to binary representation
    binary_string = bin(input_decimal)[2:]

    # Ensure the binary string has at least 29 bits (add leading zeros if needed)
    while len(binary_string) < 29:
        binary_string = '0' + binary_string

    # Extract bits 8 to 25 from the binary string and convert to decimal
    extracted_binary = binary_string[3:21]
    extracted_decimal = int(extracted_binary, 2)

    return extracted_decimal

def read_can_data(channel):
    try:
        # Initialize the Kvaser API
        cl = canlib

        # Open the specified channel (replace '0' with the desired channel number)
        ch = cl.openChannel(channel)

        # Set the channel to active
        ch.setBusParams(canlib.canBITRATE_250K)  # Adjust the bitrate as needed
        ch.busOn()

        while True:
            # Read a CAN message
            msg = ch.read(timeout=1000)  # Timeout in milliseconds (adjust as needed)

            # if msg.id == 419286321:
            if msg:
                print(f"Received CAN message:id={msg.id}, pgn={extract_pgn_from_id(msg.id)}, Data={binascii.hexlify(msg.data).decode('utf-8')}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        # Close the channel when done
        ch.busOff()
        ch.close()

if __name__ == "__main__":
    # Specify the channel number (replace '0' with the desired channel)
    channel = 0

    # Start reading CAN data
    read_can_data(channel)


# pgn=64993, Data=bytearray(b'\x07\xff\xff\xff\xff\xff\xff\xff')
