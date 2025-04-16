# wxauto-mcp

一个基于微信自动化的MCP服务器，用于与微信客户端交互。
该服务器利用[wxauto库实](https://github.com/cluic/wxauto.git)现微信消息的发送和接收功能，使大语言模型能够通过wxauto与微信进行交互。


## 功能特点

### 工具

该服务器提供以下工具：

- **send_message**: 向指定联系人或群组发送消息
  - 参数:
    - `msg`: 要发送的消息内容 (必填)
    - `to`: 接收消息的联系人或群组名称 (必填)
    - `at`: 在群消息中@的人 (可选)
  - 返回值: 无

- **get_all_messages**: 获取与指定联系人或群组的聊天记录
  - 参数:
    - `who`: 联系人或群组名称 (必填)
    - `load_more`: 是否加载更多历史消息 (可选，默认为False)
  - 返回值: 消息列表，仅包含类型为'friend'的消息，每条消息包含发送者和内容信息

## 使用方法

### 安装uv

参考[uv官方安装文档](https://docs.astral.sh/uv/getting-started/installation/)

### 配置wxauto-mcp

```bash
git clone https://github.com/barantt/wxauto-mcp.git
cd wxauto-mcp
uv sync
```

### Claude Desktop 配置

要在Claude Desktop中使用，请添加服务器配置：

在MacOS上：`~/Library/Application\ Support/Claude/claude_desktop_config.json`  
在Windows上：`%APPDATA%/Claude/claude_desktop_config.json`


```json
"mcpServers": {
  "wxauto-mcp": {
    "command": "uv",
    "args": [
      "--directory",
      "path\\to\\wxauto-mcp",
      "run",
      "wxauto_mcp.py"
    ]
  }
}
```


### Cursor配置
在Cursor中使用，请在Cursor的MCP配置文件中添加以下内容：

在Windows上：`%USERPROFILE%\.cursor\mcp.json`  

在MacOS上：`~/.cursor/mcp.json`

```json
"mcpServers": {
  "wxauto-mcp": {
    "command": "uv",
    "args": [
      "--directory",
      "path\\to\\wxauto-mcp",
      "run",
      "wxauto_mcp.py"
    ]
  }
}
```

