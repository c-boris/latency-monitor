<h1 align="center">Latency Monitor</h1>
<br>
<p align="center">
  <a href="#overview">Overview</a> &#xa0; | &#xa0;
  <a href="#requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#getting-started">Getting started</a> &#xa0; | &#xa0;
  <a href="#usage">Usage</a> &#xa0; | &#xa0;
  <a href="#testing">Testing</a> &#xa0; | &#xa0;
</p>

## Overview

This project involves creating a Python script that performs an HTTP GET request to a specified URL, logs the response, and checks if the request duration exceeds a given threshold. If the duration exceeds the threshold, a custom exception is raised.

## Requirements

Ensure you have the following tools installed before proceeding:

- [Python](https://www.python.org/downloads/)
- [Git](https://git-scm.com)

## Getting started

Follow these steps to set up and run the script on your local machine:

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the script with the required parameters:
   ```bash
   python3 main.py --protocol <protocol> --hostname <hostname> --uri <uri> --threshold <threshold>
   ```

## Usage

1. **Send an HTTP GET request and handle the response:**

   ```bash
   python3 main.py --protocol https --hostname dummyjson.com --uri /products --threshold 2
   ```

   - `protocol`: The protocol to use (http or https)
   - `hostname`: The hostname of the URL
   - `uri`: The URI of the URL
   - `threshold`: The threshold time in seconds

## Testing

1. Run unit tests using:

   ```bash
   python3 -m unittest test_format_url.py
   ```

   The test checks the format_url function to ensure it correctly formats the URL.
   <br>

<a href="#top">Back to top</a>
