import requests
import logging
import time


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