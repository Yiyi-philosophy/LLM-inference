#!/bin/bash
#conda activate flexgen
export CUDA_VISIBLE_DEVICES=1
#export CUDA_VISIBLE_DEVICES=0
# set PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:32
# python flexgen/flex_opt.py --model facebook/opt-1.3b --gpu-batch-size 8 --percent 100 0 100 0 100 0 --cut-gen-len 8 --num-gpu-batches 32 --search-order diagonal

# python flexgen/flex_opt.py --model facebook/opt-1.3b --gpu-batch-size 8 --percent 100 0 100 0 100 0 --cut-gen-len 8 --num-gpu-batches 8 --search-order zigzag

# prompt long

# origin
# prompt_len_list=(128 256 512 1024)
# num_gpu_batches_list=(4 8 16 32)
# for num_gpu_batches in "${num_gpu_batches_list[@]}"; do
#     for prompt_len in "${prompt_len_list[@]}"; do
#         python flexgen/flex_opt.py \
#             --model facebook/opt-1.3b \
#             --prompt-len $prompt_len\
#             --gpu-batch-size 8 \
#             --percent 100 0 100 0 100 0 \
#             --cut-gen-len 8 \
#             --num-gpu-batches $num_gpu_batches \
#             --search-order zigzag 
#     done
# done

# diagnal

prompt_len_list=(128 256 512 1024)
num_gpu_batches_list=(4 8 16 32)
for num_gpu_batches in "${num_gpu_batches_list[@]}"; do
    for prompt_len in "${prompt_len_list[@]}"; do
        python flexgen/flex_opt.py \
            --model facebook/opt-1.3b \
            --prompt-len $prompt_len\
            --gpu-batch-size 8 \
            --percent 100 0 100 0 100 0 \
            --cut-gen-len 8 \
            --num-gpu-batches $num_gpu_batches \
            --search-order diagonal 
    done
done
