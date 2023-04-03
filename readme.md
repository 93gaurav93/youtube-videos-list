# YouTube Channel Video Titles

A simple Python script to list down the titles of all videos from a given YouTube channel using the YouTube Data API v3.

## Prerequisites

- Python 3.6 or higher
- A Google Developer Console project with the YouTube Data API v3 enabled
- An API key for the YouTube Data API v3

## Dependencies

Install the required Python libraries using the following command:

```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/yourusername/youtube-channel-video-titles.git
cd youtube-channel-video-titles
```

2. Open the list_video_titles.py file and replace YOUR_API_KEY with your YouTube Data API v3 API key.

3. Replace the channel_id variable with the desired YouTube channel ID.

4. Run the script:

```bash
python list_video_titles.py
```

The script will output the titles of all videos from the specified YouTube channel.
