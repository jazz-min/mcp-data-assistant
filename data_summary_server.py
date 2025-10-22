from fastmcp import FastMCP
import pandas as pd

mcp = FastMCP("Data Summary Server")
@mcp.tool
def summarize_data(file_path: str) -> dict:
    """Summarizes the given CSV data and returns row/column count and numeric stats."""
    df = pd.read_csv(file_path)
    return {
        "rows": len(df),
        "columns": list(df.columns),
        "stats": df.describe().to_dict()
    }
@mcp.tool
def get_top_rows(file_path: str, n: int = 5):
    """Return top N rows of a dataset."""
    df = pd.read_csv(file_path)
    return  df.head(n).to_dict(orient="records")

@mcp.tool
def detect_missing(file_path: str) -> dict:
    """Check for missing values in each column."""
    df = pd.read_csv(file_path)
    return df.isnull().sum().to_dict()


if __name__ == "__main__":
    mcp.run()
