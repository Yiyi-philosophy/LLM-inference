
## Result on A6000 45G

## Flexgen
### Different Batches

| latency    | num batch | Origin  | diagonal |       |
|------------|-----------|---------|----------|-------|
|            | 4         | 2.649   | 2.067    |       |
|            | 8         | 5.228   | 3.627    |       |
|            | 16        | 10.434  | 6.829    |       |
|            | 32        | 21.208  | 13.143   |       |
|            |           |         |          |       |
| throughput |           | Origin  | diagonal | scale |
|            | 4         | 386.495 | 495.461  | 1.282 |
|            | 8         | 391.701 | 564.598  | 1.441 |
|            | 16        | 392.55  | 599.786  | 1.528 |
|            | 32        | 386.268 | 623.286  | 1.614 |
|            |           |         |          |       |
| peak mem   |           | Origin  | diagonal |       |
|            | 4         | 6.278   | 6.086    |       |
|            | 8         | 9.522   | 9.172    |       |
|            | 16        | 16.011  | 15.335   |       |
|            | 32        | 28.987  | 27.749   |       |

### Different Prompt length
| Num   batches | Prompt | Origin  | Origin     | Origin   | Diag    | Diag       | Diag     |
|---------------|--------|---------|------------|----------|---------|------------|----------|
|               |        | latency | throughput | peak mem | latency | throughput | peak mem |
| 4             | 128    | 2.158   | 474.599    | 3.699    | 1.246   | 822.02     | 3.525    |
| 4             | 256    | 2.32    | 441.424    | 4.555    | 1.515   | 675.8      | 4.378    |
| 4             | 512    | 2.626   | 389.879    | 6.278    | 2.069   | 494.897    | 6.086    |
| 4             | 1024   | 3.524   | 290.593    | 10.153   | 3.555   | 288.077    | 9.93     |
| 8             | 128    | 4.321   | 473.985    | 4.652    | 2.295   | 892.348    | 4.315    |
| 8             | 256    | 4.647   | 440.707    | 6.268    | 2.724   | 751.873    | 5.933    |
| 8             | 512    | 5.324   | 384.683    | 9.522    | 3.615   | 566.58     | 9.172    |
| 8             | 1024   | 7.092   | 288.789    | 16.46    | 6.025   | 339.892    | 16.078   |
| 16            | 128    | 8.692   | 471.235    | 6.559    | 4.585   | 893.311    | 5.884    |
| 16            | 256    | 9.39    | 436.231    | 9.694    | 5.386   | 760.542    | 9.034    |
| 16            | 512    | 10.633  | 385.228    | 16.011   | 6.881   | 595.28     | 15.335   |
| 16            | 1024   | 14.248  | 287.482    | 29.073   | 11.101  | 368.981    | 28.366   |
| 32            | 128    | 17.382  | 471.291    | 10.371   | 8.812   | 929.688    | 9.11     |
| 32            | 256    | 18.79   | 435.974    | 16.546   | 10.311  | 794.502    | 15.323   |
| 32            | 512    | 21.467  | 381.616    | 28.987   | 13.253  | 618.147    | 27.749   |
| 32            | 1024   | 0       | 0          | 0        | 0       | 0          | 0        |

#### Compare Scale

| Num batches | Prompt | throughput | peak mem  |
|-------------|--------|------------|-----------|
| 4           | 128    | 1.732      | 0.953     |
| 4           | 256    | 1.531      | 0.961     |
| 4           | 512    | 1.269      | 0.969     |
| 4           | 1024   | 0.991      | **0.978** |
| 8           | 128    | 1.883      | 0.928     |
| 8           | 256    | 1.706      | 0.947     |
| 8           | 512    | 1.473      | 0.963     |
| 8           | 1024   | 1.177      | 0.977     |
| 16          | 128    | 1.896      | 0.897     |
| 16          | 256    | 1.743      | 0.932     |
| 16          | 512    | 1.545      | 0.958     |
| 16          | 1024   | 1.283      | 0.976     |
| 32          | 128    | **1.973**  | 0.878     |
| 32          | 256    | 1.822      | 0.926     |
| 32          | 512    | 1.620      | 0.957     |
| 32          | 1024   | 0          | 0         |


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





