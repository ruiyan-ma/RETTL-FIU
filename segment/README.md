# Segment Audio File

## Requirements

We need to install [pydub](https://pypi.org/project/pydub/) and [ffmpeg](https://ffmpeg.org/download.html) for the segment code. 

If you are using our docker container, you don't need to do anything. 

## How to Use

Suppose you want to segment all audio files under `/root/home/example_folder`  : 

```shell
python3 segment.py /root/home/example_folder
```

Both absolute path and relative path would work. 
