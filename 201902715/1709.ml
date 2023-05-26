let check (i, j: int * int) (r) = (i * i + j * j < r * r) && ((i + 1) * (i + 1) + (j + 1) * (j + 1) > r * r)

let solve (r) = 
  let rec solve' (r) (i, j) (acc) = 
    if check (i, j) (r) then
      (
        if check (i, j + 1) (r) then
          solve' (r) (i, j + 1) (acc + 1)
        else if check (i - 1, j) (r) then
          solve' (r) (i - 1, j) (acc + 1)
        else
          solve' (r) (i - 1, j + 1) (acc + 1)
      )
    else acc
  in
  solve' (r) (r - 1, 0) 0

let _ = 
  let n = read_int () in 
  let r = n / 2 in
  Format.printf "%d" (solve r * 4)
