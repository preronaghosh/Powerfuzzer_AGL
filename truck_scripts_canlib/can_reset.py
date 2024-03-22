from canlib import canlib

def reset_can_bus(channel):
    try:
        # Initialize the Kvaser API
        cl = canlib

        # Open the specified channel (replace '0' with the desired channel number)
        ch = cl.openChannel(channel)

        # Set the channel to active
        ch.setBusOutputControl(canlib.Driver.NORMAL)
        ch.busOn()

        # Turn off the CAN bus
        ch.busOff()

        # Delay for a short period (optional, for stabilization)
        import time
        time.sleep(0.1)  # Adjust the delay time as needed

        # Turn on the CAN bus again
        ch.busOn()

        print("CAN bus reset successfully")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        # Close the channel when done
        ch.busOff()
        ch.close()

if __name__ == "__main__":
    # Specify the channel number (replace '0' with the desired channel)
    channel = 0

    # Reset the CAN bus
    reset_can_bus(channel)