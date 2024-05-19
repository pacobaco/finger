import re
from itertools import groupby

def find_common_prefix(strings):
    """
    Finds the longest common prefix in a list of strings.
    """
    if not strings:
        return ""
    prefix = strings[0]
    for string in strings[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                break
    return prefix

def find_common_suffix(strings):
    """
    Finds the longest common suffix in a list of strings.
    """
    reversed_strings = [s[::-1] for s in strings]
    reversed_prefix = find_common_prefix(reversed_strings)
    return reversed_prefix[::-1]

def generate_regex_pattern(samples):
    """
    Generates a regex pattern that matches all the given sample strings.
    """
    if not samples:
        return ""

    # Find common prefix and suffix
    common_prefix = find_common_prefix(samples)
    common_suffix = find_common_suffix(samples)
    
    # Strip common prefix and suffix from samples
    stripped_samples = [s[len(common_prefix):-len(common_suffix) if common_suffix else None] for s in samples]
    
    # Find the unique parts and generate regex pattern for them
    unique_parts = set(stripped_samples)
    
    # Construct the regex pattern
    unique_pattern = '|'.join(re.escape(part) for part in unique_parts)
    if len(unique_parts) > 1:
        unique_pattern = f"({unique_pattern})"
    
    # Combine common prefix, unique pattern, and common suffix into the final pattern
    regex_pattern = re.escape(common_prefix) + unique_pattern + re.escape(common_suffix)
    
    return regex_pattern

def main():
    # Sample data
    samples = [
        "file1.txt",
        "file2.txt",
        "file3.txt",
        "file10.txt"
    ]
    
    # Generate regex pattern
    regex_pattern = generate_regex_pattern(samples)
    
    # Compile the regex pattern
    pattern = re.compile(regex_pattern)
    
    # Validate the pattern against the sample data
    for sample in samples:
        if pattern.match(sample):
            print(f"Matched: {sample}")
        else:
            print(f"Did not match: {sample}")
    
    # Print the generated regex pattern
    print(f"Generated regex pattern: {regex_pattern}")

if __name__ == "__main__":
    main()
