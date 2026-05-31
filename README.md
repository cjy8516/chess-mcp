# Chess MCP Server

A Model Context Protocol (MCP) server that provides chess capabilities through the [chess.com](https://www.chess.com) API.

## Installation

### Prerequisites

- [uv](https://github.com/astral-sh/uv) installed on your system.
- Python 3.13 or higher.

### Configuration for MCP Clients

To use this server with an MCP client (like Claude Desktop), add the following configuration to your `mcp_config.json` (or `claude_desktop_config.json`):

#### Using `uvx` (Recommended)

The easiest way to run the server is using `uvx`, which will automatically handle dependencies:

```json
{
  "mcpServers": {
    "chess": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/cjy8516/chess-mcp.git",
        "chess"
      ]
    }
  }
}
```

#### Using Local Installation

If you have cloned the repository locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/cjy8516/chess-mcp.git
   cd chess-mcp
   ```

2. Add to your config:
   ```json
   {
     "mcpServers": {
       "chess": {
         "command": "uv",
         "args": [
           "--directory",
           "/absolute/path/to/chess-mcp",
           "run",
           "chess"
         ]
       }
     }
   }
   ```

## Available Tools

- `get_chess_player_profile`: Fetches the profile of a chess player by their username.
- `get_chess_player_stats`: Fetches the statistics of a chess player by their username.
