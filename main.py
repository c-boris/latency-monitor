import requests
import logging
import time
import argparse


# Custom exception for threshold exceeding
class ThresholdExceededException(Exception):
    pass

# Function to perform HTTP GET request and handle response
def http_get(url: str, threshold: int):
    start_time = time.monotonic()  # Start the timer
    try:
        # Send the GET request
        response = requests.get(url)
        logging.info(f"HTTP Status Code: {response.status_code}")  # Log status code
        response.raise_for_status()  # Raise an error for bad responses

        elapsed_time = time.monotonic() - start_time  # Measure elapsed time

        # Log the elapsed time
        logging.info(f"Elapsed Time: {elapsed_time:.2f} seconds")

        # Check if elapsed time exceeds the threshold
        if elapsed_time > threshold:
            raise ThresholdExceededException(
                f"Request took {elapsed_time:.2f} seconds, exceeding the threshold of {threshold} seconds"
            )
        
        return response.json()  # Return the response JSON
    except requests.exceptions.HTTPError as http_err:
        logging.critical(f"HTTP error occurred: {http_err}, Status Code: {http_err.response.status_code}")
        raise
    except Exception as err:
        logging.critical(f"Other error occurred: {err}")
        raise
    
    # Function to parse command-line arguments
def get_command_line_args():
    parser = argparse.ArgumentParser(description='Process command-line arguments for HTTP GET request.')
    # Add arguments for protocol, hostname, URI, and threshold
    parser.add_argument('--protocol', type=str, required=True, choices=['http', 'https'], help='Protocol (http or https)')
    parser.add_argument('--hostname', type=str, required=True, help='Hostname')
    parser.add_argument('--uri', type=str, required=True, help='URI')
    parser.add_argument('--threshold', type=int, required=True, help='Threshold in seconds for request duration')

    return parser.parse_args()

# Function to format URL from protocol, hostname, and URI
def format_url(protocol: str, hostname: str, uri: str) -> str:
    return f"{protocol}://{hostname}{uri}"

# Main block to run the script
if __name__ == "__main__":
    # Configure logging settings
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    # Get command-line arguments
    args = get_command_line_args()
    # Format the URL from the arguments
    url = format_url(args.protocol, args.hostname, args.uri)

    try:
        # Perform HTTP GET request and check for threshold violation
        data = http_get(url, args.threshold)
        # Print the response data
        print(data)
    except ThresholdExceededException as te:
        # Log threshold exceeded exceptions at CRITICAL level
        logging.critical(te)
    except Exception as e:
        # Log any other exceptions at CRITICAL level
        logging.critical(f"Failed to get data: {e}")