from mcp.server.fastmcp import FastMCP
from wxauto import WeChat

mcp = FastMCP("wxauto_mcp")
wx = WeChat()


@mcp.tool(name="send_message", description="send message to someone")
def send_message(msg: str, to: str, at: str | list[str] = None):
    wx.SendMsg(msg, to, at)

@mcp.tool(name="get_all_messages", description="get all messages from someone or group")
def get_all_messages(who: str, load_more: bool = False):
    wx.ChatWith(who)
    if load_more:
        wx.LoadMoreMessage()
    msgs = wx.GetAllMessage()
    if msgs:
        return [{'sender': msg.sender, 'content': msg.content} for msg in msgs if msg.type == 'friend']
    return []

if __name__ == "__main__":
    mcp.run()




