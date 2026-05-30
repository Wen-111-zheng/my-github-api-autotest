# GitHub API 自动化测试框架

> 基于 Python + Pytest + Requests 的接口自动化测试项目，以 GitHub Public API 为被测对象

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Pytest](https://img.shields.io/badge/Pytest-9.0-green)
![Requests](https://img.shields.io/badge/Requests-2.31-orange)

## 项目结构

```
my-api-test/
├── conftest.py          # 全局 fixture（Session 管理、响应时间断言）
├── pytest.ini           # 测试配置（路径、标记、输出格式）
├── requirements.txt     # 依赖清单
└── tests/
    └── test_user_api.py # 用户接口测试用例
```

## 运行方式

```bash
# 安装依赖
pip install -r requirements.txt

# 运行所有用例
pytest -v

# 只跑冒烟测试
pytest -m smoke
```

## 测试覆盖

| 接口 | 场景 | 状态 |
|------|------|------|
| GET /users/{username} | 正常用户返回 200 | ✅ |
| GET /users/{username} | 不存在用户返回 404 | 待补充 |
| GET /users/{username} | 响应时间 < 2s | ✅ |

## 设计要点

- `conftest.py` 使用 **session 级 fixture**，整个测试过程复用同一个 HTTP Session
- `pytest.ini` 配置 `@pytest.mark` 标记，支持分类执行（smoke / regression / boundary）
- 断言覆盖：状态码 + 响应时间 + 字段完整性

## 后续计划

- [ ] 补充参数化边界测试（空用户名、特殊字符等）
- [ ] 集成 Allure 生成 HTML 测试报告
- [ ] 接入 GitHub Actions 实现 CI 自动运行