
## Result on A6000 45G

### Flexgen

#### origin

--num-gpu-batches 4
peak gpu mem: 6.278 GB  projected: True
prefill latency: 0.632 s        prefill throughput: 25923.996 token/s
decode latency: 2.017 s decode throughput: 491.710 token/s
total latency: 2.649 s  total throughput: 386.495 token/s

--num-gpu-batches 8
peak gpu mem: 9.522 GB  projected: True
prefill latency: 1.275 s        prefill throughput: 25697.433 token/s
decode latency: 3.953 s decode throughput: 501.855 token/s
total latency: 5.228 s  total throughput: 391.701 token/s


--num-gpu-batches 16
peak gpu mem: 16.011 GB projected: True
prefill latency: 2.562 s        prefill throughput: 25578.576 token/s
decode latency: 7.872 s decode throughput: 504.052 token/s
total latency: 10.434 s total throughput: 392.550 token/s

--num-gpu-batches 32
peak gpu mem: 28.987 GB projected: True
prefill latency: 5.140 s        prefill throughput: 25500.405 token/s
decode latency: 16.068 s        decode throughput: 493.898 token/s
total latency: 21.208 s total throughput: 386.268 token/s

#### diagnal

--num-gpu-batches 4
model size: 2.443 GB    cache size: 3.188 GB    hidden size (p): 0.066 GB
peak gpu mem: 6.086 GB  projected: True
prefill latency: 0.319 s        prefill throughput: 51432.869 token/s
decode latency: 1.748 s decode throughput: 567.437 token/s
total latency: 2.067 s  total throughput: 495.461 token/s

--num-gpu-batches 8
model size: 2.443 GB    cache size: 6.375 GB    hidden size (p): 0.133 GB
peak gpu mem: 9.172 GB  projected: True
prefill latency: 0.958 s        prefill throughput: 34214.002 token/s
decode latency: 2.670 s decode throughput: 743.176 token/s
total latency: 3.627 s  total throughput: 564.598 token/s

--num-gpu-batches 16
model size: 2.443 GB    cache size: 12.750 GB   hidden size (p): 0.266 GB
peak gpu mem: 15.335 GB projected: True
prefill latency: 2.248 s        prefill throughput: 29155.880 token/s
decode latency: 4.581 s decode throughput: 866.126 token/s
total latency: 6.829 s  total throughput: 599.786 token/s


--num-gpu-batches 32
model size: 2.443 GB    cache size: 25.500 GB   hidden size (p): 0.531 GB
peak gpu mem: 27.749 GB projected: True
prefill latency: 4.842 s        prefill throughput: 27071.220 token/s
decode latency: 8.301 s decode throughput: 955.973 token/s
total latency: 13.143 s total throughput: 623.286 token/s





