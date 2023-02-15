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