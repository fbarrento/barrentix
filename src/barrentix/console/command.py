from argparse import ArgumentParser
from dataclasses import dataclass
from barrentix.contracts.console import AbstractCommand


@dataclass
class Command(AbstractCommand, ArgumentParser):
    parent: None | ArgumentParser = None
