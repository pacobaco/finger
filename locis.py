import telnetlib
import time

# Define the host and port
HOST = "loc.gov"
PORT = 23

# Create a Telnet object
tn = telnetlib.Telnet(HOST, PORT)

# Read the welcome message (initial screen content)
initial_screen = tn.read_until(b"\n", timeout=10).decode('ascii')
print("Initial screen content:")
print(initial_screen)

# Depending on the server's prompt and responses, you might need to send certain commands.
# For demonstration, let's assume we need to send 'help' command to get the next screen.
tn.write(b"help\n")

# Allow some time for the server to respond
time.sleep(2)

# Read the screen content after sending the command
next_screen = tn.read_very_eager().decode('ascii')
print("Next screen content:")
print(next_screen)

# Close the Telnet connection
tn.close()

# You can add parsing logic here based on your needs
# For example, extracting specific information from the screen content
