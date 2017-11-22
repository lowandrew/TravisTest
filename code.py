from Bio import SeqIO
import shutil


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def dependency_check(program):
    if shutil.which(program) is not None:
        return True
    else:
        return False
