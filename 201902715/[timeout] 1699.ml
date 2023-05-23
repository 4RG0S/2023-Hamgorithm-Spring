let get_min_pair (li : int list) = 
  let len = List.length li in
  (* let _ = List.iter (fun e -> Format.printf "%d " e) (li) in
  let _ = Format.printf "\n" in *)
  let n = (len + 1) / 2 in
  let rec get_min_pair' (li : int list) (rev : int list) (trial : int) (current_min : int) = 
    if trial = 0 then current_min
    else
      (
        match li, rev with
        | [], [] -> current_min
        | h1 :: t1, h2 :: t2 -> get_min_pair' (t1) (t2) (trial - 1) (min (h1 + h2) current_min)
        | _ -> failwith ""
      )
  in 
  let min_pair = get_min_pair' (li) (List.rev li) (n) (List.nth li 0 + List.nth li (len - 1)) in
  (* Format.printf "%d\n\n" min_pair ; *)
  min_pair

let is_sq_num (n : int) : bool = 
  let iof = int_of_float (sqrt (float_of_int n)) in
  iof * iof = n

let solve (n : int) : int = 
  let rec solve' (n : int) : int list =
    if n = 1 then [1]
    else if n = 2 then [1; 2]
    else 
      (
        let prev_stage = solve' (n - 1) in
        if is_sq_num (n) then prev_stage @ [1]
        else prev_stage @ [get_min_pair (prev_stage)]
      )
  in
  let solved = solve' (n) in 
  List.nth solved (List.length (solved) - 1)

let _ = 
  let n = read_int () in
  Format.printf "%d" (solve n)
