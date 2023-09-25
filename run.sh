#!/bin/bash
#conda activate flexgen
export CUDA_VISIBLE_DEVICES=0
#export CUDA_VISIBLE_DEVICES=0
<<<<<<< HEAD
set PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:32
python -m ipdb flexgen/flex_opt.py --model facebook/opt-1.3b --gpu-batch-size 8 --percent 100 0 100 0 100 0 --cut-gen-len 8 --num-gpu-batches 12
=======
# set PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:32

python -m ipdb flexgen/flex_opt.py --model facebook/opt-1.3b --gpu-batch-size 8 --percent 100 0 100 0 100 0 --cut-gen-len 8 --num-gpu-batches 8
python -m ipdb flexgen/flex_opt.py --model facebook/opt-1.3b --gpu-batch-size 8 --percent 100 0 100 0 100 0 --cut-gen-len 8 --num-gpu-batches 8
>>>>>>> d285ed25da8cc881b9555f6248f1c076c24ec4b8
