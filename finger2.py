import subprocess
import re

def run_command(command):
    """
    Runs a given command in the terminal and returns the output.
    """
    try:
        # Run the command and capture the output
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        result.check_returncode()  # Raises CalledProcessError if the command returned a non-zero exit code
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return None

def scrape_output(output, pattern):
    """
    Scrapes the terminal output using a regular expression pattern.
    """
    matches = re.findall(pattern, output)
    return matches

def main():
    # Example command to run
    command = "ls -l"  # This lists directory contents in long format
    
    # Run the command and get the output
    output = run_command(command)
    
    if output:
        # Define a regex pattern to extract data (e.g., file names)
        pattern = r'^\S+\s+\d+\s+\S+\s+\S+\s+\d+\s+\S+\s+\S+\s+\S+\s+(.+)$'
        
        # Scrape the output using the pattern
        data = scrape_output(output, pattern)
        
        # Print the extracted data
        for item in data:
            print(item)

if __name__ == "__main__":
    main()
