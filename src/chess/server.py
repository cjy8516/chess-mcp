from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Chess.com")

from .chess_api import get_player_profile, get_player_stats

@mcp.tool()
def get_chess_player_profile(username: str):
    """Fetches the profile of a chess player by their username."""
    return get_player_profile(username)


@mcp.tool()
def get_chess_player_stats(username: str):
    """Fetches the statistics of a chess player by their username."""
    return get_player_stats(username)


def main():
      mcp.run()


if __name__ == "__main__":
     main()
  



