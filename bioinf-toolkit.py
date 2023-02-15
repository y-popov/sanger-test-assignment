import argparse
from src.fastq import Fastq


def main():
    parser = argparse.ArgumentParser(description='Sanger Bioinformatics Toolkit')
    parser.add_argument('-f', '--fastq', help='path to fastq file', required=True)
    args = parser.parse_args()

    fastq = Fastq(path=args.fastq)


if __name__ == '__main__':
    main()
