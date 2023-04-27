execute_gen_len = 32
num_layers = 50
num_gpu_batches = 4
flag_warmup = 0
# 0: normal
# 1: ./
# 2: /=/
# 3: /. 

def load_weight( i, j, k, overlap=True):
        # Handle corner cases
        if (flag_warmup==0): # 0: normal
            if j == num_layers:
                j = 0
                i += 1 
                if i == execute_gen_len:
                    return
        elif (flag_warmup==1): # 1: ./
            next
        elif (flag_warmup==2): # 2: /=/
            if j == num_layers:
                j = 0
                i += 1 
                if i == execute_gen_len:
                    return
        else: # 3: /. 
            next
            
        
        print("    load_weight:", i, j, k)
        # Load from weight_home to weight_read_buf
        
def load_cache( i, j, k, overlap=True):
        # Handle corner cases
        if i == 0:  # prefill, no cache
            return
        if k == num_gpu_batches:
            k = 0
            j += 1
        if j == num_layers:
            j = 0
            i += 1
            if i == execute_gen_len:
                return
        print("    load_cache", i, j, k)
        # Load from cache_home to cache_read_buf
        
def store_hidden( i, j, k):
        # Handle corner cases
        if k == -1:
            k = num_gpu_batches - 1
            j -= 1
        if j == -1:
            j = num_layers - 1
            i -= 1
            if i == -1:
                return
        print("    store_hidden:", i, j, k)
        # Store to hidden states buffers
        
def load_hidden( i, j, k):
        # Handle corner cases
        if k == num_gpu_batches:
            k = 0
            j += 1
        if j == num_layers:
            j = 0
            i += 1
            if i == execute_gen_len:
                return
        print("    load_hidden:", i, j, k)
        # Load to hidden states buffers
        
def store_cache( i, j, k, overlap=True):
        # Handle corner cases
        if k == -1:
            k = num_gpu_batches - 1
            j -= 1
        if j == -1:
            j = num_layers - 1
            i -= 1
            if i == -1:
                return
        # if i == task.gen_len - 1:  # last token, no need to store cache
        #     cache_write_buf[j][k].pop()
        #     return
        print("    store_cache:", i, j, k)
        # Store cache_write_buf to cache_home
        # Delete cache_write_buf

def order_normal():
    for i in range(execute_gen_len):
        # timers("generate").start()
        # for k in range(num_gpu_batches):
            # update_attention_mask(i, k)
        for j in range(num_layers):
            for k in range(num_gpu_batches):
                print("i,j,k=",i,j,k)
                load_weight(i, j+1, k)
                
                load_cache(i, j, k+1)

                store_hidden(i, j, k-1)
                
                load_hidden(i, j, k+1)
                
                # compute_layer(i, j, k)
                
                store_cache(i, j, k-1)
                # sync()
        # timers("generate").stop()
        
#########################################################################
#########################################################################

def order_uptri():
    for i in range(execute_gen_len):
        # timers("generate").start()
        # for k in range(num_gpu_batches):
            # update_attention_mask(i, k)
        for j in range(num_layers):
            for k in range(num_gpu_batches):
                print("i,j,k=",i,j,k)
                load_weight(i, j+1, k)
                
                load_cache(i, j, k+1)

                store_hidden(i, j, k-1)
                
                load_hidden(i, j, k+1)
                
                # compute_layer(i, j, k)
                
                store_cache(i, j, k-1)
                # sync()
        # timers("generate").stop()

        
def order_parallelogram():
    if (flag_warmup==0): # 0: normal
        print("zigzag")
    elif (flag_warmup==1): # 1: ./
        print("./")
    elif (flag_warmup==2): # 2: /=/
        print("/=/")
    else: # 3: /. 
        print("/.")
        
    for i in range(0, execute_gen_len-num_gpu_batches+1): # 0-46
        # timers("generate").start()
        # for k in range(num_gpu_batches):
            # update_attention_mask(i, k)
        for j in range(num_layers):
            for k in range(num_gpu_batches-1, -1, -1): # 3-0
                q = num_gpu_batches-1 - k
                print("i,j,k=",q,j,k)
                
                # load_weight(i, j+1, k)
                load_weight     (q, j+1, k)
                
                #load_cache(i, j, k+1)
                load_cache      (q+1, j, k-1)

                # store_hidden(i, j, k-1)
                store_hidden    (q-1, j, k+1)
                
                # load_hidden(i, j, k+1)
                load_hidden     (q+1, j, k-1)
                
                # compute_layer(i, j, k)
                print("    compute_layer:", q, j, k)
                
                # store_cache(i, j, k-1)
                store_cache     (q-1, j, k+1)
                # sync()
        # timers("generate").stop()

def order_downtri():
    for i in range(execute_gen_len):
        # timers("generate").start()
        # for k in range(num_gpu_batches):
            # update_attention_mask(i, k)
        for j in range(num_layers):
            for k in range(num_gpu_batches):
                print("i,j,k=",i,j,k)
                load_weight(i, j+1, k)
                
                load_cache(i, j, k+1)

                store_hidden(i, j, k-1)
                
                load_hidden(i, j, k+1)
                
                # compute_layer(i, j, k)
                
                store_cache(i, j, k-1)
                # sync()
        # timers("generate").stop()
        
if __name__ == "__main__":
    # order_normal()
    flag_warmup = 2
    order_parallelogram()