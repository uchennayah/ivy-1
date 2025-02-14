import jax.numpy as jnp

from ivy.functional.backends.jax import JaxArray
from typing import Optional, Union

def argmax(
    x:JaxArray, 
    axis:Optional[int]=None, 
    out: Optional[JaxArray] = None, 
    keepdims:bool= False
) -> JaxArray: 
    return jnp.argmax(x,axis=axis,out=out,keepdims=keepdims)

def argmin(x : JaxArray,
    axis: Optional[int] = None,
    out: Optional[JaxArray] = None,
    keepdims: bool = False
    ) -> JaxArray:

    ret = jnp.argmin(x,axis=axis,out=out,keepdims=keepdims)
    return (ret)

where = lambda condition, x1, x2: jnp.where(condition, x1, x2)