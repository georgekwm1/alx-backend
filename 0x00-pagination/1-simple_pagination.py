#!/usr/bin/env python3

"""Defines a class that paginates"""

import csv
import math
from typing import List


def index_range(page, page_size):
    """Return a tuple of size two containing the start and end index"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Gets page"""
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        if (page * page_size) <= len(self.dataset()):
            page_index_range = list(index_range(page, page_size))
            result = self.dataset()[page_index_range[0]:page_index_range[1]]
            return result
        else:
            return []
