# RETTL UCI FIU

Automated robotics training in VR: Concept and Affect Detection.

![flow-chart](images/flow-chart.png)

## **Confidence Estimation**

### Requirements

Use `Dockerfile` to build an docker image and create a new container. 

```shell
docker build -t confidence .
docker run -itd -v "your_working_dir":/root/home --name confidence confidence:basic
```

Then start our new container. 

```shell
docker exec -it confidence /bin/zsh
```

See special requirements in each subfolder. 

### Tasks

- [x]  Create file name convention.
- [x]  Write python code to segment recordings in 5s clips.
- [x]  Use google speech-to-text to transcript 5s clips and store transcriptions
- [x]  Save the transcription for each 5 seconds clips, with the same naming conventions. 
- [x]  Extract and store acoustic features of clips (OpenSmile library), with the same naming conventions. 
- [ ]  Concatenate student id, clip id, acoustic features, transcription content to a csv file. 

### Naming Convention

First directory: studentId

Second directory: studentId-taskId

Third directory: studentId-taskId-clipId

For each clip: studentId-taskId-clipId

### Extract Features

Extract and store acoustic features: using compare emotion, EGEmaps configuration files.

Goal: find the features which are most correlated to the labeled confident extend. 
