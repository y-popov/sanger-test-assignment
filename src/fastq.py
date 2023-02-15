import os.path


class Fastq:
    def __init__(self, path: str):
        self.path = path
        self.validate_path()

    def validate_path(self) -> None:
        """ checks that input path follows fastq extension """
        if not os.path.exists(self.path):
            raise FileNotFoundError(self.path)

        if not self.path.endswith(('.fastq', 'fq')):
            print(f'{self.path} does not seem to be a fastq file. Please check the path')

    def count_seqs(self) -> int:
        """ counts number of sequences in file """
        lines = 0
        with open(self.path) as f:
            for line in f:
                lines += 1

        seqs = lines / 4
        if seqs.is_integer():
            seqs = int(seqs)
        else:
            raise ValueError('Number of lines is not multiple by 4')

        return seqs

    def count_bps(self) -> int:
        """ counts number of nucleotides in file """
        line_number = 0
        count = 0

        with open(self.path) as f:
            for line in f:
                line_number += 1
                if line_number % 2 == 0 and line_number % 4 != 0:
                    count += len(line.rstrip())

        return count
