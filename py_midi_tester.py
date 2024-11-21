import mido
import time

# Function to send a MIDI message and check for a response
def send_and_check_response(message):
    outport.send(message)
    time.sleep(0.1)  # Wait for a response
    for msg in inport.iter_pending():
        if msg.type == 'control_change' or msg.type == 'program_change':
            return True
    return False

# Function to verify all MIDI commands for all channels
def verify_midi_commands():
    for channel in range(16):
        print(f"Channel {channel + 1}")

        # Lists to store verified program changes and control changes
        verified_program_changes = []
        verified_control_changes = []

        # Loop through all possible program change messages
        for program in range(128):
            msg = mido.Message('program_change', program=program, channel=channel)
            if send_and_check_response(msg):
                verified_program_changes.append(program)

        # Loop through all possible control change messages
        for control in range(128):
            for value in range(128):
                msg = mido.Message('control_change', control=control, value=value, channel=channel)
                if send_and_check_response(msg):
                    verified_control_changes.append((control, value))

        # Print the verified program changes and control changes for the current channel
        print(f"Verified Program Changes for Channel {channel + 1}: {verified_program_changes}")
        print(f"Verified Control Changes for Channel {channel + 1}: {verified_control_changes}")

# Function to print input and output names
def print_midi_ports():
    output_names = mido.get_output_names()
    input_names = mido.get_input_names()
    
    print("MIDI Output Ports:")
    for name in output_names:
        print(name)
    
    print("\nMIDI Input Ports:")
    for name in input_names:
        print(name)

# Open the MIDI output and input ports
outport = mido.open_output('Your MIDI Interface Name')
inport = mido.open_input('Your MIDI Interface Name')

# Call the function to print MIDI ports
print_midi_ports()

# Call the function to verify MIDI commands
verify_midi_commands()
