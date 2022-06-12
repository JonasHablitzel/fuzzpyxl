from openpyxl.cell.read_only import EmptyCell
from .base import BaseComparer, ReadOnlyCellTypes, SearchCellDefinition


class DataTypeCompare(BaseComparer):
    def __init__(self, weigth: int = 1):
        super().__init__(weigth=weigth)

    def _compare(
        self, cell: ReadOnlyCellTypes, search_cell: SearchCellDefinition
    ) -> int:
        if search_cell.re_pattern is None and isinstance(cell,EmptyCell):
            return 100
        elif search_cell.re_pattern is None:
            return 0
        
        return 100 if bool(search_cell.re_pattern.match(str(cell.value))) else 0