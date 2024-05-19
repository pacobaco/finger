import telnetlib
import time

class TelnetScreen:
    def __init__(self, host, port=23):
        self.host = host
        self.port = port
        self.connection = None
        self.screen_content = ""

    def connect(self):
        try:
            self.connection = telnetlib.Telnet(self.host, self.port)
            self.read_initial_screen()
        except Exception as e:
            print(f"Failed to connect to {self.host}:{self.port} - {e}")

    def read_initial_screen(self):
        if self.connection:
            self.screen_content = self.connection.read_until(b"\n", timeout=10).decode('ascii')

    def send_command(self, command):
        if self.connection:
            self.connection.write(command.encode('ascii') + b"\n")
            time.sleep(2)  # Wait for the server to respond
            self.update_screen_content()

    def update_screen_content(self):
        if self.connection:
            self.screen_content += self.connection.read_very_eager().decode('ascii')

    def get_screen_content(self):
        return self.screen_content

    def close(self):
        if self.connection:
            self.connection.close()

    def input_command(self):
        command = input("Enter command: ")
        self.send_command(command)
        print("Screen content after sending command:")
        print(self.get_screen_content())

class BTreeNode:
    def __init__(self, telnet_screen):
        self.telnet_screen = telnet_screen
        self.left = None
        self.right = None

class BTree:
    def __init__(self):
        self.root = None

    def add(self, telnet_screen):
        if not self.root:
            self.root = BTreeNode(telnet_screen)
        else:
            self._add(self.root, telnet_screen)

    def _add(self, node, telnet_screen):
        if node.left is None:
            node.left = BTreeNode(telnet_screen)
        elif node.right is None:
            node.right = BTreeNode(telnet_screen)
        else:
            # For simplicity, add to left subtree if both children exist
            self._add(node.left, telnet_screen)

    def traverse(self, node):
        if node:
            print(node.telnet_screen.get_screen_content())
            self.traverse(node.left)
            self.traverse(node.right)

# Usage example
if __name__ == "__main__":
    # Create a TelnetScreen object for locis.gov
    screen1 = TelnetScreen("locis.loc.gov")
    screen1.connect()
    screen1.send_command("help")

    screen2 = TelnetScreen("locis.gov")
    screen2.connect()
    screen2.send_command("info")

    screen3 = TelnetScreen("locis.gov")
    screen3.connect()
    screen3.send_command("status")

    # Create a BTree and add TelnetScreen objects
    tree = BTree()
    tree.add(screen1)
    tree.add(screen2)
    tree.add(screen3)

    # Traverse the tree and print screen contents
    print("Traversing the BTree:")
    tree.traverse(tree.root)

    # Close all Telnet connections
    screen1.close()
    screen2.close()
    screen3.close()
