# Segment Audio File

## Requirements

First, set up a [python development environment](https://cloud.google.com/python/docs/setup) and activate it.

Install pydub library. 

```python
pip install pydub
```

If you are using Ubuntu OS, you can install ffmpeg by the following command. 

```
sudo apt install ffmpeg
```

If you want to install ffmpeg on other OS, check this [link](https://ffmpeg.org/download.html). 

## How to Use

Suppose you want to segment all audio files under `/root/home/example_folder`  : 

```
python segment.py /root/home/example_folder
```

Both absolute path and relative path would work. 
