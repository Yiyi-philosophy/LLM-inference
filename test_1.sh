#!/bin/bash
export CUDA_VISIBLE_DEVICES=1
set PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:32
# https://blog.csdn.net/MirageTanker/article/details/127998036#%E6%80%BB%E7%BB%93

# nvprof -o prof_1b3.nvvp 
# python3 ./benchmark/flexgen/bench_suite.py 1b3_test
# python3 ./benchmark/flexgen/bench_suite.py 1b3_test
# python3 ./benchmark/flexgen/bench_suite.py 6b7_1x1

# python -m flexgen.flex_opt --model facebook/opt-1.3b --gpu-batch-size 16 --percent 100 0 100 0 100 0 --cut-gen-len 8

### flex_opt, jk
python -m flexgen.flex_opt \
--model facebook/opt-1.3b --path _DUMMY_ --percent 100 0 100 0 100 0 --gpu-batch-size 4 --num-gpu-batches 4 --overlap True --compress-weight --compress-cache --prompt-len 512 --debug-mode fewer_batch

### flex_opt, kj
# # ipdb https://zhuanlan.zhihu.com/p/365255205
# python -m flexgen_kj.flex_opt_kj \
# --model facebook/opt-6.7b \
# --path _DUMMY_ \
# --percent 100 0 100 0 100 0 \
# --gpu-batch-size 4 \
# --num-gpu-batches 2 \
# --overlap True \
# --compress-weight \
# --compress-cache \
# --prompt-len 512