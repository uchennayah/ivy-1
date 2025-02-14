import numpy as np

from typing import Union, Optional

def argmax(
    x:np.ndarray,
    axis: Optional[int] = None,
    out: Optional[int] = None,
    keepdims: bool = False,
) -> np.ndarray:
    ret = np.argmax(x,axis=axis,keepdims=keepdims)
    return ret


def argmin(x: np.ndarray,
           axis: Optional[int] = None,
           out: Optional[np.ndarray] = None,
           keepdims: bool = False
           ) -> np.ndarray:
    ret = np.argmin(x, axis=axis, out=out, keepdims=keepdims)
    return ret


where = lambda condition, x1, x2: np.where(condition, x1, x2)
