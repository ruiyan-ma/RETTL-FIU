from pydub import AudioSegment
import os
import sys
import math


class WavAudioSplitter():
    def __init__(self, file_path):
        """Create a wav audio splitter.

        Args:
            file_path (str): the path of your wav audio file.
        """
        # suppose file_path = /home/M1Lesson2.wav
        self.segment_folder = os.path.splitext(file_path)[0]
        # make segment folder /home/M1Lesson2
        os.makedirs(self.segment_folder)
        # file_name = M1Lesson2
        self.file_name = os.path.split(self.segment_folder)[1]
        self.audio = AudioSegment.from_wav(file_path)

    def get_length(self):
        """Return the duration of the audio file in seconds. """
        return self.audio.duration_seconds

    def split(self, folder, file_name, start, end):
        """Segment the audio file.

        Args:
            folder (str): which folder you want to store the segment file.
            file_name (str): what name you want to use for the segment file.
            start (int): start time of the segment file.
            end (int): end time of the second file.
        """
        t1 = start * 1000
        t2 = end * 1000
        split_audio = self.audio[t1:t2]
        split_audio.export(os.path.join(folder, file_name), format="wav")

    def multi_split(self, step, length):
        """Segment the audio file into multiple clips.

        Args:
            step (int): interval between two split point. 
            length (int): duration of each segment file.

        Overlap time = length - step
        """
        total_len = math.ceil(self.get_length())
        for start in range(0, total_len, step):
            index = start // step
            # clip_folder = /home/M1Lesson2/M1Lesson2-0
            clip_folder = os.path.join(
                self.segment_folder, self.file_name) + '-' + str(index)
            os.makedirs(clip_folder)
            # clip_file = M1Lesson2-0.wav
            clip_file = self.file_name + '-' + str(index) + '.wav'
            # split file and store clips
            self.split(clip_folder, clip_file, start, start + length)
            if start + step >= total_len:
                print('Segment {} successfully.'.format(
                    self.file_name + '.wav'))


if __name__ == "__main__":
    folder = sys.argv[1]
    for root, dirs, files in os.walk(folder):
        files = [file for file in files if file.endswith('.wav')]
        for file_name in files:
            file_path = os.path.join(root, file_name)
            s = WavAudioSplitter(file_path)
            s.multi_split(4, 5)  # Split to 5s clips, overlap 1 second
