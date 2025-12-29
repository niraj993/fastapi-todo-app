
from typing import List, Dict, Union
from sqlite3 import Row

def rows_to_dicts(rows: Union[List[Row], Row, None]) -> Union[List[Dict], Dict, None]:
    """
    Convert sqlite3.Row or list of Rows to dict or list of dicts.
    """
    if rows is None:
        return None
    if isinstance(rows, list):
        return [dict(row) for row in rows]
    return dict(rows)
