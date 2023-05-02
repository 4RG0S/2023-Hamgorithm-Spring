# let rec solve (k) (desc_sorted_coin_list) = 
#   match desc_sorted_coin_list with 
#   | [] -> 0
#   | h :: t -> (k / h) + (solve (k mod h) t)

# let _ = 
#   let n, k = Scanf.scanf "%d %d" (fun a b -> a, b) in 
#   let (coin_list) = List.init n (fun _ -> read_int ()) in 
#   let desc_sorted_coin_list = List.rev coin_list in 
#   let answer = solve k desc_sorted_coin_list in 
#   Format.printf "%d" answer

import sys


n, k = map(int, sys.stdin.readline().split())
answer = 0
coin_list = []
for _ in range(n):
    coin_list.append(int(sys.stdin.readline()))
for elem in reversed(coin_list):
    answer += k // elem
    k = k % elem
print(answer)