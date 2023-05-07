let solve (n : int) : int = 
  let arr = Array.init 224 (fun i -> (i + 1) * (i + 1)) in
  let solution = [|4|] in
  for a = 1 to 224 do
    if arr.(a-1) = n then solution.(0) <- min solution.(0) 1
    else ();
    for b = 1 to 224 do
      if arr.(a-1) + arr.(b-1) = n then solution.(0) <- min solution.(0) 2
      else ();
      for c = 1 to 224 do
        if arr.(a-1) + arr.(b-1) + arr.(c-1) = n then solution.(0) <- min solution.(0) 3
        else ();
      done
    done
  done;
  solution.(0)

let _ = 
  let n = read_int () in
  Format.printf "%d" (solve n)
