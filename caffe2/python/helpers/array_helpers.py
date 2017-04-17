## @package arra_helpers
# Module caffe2.python.helpers.array_helpers
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


def Concat(model, blobs_in, blob_out, order="NCHW", **kwargs):
    """Depth Concat."""
    return model.net.Concat(
        blobs_in,
        [blob_out, "_" + blob_out + "_concat_dims"],
        order=order,
        **kwargs
    )[0]


def DepthConcat(model, blobs_in, blob_out, **kwargs):
    """The old depth concat function - we should move to use concat."""
    print("DepthConcat is deprecated. use Concat instead.")
    return Concat(blobs_in, blob_out, **kwargs)
