let rec calculate n x y count =
  if y = 0 then count
  else
    if n*n < x*x + y*y then calculate n (x) (y-1) (count+1)
    else if n*n = x*x + y*y then calculate n (x) (y-1) (count)
    else calculate n (x+1) (y) (count)

let () =
  let n = read_int () in
  let n = n / 2 in
  Printf.printf "%d" (((calculate n 0 n 0) + n) * 4)
