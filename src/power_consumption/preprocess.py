import pandas as pd
import yaml
from sklearn.base import BaseEstimator, TransformerMixin

from power_consumption.utils import get_config

__all__ = [
    "ColSelector",
    "ColRenamer",
]

CONFIG = get_config()


class ColSelector(BaseEstimator, TransformerMixin):
    """This estimator selects columns specified in config.yaml
    from the raw dataframe.
    """

    def __init__(self, cols=CONFIG["cols"]["take"]):
        self.cols = cols

    def fit(self, X: pd.DataFrame, y=None):
        return self

    def transform(self, X):
        # validation
        assert set(self.cols) == set(CONFIG["cols"]["take"]), "unknown columns!"
        return X[self.cols]


class ColRenamer(BaseEstimator, TransformerMixin):
    """This estimator renames selected columns as specified in config.yaml."""

    def __init__(self, cols_rename_dict=CONFIG["cols"]["rename"]):
        self.cols_rename_dict = cols_rename_dict

    def fit(self, X: pd.DataFrame, y=None):
        return self

    def transform(self, X):
        # validation
        assert set(self.cols_rename_dict.keys()) == set(
            CONFIG["cols"]["take"]
        ), "unknown columns!"
        return X.rename(columns=self.cols_rename_dict)
