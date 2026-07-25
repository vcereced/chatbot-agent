# chatbot-agent
sfsfsfsd

dependencias curl bash, makefile, docker, compose

[Microservicio Agent] ──(HTTP JSON)──> [tools-executor]
                                              │
                                              ├── 1. Router (/execute, /tools)
                                              ├── 2. ToolService (async, timeouts, try/except)
                                              ├── 3. ToolRegistry (Registro O(1) en RAM)
                                              └── 4. BaseTool -> [Echo, Calculator, DateTime...]