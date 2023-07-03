import os
from urllib import request
import sys
import argparse

# Sorts files by their name. Directories come first.
def sort_files(a, b):
    if a == b:
        return 0
    if a == None or b == None:
        return -1 if a == None else 1
    left, right = os.path.isdir(a), os.path.isdir(b)
    if left == right:
        return -1 if a < b else 1
    return -1 if left else 1


# Creates a line of text for a directory entry.
def directory_line(file_name, full_path, level):
    has_readme = os.path.isfile(os.path.join(full_path, 'README.md'))
    return ('\t' * level) + '- ' + (file_name if not has_readme else '[%s](%s)' % (file_name, request.pathname2url(full_path)))

# Creates a line of text for a file entry.
def file_line(file_name, full_path, level):
    file_root = os.path.splitext(file_name)[0]
    return ('\t' * level) + '- [%s](%s)' % (file_root, request.pathname2url(file_name))

# Walks a given directory to create a TOC out of it.
def walk_directory(path = '.', exclude = ['.git', '.idea'], level = 0):
    # Dir list
    dirlist = sorted([x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))])
    # File list
    filelist = sorted([x for x in os.listdir(path) if not os.path.isdir(os.path.join(path, x))])

    result=[]
    # Make sure directories are listed before files (personal Preference)
    for file_name in dirlist + filelist:
        full_path = os.path.join(path, file_name)
        # Skip the file if its in the exclude list.
        if file_name in exclude: continue
        if os.path.isdir(full_path):
            result.append(directory_line(file_name, full_path, level))
            result.extend(walk_directory(full_path, exclude, level + 1))
        elif (file_name != 'README.md' and file_name.endswith('.md')) or file_name.endswith('.pdf'):
            #print(file_name)
            result.append(file_line(file_name, full_path, level))
    return result

def replace_toc(file_path, toc, toc_start, toc_end):
    toc_file = open(file_path, 'r').read()
    start, end =toc_file.find(toc_start), toc_file.find(toc_end)
    return (toc_file[:start + len(toc_start)]) + ("\n\n%s\n\n" % toc) + (toc_file[end:])



parser = argparse.ArgumentParser()
parser.add_argument("--readme", help="Searches and replaces the lines between toc-start and toc-end in the given file and prints the output. If not given, the script just prints the TOC generated.")
parser.add_argument("--target", help="Target folder to create TOC for.", default=".")
parser.add_argument("--exclude", help="List of folder and file names to exclude.", default=['.git', '.idea'], type=str, nargs='+')
parser.add_argument("--toc-start", help="Start of the TOC.", default="[//]: # (TOCSTART)")
parser.add_argument("--toc-end", help="End of the TOC.", default="[//]: # (TOCEND)")
args = parser.parse_args()

result = "\n".join(walk_directory(args.target, args.exclude))

if args.readme == None:
    sys.stdout.write(result)
else:
    sys.stdout.write(replace_toc(args.readme, result, args.toc_start, args.toc_end))
sys.stdout.flush()