# client.py
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    # Launch the server process with STDIO
    params = StdioServerParameters(command="python", args=["server.py"])
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            # Perform the MCP handshake
            await session.initialize()
            # Call the "sum" tool we registered on the server
            result = await session.call_tool("sum", {"a": 3, "b": 4})
            # The result content is a list of TextContent blocks
            print("Tool output:", result.content[0].text)  # e.g. "7"
            # Read the greeting resource
            greet = await session.read_resource("greeting://Alice")
            print("Greeting:", greet.contents[0].text)  # e.g. "Hello, Alice!"

asyncio.run(main())
