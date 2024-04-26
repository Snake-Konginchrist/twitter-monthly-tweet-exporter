# Twitter Monthly Tweet Exporter

### [切换为简体中文版本](README.md)

## Project Description
The Twitter Monthly Tweet Exporter is a tool designed to fetch tweets from a specified Twitter account and archive them according to the month selected by the user. Each month's tweets are saved into a separate XLSX file. Users can easily export historical data using a simple calendar interface to select the desired month and year.

## Features
- Input a Twitter username to fetch tweets.
- Provides a calendar interface for users to select the specific year and month.
- Saves tweets monthly into XLSX files.
- Supports efficient exporting of a large number of tweets.

## Functional Description
1. **User Input Interface**:
   - A simple interface allows users to enter a Twitter username.
   - A calendar component enables users to select a specific year and month.

2. **Tweet Data Fetching**:
   - Retrieves all tweets from the specified user and selected month via the Twitter API.
   - Implements pagination in data fetching to ensure complete collection of tweets for the entire month.

3. **Data Processing**:
   - Sorts the collected tweets in chronological order.
   - Cleanses data, removing non-essential information, and retains key details such as tweet content, posting time, and interaction data (likes, retweets).

4. **File Saving**:
   - Processed data are saved into XLSX files sorted by month.
   - Files are named in the format “username_year_month.xlsx” for easy management and retrieval.

## Installation Guide

### System Requirements
- Python 3.8+
- pip (Python package manager)

### Installation Steps
1. Clone the repository locally
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

### Configuring API Keys
To obtain Twitter API keys, you need to complete the following steps:
#### Visit the Twitter Developer Platform
Open the [Twitter Developer Platform](https://developer.twitter.com/) and log in with your Twitter account.
#### Apply for Developer Access
Click “Apply for access” and follow the prompts to complete the application process.
#### Create a Project and Application
After obtaining developer accreditation, create a new project in the developer console. Create an application within the project and fill in necessary details such as the app name and description.
#### Obtain API Keys and Tokens
After creating the application, you will receive the API Key and API Secret Key.
Further generate the Access Token and Access Token Secret in the app settings.
#### Note
This requires upgrading your application's access rights, needing a purchase of the basic version of API_v2 at $100 per month (the free version only allows posting on behalf of users).

### Key File Configuration
You need to manually create a `config.py` file in the project root directory to store your Twitter API keys and tokens. Please create the file in the following format:

```python
# Fill in your Twitter API keys here
CONSUMER_KEY = 'your_consumer_key'
CONSUMER_SECRET = 'your_consumer_secret'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'
```
### Note
- Do not store your API keys and tokens directly in the code or upload them to any public repository.
- Consider using environment variables or other methods to protect this sensitive information.

## How to Use
1. Run the program
   ```bash
   python app.py
   ```
2. Follow the prompts to enter a Twitter username.
3. Use the calendar control to select the year and month.
4. The exported XLSX file will be located in the `data/` directory.

## Technical Architecture
- **Python**: Primary programming language.
- **Tweepy**: Used for accessing the Twitter API.
- **Pandas**: Used for data processing and generating XLSX files.
- **Tkinter**: Provides a graphical user interface (GUI) for calendar selection.

## Project Structure
```
twitter-monthly-post-tracker/
│
├── app.py                # Main program file containing GUI logic
├── config.py             # Configuration file storing Twitter API keys
├── requirements.txt      # File listing project dependencies
├── twitter/              # Module for handling Twitter data
│   ├── __init__.py       # Module initialization file, can be empty
│   └── api.py            # Responsible for Twitter API calls
├── storage/              # Module for data storage
│   ├── __init__.py       # Module initialization file, can be empty
│   └── excel.py          # Responsible for saving data to Excel files
└── data/                 # Directory where Excel files are stored
```

## Contribution Guide
If you would like to contribute to the project, you can do so via GitHub's Pull Request or Issue.

## License
This project is licensed under the MIT License. For more details, please refer to the LICENSE

 file.

## Contact Information
- GitHub: [Snake-Konginchrist](https://github.com/Snake-Konginchrist)
- Email: 592413692@qq.com

This translation of the README file provides a comprehensive overview of the project in English, suitable for an international audience.