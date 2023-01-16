def solve (N, workload):
    final_cont = 0
    cont =0 
    for i, number in enumerate(workload)
        if number > 6:
            cont+=1
        else:
            if cont > final_cont:
                final_cont = cont
            cont=0
    if cont > final_cont:
        final_cont = cont
    return final_cont

N = int(input())
workload = list(map(int, input().split()))

out_ = solve(N, workload)
print (out_)