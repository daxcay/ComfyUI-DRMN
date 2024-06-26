# By Daxton Caylor
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to
# deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""
@author: Daxton Caylor
@title: ComfyUI-DataSet
@nickname: ComfyUI-DataSet
@description: Data Research, Preparation And Manipulators Nodes for Model Trainers, Artists, Designers and Animators.
"""

from .classes.DATASET_TXTFileSaver import N_CLASS_MAPPINGS as TXTFileSaverMappings, N_DISPLAY_NAME_MAPPINGS as TXTFileSaverNameMappings
from .classes.DATASET_TXTFileLoader import N_CLASS_MAPPINGS as TXTFileLoaderMappings, N_DISPLAY_NAME_MAPPINGS as TXTFileLoaderNameMappings
from .classes.DATASET_TagManipulatorByImageNames import N_CLASS_MAPPINGS as TagManipulatorByImageNamesMappings, N_DISPLAY_NAME_MAPPINGS as TagManipulatorByImageNamesNameMappings
from .classes.DATASET_CaptionVisualizer import N_CLASS_MAPPINGS as CaptionVisualizerMappings, N_DISPLAY_NAME_MAPPINGS as CaptionVisualizerNameMappings
from .classes.DATASET_SearchAndReplace import N_CLASS_MAPPINGS as SearchAndReplaceMappings, N_DISPLAY_NAME_MAPPINGS as SearchAndReplaceNameMappings
from .classes.DATASET_xCopy import N_CLASS_MAPPINGS as xCopyMappings, N_DISPLAY_NAME_MAPPINGS as xCopyNameMappings
from .classes.DATASET_OpenAIChat import N_CLASS_MAPPINGS as OpenAIChatMappings, N_DISPLAY_NAME_MAPPINGS as OpenAIChatNameMappings
from .classes.DATASET_OpenAIChatImage import N_CLASS_MAPPINGS as OpenAIChatImageMappings,  N_DISPLAY_NAME_MAPPINGS as OpenAIChatImageNameMappings
from .classes.DATASET_LoadImage import N_CLASS_MAPPINGS as LoadImageMappings,  N_DISPLAY_NAME_MAPPINGS as LoadImageNameMappings
from .classes.DATASET_SaveImage import N_CLASS_MAPPINGS as SaveImageMappings,  N_DISPLAY_NAME_MAPPINGS as SaveImageNameMappings
from .classes.DATASET_TXTFileSaverBatch import N_CLASS_MAPPINGS as TXTFileSaverBatchMappings, N_DISPLAY_NAME_MAPPINGS as TXTFileSaverBatchNameMappings
from .classes.DATASET_OpenAIChatImageBatch import N_CLASS_MAPPINGS as OpenAIChatImageBatchMappings,  N_DISPLAY_NAME_MAPPINGS as OpenAIChatImageBatchNameMappings

NODE_CLASS_MAPPINGS = {}
NODE_CLASS_MAPPINGS.update(TXTFileSaverMappings)
NODE_CLASS_MAPPINGS.update(TXTFileLoaderMappings)
NODE_CLASS_MAPPINGS.update(TagManipulatorByImageNamesMappings)
NODE_CLASS_MAPPINGS.update(CaptionVisualizerMappings)
NODE_CLASS_MAPPINGS.update(SearchAndReplaceMappings)
NODE_CLASS_MAPPINGS.update(xCopyMappings)
NODE_CLASS_MAPPINGS.update(OpenAIChatMappings)
NODE_CLASS_MAPPINGS.update(OpenAIChatImageMappings)
NODE_CLASS_MAPPINGS.update(LoadImageMappings)
NODE_CLASS_MAPPINGS.update(SaveImageMappings)
NODE_CLASS_MAPPINGS.update(TXTFileSaverBatchMappings)
NODE_CLASS_MAPPINGS.update(OpenAIChatImageBatchMappings)

NODE_DISPLAY_NAME_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS.update(TXTFileSaverNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(TXTFileLoaderNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(TagManipulatorByImageNamesNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(CaptionVisualizerNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(SearchAndReplaceNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(xCopyNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(OpenAIChatNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(OpenAIChatImageNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(LoadImageNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(SaveImageNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(TXTFileSaverNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(OpenAIChatImageBatchNameMappings)

WEB_DIRECTORY = "./web"