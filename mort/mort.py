"""Main file of this package"""
import argparse
import sys
import tempfile
import os
import shlex
from contextlib import contextmanager

from mand.mand import replace_sys_args
import mand


def _get_parser():
    parser = argparse.ArgumentParser()
    #parser.add_argument('--debugger',
    #                    help='Debug module to invoke. Default: %(default)s', default="pdb")
    parser.add_argument(metavar='file', help='File or module to invoke', dest='file_path')
    parser.add_argument('args',
                        help='Passthrough these arguments to given module / script',
                        nargs="*",
                        default=None)
    return parser


def main(argv=None):
    """Cli entry point"""
    if argv is None:
        argv = sys.argv[1:]
    args = _get_parser().parse_args(argv)
    run(args.file_path, args.args)


def run(file_path_or_module, args=None):
    """API entry point

    args:
        """
    new_cli_args = [file_path_or_module]
    if args is not None:
        if isinstance(args, str):
            new_cli_args.extend(shlex.split(args))
        else:
            new_cli_args.extend(args)

    with readable_temporary_file(PAYLOAD) as payload_path:
        with replace_sys_args(new_cli_args):
            mand.mand([payload_path, file_path_or_module])


# Taken from https://stackoverflow.com/a/13174701/487464
PAYLOAD = """
import sys

def info(type, value, tb):
   if hasattr(sys, 'ps1') or not sys.stderr.isatty():
      # we are in interactive mode or we don't have a tty-like
      # device, so we call the default hook
      sys.__excepthook__(type, value, tb)
   else:
      import traceback, pdb
      # we are NOT in interactive mode, print the exception...
      traceback.print_exception(type, value, tb)
      print()
      # ...then start the debugger in post-mortem mode.
      pdb.post_mortem(tb)

sys.excepthook = info
"""


@contextmanager
def readable_temporary_file(txt):
    """Create readable temporary file from given txt

    yields:
        path to readable temporary file

    Removes temporary file after context manager
    exits
    """
    with tempfile.NamedTemporaryFile('w', delete=False) as named_file:
        named_file.write(txt)
    try:
        yield named_file.name
    finally:
        os.remove(named_file.name)
