deepspeed --num_nodes 2 --num_gpus 1 --master_port 7778 --hostfile hostfile \
    hf_opt.py --model facebook/opt-6.7b --batch-size 16 --cut-gen-len 5 --dummy
