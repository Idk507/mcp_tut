# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server named "Demo"
mcp = FastMCP("Demo")

# Add a tool that sums two numbers
@mcp.tool()
def sum(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Add a resource with a dynamic greeting (just as an example)
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    return f"Hello, {name}!"

# Run the server (e.g. mount to stdin/stdout or other transport)
mcp.run()  # or use mcp.listen_over_stdio(), etc.
