from pydub import AudioSegment
import os
import sys
import math


class WavAudioSplitter():
    def __init__(self, filepath):
        """Create a wav audio splitter.

        Args:
            filepath (str): the path of your wav audio file.
        """
        self.folder, self.filename = os.path.split(filepath)
        self.filename, self.extention = os.path.splitext(self.filename)
        self.audio = AudioSegment.from_wav(filepath)

    def get_length(self):
        """Return the duration of the audio file in seconds. """
        return self.audio.duration_seconds

    def split(self, folder, filename, start, end):
        """Split the audio file and get a segment.

        Args:
            folder (str): which folder you want to store the segment file.
            filename (str): what name you want to give to the segment file.
            start (int): start time of the segment file.
            end (int): end time of the second file.
        """
        t1 = start * 1000
        t2 = end * 1000
        split_audio = self.audio[t1:t2]
        split_audio.export(os.path.join(folder, filename), format="wav")

    def multi_split(self, folder, step, length):
        """Split the audio file for multiple times.

        Args:
            folder (str): which folder you want to store the segment file.
            step (int): interval between two split point. 
            length (int): duration of each segment file.

        Overlap time = length - step
        """
        total_len = math.ceil(self.get_length())
        for start in range(0, total_len, step):
            index = start // step
            filename = self.filename + '_' + str(index) + self.extention
            self.split(folder, filename, start, start + length)
            if start + step >= total_len:
                print('Split successful')


if __name__ == "__main__":
    filepath = sys.argv[1]
    target_folder = sys.argv[2]
    # if target folder doesn't exist, make directory.
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    s = WavAudioSplitter(filepath)
    # Split to 5s clips, overlap 1 second
    s.multi_split(target_folder, 4, 5)
