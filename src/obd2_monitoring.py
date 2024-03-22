import socket
import struct
import kuksa_viss_client
import can


def process_can_message(msg):
    if msg.arbitration_id == 150892286:
        # vehicle_speed = int.from_bytes(msg.data, byteorder='big') # TODO: check byteorder, check the arbitration_id, these are arbitrary
        print(f"CAN ID: Electronic Engine Controller 1")
    elif msg.arbitration_id == 0x102:
        # Handle other CAN IDs and data decoding here
        pass
    else:
        print(f"Unknown CAN ID")
        
        
def main():
    print("J1939 to Vehicle Signals")
    s = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)

    client = kuksa_viss_client.KuksaClientThread(config={})
    client.start()
    client.authorize("/usr/lib/python3.10/site-packages/kuksa_certificates/jwt/super-admin.json.token") #TODO: confirm if this is needed?
    print("Kuksa Client init... done!")

    # v_temp = 65.0

    try:
        s.bind(('can0',))
    except OSError as e:
        print(f"Bind error: {e}")
        return 1

    print("-------------------------------------------------------------------")


    while True:
        try:
            frame = s.recv(16)  
            
        except KeyboardInterrupt:
            print("User interrupted program..")
            client.stop()
            return 1
            
        except OSError as e:
            print(f"Read error: {e}")
            return 1

        can_id, can_dlc, data = struct.unpack("<IB3x8s", frame)

        print(f"0x{can_id:03X} [{can_dlc}] ", end="")

        # Decode the received frame using python-can
        msg = can.Message(
            arbitration_id=can_id,
            data=data,
            dlc=can_dlc,
            is_extended_id=True  # Assuming standard CAN frames
        )


        # Call the message processing function
        process_can_message(msg)
        
        pgn_id = (can_id >> 8) & 0xFFFF
        can_id_data = can_id & 0xFF
        
        if pgn_id == 0xFEF1:
            print("VehicleSpeed: {}".format(can_id_data))
            client.setValue("Vehicle.Speed", str(can_id_data))
            # v_temp += 10
            
        if pgn_id == 0xFFFF: # update PGN_ID for RPM
            print("RPM: {}".format(can_id_data))
            client.setValue("Vehicle.Powertrain.CombustionEngine.Speed", str(can_id_data))

        print(f"Arbitration ID received: {msg.arbitration_id}")


        print("-------------------------------------------------------------------")
        
        if KeyboardInterrupt:
            print("User interrupted program..")
            client.stop()
            return 1


if __name__ == "__main__":
    exit_code = main()
    exit(exit_code)