#!/bin/bash
#conda activate flexgen
export CUDA_VISIBLE_DEVICES=1
set PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:32
### flex_opt, jk
python -m ipdb flexgen/flex_opt.py --model facebook/opt-1.3b --path _DUMMY_ --percent 100 0 100 0 100 0 --gpu-batch-size 4 --num-gpu-batches 4 --overlap True --compress-weight --compress-cache --prompt-len 512