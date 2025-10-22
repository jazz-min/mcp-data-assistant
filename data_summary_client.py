from fastmcp import Client
import asyncio
import json

# Initialize the MCP client
client = Client("data_summary_server.py")


# Function to test all tools in a single connection
async def test_all_tools(file_path: str, row_count: int):
    async with client:
        # Test summarize_data tool
        response = await client.call_tool("summarize_data", {"file_path": file_path})
        summarize_result = response.structured_content
        print("Summarize Data Result:")
        print(json.dumps(summarize_result, indent=4))

        # Test get_top_rows tool
        response = await client.call_tool("get_top_rows", {"file_path": file_path, "n": row_count})
        top_rows_result = response.content[0].text
        print(f"Top {row_count} Rows Result:")
        print(json.dumps(top_rows_result, indent=4))

        # Test detect_missing tool
        response = await client.call_tool("detect_missing", {"file_path": file_path})
        missing_values_result = response.structured_content
        print("Detect Missing Values Result:")
        print(json.dumps(missing_values_result, indent=4))

# Example usage
if __name__ == "__main__":
    file_path = input("Enter the path to your CSV file: ")
    row_count = input("Enter the number of rows for the top rows tool (default is 5): ")
    row_count = int(row_count) if row_count.strip() else 5
    asyncio.run(test_all_tools(file_path,row_count))