# import can

# # Define the CAN message
# can_id = 0x123  # CAN message ID
# data = [0x01, 0x02, 0x03, 0x04]  # Data bytes

# # Create a CAN message object
# message = can.Message(
#     arbitration_id=can_id,
#     data=data,
#     # extended_id=True  # Set to True if using extended IDs
# )

# # Create a CAN bus interface (replace 'kvaser' with the actual interface name)
# # You can list available interfaces using can.interfaces.list_interfaces()
# bus = can.interface.Bus(bustype='kvaser', channel=0, bitrate=250000)  # Adjust channel and bitrate

# try:
#     # Send the CAN message
#     bus.send(message)
#     print(f"Message sent: ID={message.arbitration_id}, Data={message.data}")
# except can.CanError:
#     print("Error sending CAN message")

# # Close the CAN bus when done
# bus.shutdown()


from canlib import canlib, Frame

def send_can_command(channel, can_id, data):
    try:
        # Initialize the Kvaser API
        cl = canlib

        # Open the specified channel (replace '0' with the desired channel number)
        ch = cl.openChannel(channel)

        # Set the channel to active
        ch.setBusParams(canlib.canBITRATE_250K)
        ch.setBusOutputControl(canlib.Driver.NORMAL)
        ch.busOn()

        # Create a CAN message object
        msg = Frame(id_=can_id,data=data)
        # msg.id = can_id
        # msg.data = data

        # Send the CAN message
        ch.write(msg)

        print(f"Sent CAN message: ID={msg.id}, Data={msg.data}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        # Close the channel when done
        ch.busOff()
        ch.close()

if __name__ == "__main__":
    # Specify the channel number (replace '0' with the desired channel)
    channel = 0

    # Define the CAN message
    can_id = 0x123  # CAN message ID
    data = [0x01, 0x02, 0x03, 0x04]  # Data bytes

    # Send the CAN command
    send_can_command(channel, can_id, data)
