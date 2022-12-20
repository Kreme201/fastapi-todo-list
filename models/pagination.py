from dataclasses import dataclass
from typing import List
from math import ceil


@dataclass
class Pagination:
    total: int = 0
    rpp: int = 0
    current: int = 1
    length: int = 5

    @property
    def pages(self) -> List[int]:
        # 가운데 표시 페이지 갯수 구하기
        calc_length: int = (
            (self.length - 1 if self.length % 2 == 0 else self.length)
            if self.length >= 5
            else 5
        ) - 2

        # 전체 페이지
        page: List[int] = [item for item in range(1, self.total_pages + 1)]

        # 전체 페이지 수가 표시할 페이지수보다 많을 경우
        if self.total_pages > calc_length + 2:
            separator: int = max(1, int((calc_length - 1) / 2))
            start: int = max(1, self.current - separator)
            end: int = min(self.total_pages, self.current + separator)

            # 전체 페이지 수가 계산된 페이지수보다 많을 경우
            if self.total_pages > calc_length:
                page = [item for item in page if start <= item <= end]

            while len(page) < calc_length:
                if max(page) == self.total_pages:
                    page.insert(0, min(page) - 1)
                else:
                    page.append(max(page) + 1)

            if min(page) == 1:
                page.append(max(page) + 1)
            elif min(page) == 2:
                page.insert(0, 1)
            elif max(page) == self.total_pages:
                page.insert(0, min(page) - 1)
            elif max(page) == self.total_pages - 1:
                page.append(self.total_pages)

        return page

    @property
    def has_pagination(self) -> bool:
        return self.total > 0 and len(self.pages) > 0

    @property
    def total_pages(self) -> int:
        return ceil(self.total / self.rpp)
