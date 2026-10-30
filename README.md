# llm-usecase-generator

基于大模型API的智能需求分析与用例生成工具 (课程项目九)

## 🌟 核心功能
- [ ] 需求解析：输入用户故事，提取功能点。
- [ ] 结构化生成：基于Prompt模板，输出符合UML规范的JSON用例。
- [ ] 自动校验：Schema格式校验 + 业务逻辑一致性检查。
- [ ] 人机协同：Web端交互，支持用例修改与重试反馈。
- [ ] 效率评估：对比纯手工与AI辅助的编写效率。

## 🛠️ 技术栈
- 后端/核心逻辑：Python, FastAPI
- 大模型API：OpenAI/通义千问/文心一言 (待定)
- 数据结构校验：Pydantic
- 前端：Vue

## 📂 目录结构 (规划)
```text
├── data/           # 100个测试集样例 (BDD数据集等)
├── prompts/        # 提示词模板设计
├── src/            # 核心代码
│   ├── api.py      # 大模型调用封装
│   ├── validator.py# 校验器 (Pydantic + 业务规则)
│   └── main.py     # Web服务入口
└── README.md
