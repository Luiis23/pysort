#~ IMPORTS ~#
import argparse
from sorter import Sorter

#~ GLOBALS ~#

#~ ARGPARSING ~#
def argp():
    parser = argparse.ArgumentParser(description="Sort files in subfolders")

    parser.add_argument("path", type=str, help="Path of the folder that will be sorted") 

    return parser.parse_args()

#~ MAIN PROGRAM ~#
def main():
    args = argp()
    s = Sorter(args.path)

    s.sortfiles()
if __name__ == "__main__":
    main()

    
#       BY GEGAKE AND LUIIS
#  https://github.com/Luiis23/pysort     
