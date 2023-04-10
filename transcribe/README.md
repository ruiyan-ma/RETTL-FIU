# Transcript Audio Records

## Requirements

First, we need the [google-cloud-speech](https://cloud.google.com/speech-to-text/docs/speech-to-text-client-libraries?hl=zh-cn) library. It's already installed in our docker container. 


```shell
pip install --upgrade google-cloud-speech
```

Then, [set up speech-to-text and create a JSON key](https://cloud.google.com/speech-to-text/docs/before-you-begin) and set your authentication environment variable. 

```shell
# replace KEY_PATH with the path of the JSON key. 
export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"
```

If you want the variable to apply to future shell sessions, set the variable in your shell startup file, for example in the `~/.bashrc` or `~/.profile` file. 

## How to Use

Suppose you want to transcribe all audio record files under `/root/home/example_folder` : 

```shell
python3 transcribe.py /root/home/example_folder
```

Both absolute path and relative path would work. 

## Resources

[Speech-to-Text Client Libraries Introduction](https://cloud.google.com/speech-to-text/docs/transcribe-client-libraries#client-libraries-usage-python)

[How to create and use Speech-to-Text credential](https://cloud.google.com/speech-to-text/docs/speech-to-text-client-libraries)

[Transcribe short audio files](https://cloud.google.com/speech-to-text/docs/sync-recognize)

[Python speech to text with Google Cloud Speech example](https://www.youtube.com/watch?v=DtlJH6MgBso&ab_channel=ParwizForogh)
