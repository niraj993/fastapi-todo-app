from abc import ABC, abstractmethod
from typing import Any, Optional, Tuple


class DatabaseConnector(ABC):

    @abstractmethod
    def connect(self) -> Any:
        """
        Must return a DB connection object
        """
        pass

    def execute(
        self,
        query: str,
        params: Tuple = (),
        fetchone: bool = False,
        fetchall: bool = False,
        commit: bool = False
    ) -> Optional[Any]:
        """
        Universal DB executor (DRY)
        """
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)

            if commit:
                conn.commit()

            if fetchone:
                return cursor.fetchone()

            if fetchall:
                return cursor.fetchall()

            return cursor
