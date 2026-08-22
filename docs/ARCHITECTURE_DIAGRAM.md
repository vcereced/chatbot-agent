graph LR

  subgraph User
    U[Usuario Web]
  end

  subgraph NGINX["nginx (static + proxy)"]
    NG[Nginx Proxy / UI]
  end

  subgraph AGENT["agent (API + runtime)"]
    A_HTTP[HTTP API]
    A_WS[WebSocket Session]
    ChatSvc[ChatService]
    BaseClient["BaseClient.post - common HTTP client"]
  end

  subgraph LLM["llm (service)"]
    L_API[POST /generate]
    L_Service[LLMService]
    OllamaProv[OllamaProvider]
    OllamaHost["http://ollama:11434"]
  end

  subgraph MEMORY["memory (service)"]
    M_API[Memory API]
    M_Repo[Repositories]
  end

  subgraph TOOLS["tools-executor (service)"]
    T_API[POST /execute]
    ToolRegistry[ToolRegistry]
    ToolsImpl["Calculator / Date / DirTree"]
  end

  subgraph SHARED["shared (library)"]
    Shared["models / schemas / logging / utils"]
  end

  U -->|HTTP / Web UI| NG
  NG -->|proxy HTTP| A_HTTP
  NG -->|proxy WS| A_WS

  A_HTTP --> ChatSvc
  A_WS --> ChatSvc

  ChatSvc -->|POST /get_or_create| BaseClient
  BaseClient --> M_API

  ChatSvc -->|POST /generate| BaseClient
  BaseClient --> L_API

  ChatSvc -->|POST /execute| BaseClient
  BaseClient --> T_API

  L_API --> L_Service
  L_Service -->|provider call| OllamaProv
  OllamaProv --> OllamaHost
  L_Service -->|uses| Shared

  T_API --> ToolRegistry
  ToolRegistry -->|invokes| ToolsImpl

  M_API -->|uses| M_Repo

  ChatSvc --> Shared
  BaseClient --> Shared
  A_WS --> Shared

  classDef info fill:#f9f,stroke:#333,stroke-width:0.5
  class OllamaHost info