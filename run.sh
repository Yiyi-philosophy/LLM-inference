#!/bin/bash
#conda activate flexgen
export CUDA_VISIBLE_DEVICES=1
#export CUDA_VISIBLE_DEVICES=0
# set PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:32
python flexgen/flex_opt.py --model facebook/opt-1.3b --gpu-batch-size 8 --percent 100 0 100 0 100 0 --cut-gen-len 8 --num-gpu-batches 32 --search-order diagonal

# python flexgen/flex_opt.py --model facebook/opt-1.3b --gpu-batch-size 8 --percent 100 0 100 0 100 0 --cut-gen-len 8 --num-gpu-batches 8 --search-order zigzag

