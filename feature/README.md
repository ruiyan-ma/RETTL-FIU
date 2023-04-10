# Extract Acoustic Features

## Requirements

Check out [openSMILE documentation](https://audeering.github.io/opensmile/get-started.html#obtaining-and-installing-opensmile) and download [openSMILE](https://github.com/audeering/opensmile/releases) library for your OS. 

Note: for M1chip macbook, please exit docker container and download openSMILE macos version. Running openSMILE linux version in docker causes some issues and it's pretty slow. 

## How to Use

Suppose you want to extract features for all audio files under `input_folder`, using configuration file `example.conf`. 

```shell
python feature.py SMILExtract example.conf input_folder
```

Here both absolute path and relative path would work. 

By default the output file extension is `.csv`, you can specify it in command. 

Suppose you want use `.xls` as the output file extension: 

```shell
python feature.py SMILExtract example.conf input_folder .xls
```

## Resources

[Open Smile Documentation](https://audeering.github.io/opensmile/get-started.html#extracting-your-first-features)