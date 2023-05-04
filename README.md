
## Run code
[Git利用git pull命令将远程指定仓库的分支拉取到本地](https://blog.csdn.net/weixin_44312010/article/details/102970413)

Run origin code
``` shell
cd LLM-inference
./test_1.sh
```

Run batch schedule code (in debug)
``` shell
cd LLM-inference
./test_2.sh
```

use this `ipdb.set_trace = lambda: None` instructions to avoid debug
```shell
> /home/dingyiran/FlexGen/flexgen_kj/flex_opt_kj.py(1099)generation_loop_overlap_multi_batch()
   1098                         ipdb.set_trace() #
-> 1099                         self.store_hidden(i, j, k-1)
   1100 

ipdb> ipdb.set_trace = lambda: None
ipdb> c
```