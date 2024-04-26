# Twitter月度推文导出器

### [Switch to English Version](README(en).md)

## 项目描述
Twitter月度推文导出器是一个工具，用于从指定的Twitter账户获取推文，并根据用户选择的月份进行归档，每个月的推文将被保存到一个单独的XLSX文件中。用户可以通过一个简单的日历界面选择年月，方便地导出历史数据。

## 功能特性
- 输入Twitter用户名，获取该用户的推文。
- 提供日历界面供用户选择具体的年月。
- 按月份将推文保存到XLSX文件。
- 支持大量推文的高效导出。

## 功能描述
1. **用户输入界面**：
   - 简洁的界面供用户输入Twitter用户名。
   - 日历组件让用户可以选择特定的年份和月份。

2. **推文数据获取**：
   - 根据输入的用户名和选择的月份，通过Twitter API获取该时期的所有推文。
   - 实现推文的分页获取，确保完整收集整个月的数据。

3. **数据处理**：
   - 对收集到的推文按时间顺序进行排序。
   - 清洗数据，去除非关键信息，保留推文内容、发布时间及互动数据（点赞、转发）。

4. **文件保存**：
   - 将处理后的数据按月份保存至XLSX文件。
   - 文件命名格式为“用户名_年份_月份.xlsx”，方便管理和检索。

## 安装指南

### 环境要求
- Python 3.8+
- pip (Python包管理器)

### 安装步骤
1. 克隆仓库到本地
2. 安装依赖
   ```bash
   pip install -r requirements.txt
   ```

### 配置API密钥
要获取Twitter API密钥，你需要完成以下步骤： 
#### 访问Twitter开发者平台
打开[Twitter Developer Platform](https://developer.twitter.com/)并登录你的Twitter账户。 
#### 申请开发者访问权限
点击“Apply for access”并按照提示完成申请流程。
#### 创建一个项目和应用
完成开发者认证后，在开发者控制台中创建一个新项目。在项目中创建应用，并填写必要的详情，如应用名称、描述等。
#### 获取API密钥和令牌
创建应用后，你将获得API Key和API Secret Key。
进一步在应用设置中生成Access Token和Access Token Secret。
#### 注意
这需要升级你的应用访问权限，需要购买基本版API_v2，每个月100美元（免费版只能代表用户发帖）。
### 密钥文件设置
你需要在项目根目录下自行创建一个config.py文件来存储你的Twitter API密钥和令牌。请按照下面的格式创建该文件：

```python
# 这里需要填写你的Twitter API密钥
CONSUMER_KEY = 'your_consumer_key'
CONSUMER_SECRET = 'your_consumer_secret'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'
```
### 注意
- 请不要将你的API密钥和令牌直接存放在代码中或上传到任何公共仓库。
- 考虑使用环境变量或其他方法保护这些敏感信息。

## 使用方法
1. 运行程序
   ```bash
   python app.py
   ```
2. 按照提示输入Twitter用户名。
3. 使用日历控件选择年月。
4. 导出的XLSX文件将在 `data/` 目录下。

## 技术架构
- **Python**: 主要编程语言。
- **Tweepy**: 用于访问Twitter API。
- **Pandas**: 用于数据处理和XLSX文件生成。
- **Tkinter**: 提供图形用户界面(GUI)用于日历选择。

## 项目结构
```
twitter-monthly-post-tracker/
│
├── app.py                # 主程序文件，包含GUI逻辑
├── config.py             # 存放Twitter API密钥的配置文件
├── requirements.txt      # 项目依赖文件
├── twitter/              # Twitter数据处理模块
│   ├── __init__.py       # 模块初始化文件，可以为空
│   └── api.py            # 负责Twitter API调用的文件
├── storage/              # 数据存储模块
│   ├── __init__.py       # 模块初始化文件，可以为空
│   └── excel.py          # 负责数据保存到Excel的文件
└── data/                 # 存放生成的Excel文件的目录
```

## 贡献指南
如果你想对项目做出贡献，可以通过GitHub的Pull Request或Issue进行。

## 许可证
本项目采用MIT许可证，详细信息请查阅LICENSE文件。

## 联系方式
- GitHub: [Snake-Konginchrist](https://github.com/Snake-Konginchrist)
- Email: 592413692@qq.com