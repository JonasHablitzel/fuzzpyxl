from .base import BaseComparer, ReadOnlyCellTypes, SearchCellDefinition

class CelltypeCompare(BaseComparer):
    def __init__(self, weigth: int = 1):
        super().__init__(weigth=weigth)

    def _compare(
        self, cell: ReadOnlyCellTypes, search_cell: SearchCellDefinition
    ) -> int:        
        return 100 if isinstance(cell,search_cell.cell_type) else 0