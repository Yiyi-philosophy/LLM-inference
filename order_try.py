execute_gen_len = 32
num_layers = 50
num_gpu_batches = 4
flag_warmup = 0

# 0: normal
# 1: ./
# 2: /=/
# 3: /. 

'''
    if (flag_warmup==0): # 0: normal
        next
    elif (flag_warmup==1): # 1: ./
        next
    elif (flag_warmup==2): # 2: /=/
        next
    else: # 3: /. 
        next
'''
# load_weight(i, j+1, k)
def load_weight( i, j, k, overlap=True):
    # Handle corner cases
    if (flag_warmup==0): # 0: normal
        if j == num_layers:
            j = 0
            i += 1 
            if i == execute_gen_len:
                return
    elif (flag_warmup==1): # 1: ./
        if j == num_layers:
            j = 0
            i += 1 
            if i == execute_gen_len:
                return
    elif (flag_warmup==2): # 2: /=/
        if j == num_layers:
            j = 0
            i += 1 
            if i == execute_gen_len:
                return
    else: # 3: /. 
        if j == num_layers:
            j = 0
            i += 1 
            if i == execute_gen_len:
                return
   
    print("    load_weight:", i, j, k)
    # Load from weight_home to weight_read_buf
        
# load_cache(i, j, k+1)
def load_cache( i, j, k, overlap=True):
    # Handle corner cases
    if (flag_warmup==0): # 0: normal
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
    elif (flag_warmup==1): # 1: ./
        if i == 0:  # prefill, no cache
            return
        if k == num_gpu_batches - 1 - i:
            k = 0
            j += 1
        if j == num_layers:
            j = 0
            i += 1
            if i == num_gpu_batches - 1:
                i = 0
                k = num_gpu_batches - 1 
    elif (flag_warmup==2): # 2: /=/
        if i == 0:  # prefill, no cache
            return
        if k == -1:
            k = num_gpu_batches - 1
            i = i - (num_gpu_batches - 1)
            j += 1
        if j == num_layers:
            j = 0
            i = i - (num_gpu_batches - 1) + 1
            if i == execute_gen_len:
                return
    else: # 3: /. 
        if i == 0:  # prefill, no cache
            return
        if k == num_gpu_batches:
            k = execute_gen_len - i 
            j += 1
        if j == num_layers:
            j = 0
            k = k - 1
            i += 1
            if i == execute_gen_len:
                return
       
    print("    load_cache", i, j, k)
    # Load from cache_home to cache_read_buf

# store_hidden(i, j, k-1)       
def store_hidden( i, j, k):
    if (flag_warmup==0): # 0: normal
        # Handle corner cases
        if k == -1:
            k = num_gpu_batches - 1
            j -= 1
        if j == -1:
            j = num_layers - 1
            i -= 1
            if i == -1:
                return
    elif (flag_warmup==1): # 1: ./
        # Handle corner cases
        if k == -1:
            k = num_gpu_batches - i - 2
            j -= 1
        if j == -1:
            j = num_layers - 1
            k = k + 1
            i -= 1
            if i == -1:
                return
    elif (flag_warmup==2): # 2: /=/
        if k == num_gpu_batches:
            k = 0
            i = i + (num_gpu_batches - 1) + 1
            j -= 1
        if j == -1:
            j = num_layers - 1
            i = i - 1
            # if i == (num_gpu_batches - 1) :
            #     i = i - 1
    else: # 3: /. 
        if k == execute_gen_len - i - 1:
            k = num_gpu_batches - 1
            j -= 1
        if j == -1:
            j = num_layers - 1
            i -= 1
            if i == execute_gen_len - num_gpu_batches:
                i = execute_gen_len - 1
                k = 0

    print("    store_hidden:", i, j, k)
    # Store to hidden states buffers
           
# load_hidden(i, j, k+1)
def load_hidden( i, j, k):
    if (flag_warmup==0): # 0: normal
        # Handle corner cases
        if k == num_gpu_batches:
            k = 0
            j += 1
        if j == num_layers:
            j = 0
            i += 1
            if i == execute_gen_len:
                return
    elif (flag_warmup==1): # 1: ./
        if k == num_gpu_batches - 1 - i:
            k = 0
            j += 1
        if j == num_layers:
            j = 0
            i += 1
            if i == num_gpu_batches - 1:
                i = 0
                k = num_gpu_batches - 1 
    elif (flag_warmup==2): # 2: /=/
        # Handle corner cases
        if k == -1:
            k = num_gpu_batches - 1
            i = i - (num_gpu_batches - 1)
            j += 1
        if j == num_layers:
            j = 0
            i = i - (num_gpu_batches - 1) + 1
            if i == execute_gen_len:
                return
    else: # 3: /. 
        if k == num_gpu_batches:
            k = execute_gen_len - i 
            j += 1
        if j == num_layers:
            j = 0
            k = k - 1
            i += 1
            if i == execute_gen_len:
                return
            
        
    print("    load_hidden:", i, j, k)
    # Load to hidden states buffers

# store_cache(i, j, k-1) 
def store_cache( i, j, k, overlap=True):
    if (flag_warmup==0): # 0: normal
        # Handle corner cases
        if k == -1:
            k = num_gpu_batches - 1
            j -= 1
        if j == -1:
            j = num_layers - 1
            i -= 1
            if i == -1:
                return
        if i == execute_gen_len - 1:  
             # last token, no need to store cache
            # cache_write_buf[j][k].pop()
            return

    elif (flag_warmup==1): # 1: ./
        # Handle corner cases
        if k == -1:
            k = num_gpu_batches - i - 2
            j -= 1
        if j == -1:
            j = num_layers - 1
            k = k + 1
            i -= 1
            if i == -1:
                return
    elif (flag_warmup==2): # 2: /=/
        # Handle corner cases
        if k == num_gpu_batches:
            k = 0
            i = i + (num_gpu_batches - 1) + 1
            j -= 1
        if j == -1:
            j = num_layers - 1
            i = i - 1
            # if i == (num_gpu_batches - 1) :
            #     return
            
        if i == execute_gen_len:  # last token, no need to store cache
            # cache_write_buf[j][k].pop()
            return
    else: # 3: /. 
        if k == execute_gen_len - i - 1:
            k = num_gpu_batches - 1
            j -= 1
        if j == -1:
            j = num_layers - 1
            i -= 1
            if i == execute_gen_len - num_gpu_batches:
                i = execute_gen_len - 1
                k = 0
        
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
                print("    compute_layer:", i, j, k)
                
                store_cache(i, j, k-1)
                # sync()
        # timers("generate").stop()
        
##############################################################
##### order #########
##############################################################

def order_uptri():
   for i in range(0, num_gpu_batches - 1): # 0-3
        # timers("generate").start()
        # for k in range(0,num_gpu_batches - i - 1):
           # update_attention_mask(i, k)
        for j in range(num_layers):
            for k in range(0, num_gpu_batches - i - 1): # 0-3
                print("i,j,k=",i,j,k)
                
                load_weight(i, j+1, k)
                
                load_cache(i, j, k+1)

                store_hidden(i, j, k-1)
                
                load_hidden(i, j, k+1)
                
                # compute_layer(i, j, k)
                print("    compute_layer:", i, j, k)
                store_cache(i, j, k-1)
                # sync()
        # timers("generate").stop()

        
def order_parallelogram():      
    for i in range(0, execute_gen_len-num_gpu_batches+1): # 0-46
        # timers("generate").start()
        # for k in range(num_gpu_batches):
            # update_attention_mask(i, k)
        for j in range(num_layers):
            for k in range(num_gpu_batches-1, -1, -1): # 3-0
                q = i + num_gpu_batches-1 - k # i + 0-3
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
    for i in range(execute_gen_len - num_gpu_batches + 1, execute_gen_len): # 1-3
        #timers("generate").start()
        # for k in range(execute_gen_len - i, num_gpu_batches):
        #     update_attention_mask(i, k)
        for j in range(num_layers):
            for k in range(execute_gen_len - i, num_gpu_batches):
                print("i,j,k=",i,j,k)
                
                load_weight(i, j+1, k)
                
                load_cache(i, j, k+1)
                
                store_hidden(i, j, k-1)
                
                load_hidden(i, j, k+1)
                
                # compute_layer(i, j, k)
                print("    compute_layer:", i, j, k)
                
                store_cache(i, j, k-1)
                # sync()
        #timers("generate").stop()
        
if __name__ == "__main__":
    # 
    flag_warmup = 1
  
    if (flag_warmup == 0):
        print("zigzag")
        order_normal()
    elif (flag_warmup == 1):
        print("./")
        order_uptri()
    elif (flag_warmup == 2):
        print("/=/")
        order_parallelogram()
    else:
        print("/.")
        order_downtri()