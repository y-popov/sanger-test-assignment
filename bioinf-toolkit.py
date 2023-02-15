import argparse
from src.fastq import Fastq


def main():
    parser = argparse.ArgumentParser(description='Sanger Bioinformatics Toolkit')
    parser.add_argument('-f', '--fastq', help='path to fastq file', required=True, type=str)
    parser.add_argument('--seq_count', help='prints the sequence count', action='store_true')
    args = parser.parse_args()

    fastq = Fastq(path=args.fastq)

    if args.seq_count:
        n = fastq.count_seqs()
        print(n)


if __name__ == '__main__':
    main()
