#  AI Data Assistant using FastMCP
An AI-powered Data Assistant built using the FastMCP framework, capable of analyzing CSV datasets through standardized Model Context Protocol (MCP) tools.
This project demonstrates how AI clients can securely connect to external data tools — summarizing, inspecting, and detecting issues in datasets using a consistent MCP interface.
## Features
* **Summarize CSV files**: Summarizes the given CSV file — reports row and column counts, and provides descriptive statistics for all numeric columns.
* **Show top rows of data**:  Returns the top N rows of a dataset (default = 5). Useful for a quick preview of the data.
* **Detect Missing Values**: Checks for missing values in each column and reports counts. 

## Run
```
pip install -r requirements.txt
python data_summary_server.py
```
This starts the FastMCP server exposing your data tools via the MCP protocol.

## Client Interaction
To test locally, you can use the provided client script:
```
python data_summary_client.py 
```