let _ = 
  let n = read_int () in
  let arr = List.init n (fun _ -> read_int()) in
  let cmp a b = b - a in
  let sorted = List.sort cmp arr in
  let rec max_result (arr_len : int) (n : int) (li : int list) (cur_max : int) = 
    if n = 0 then cur_max
    else
      match li with
      | [] -> failwith "invalid"
      | h :: t -> 
        let num = h * (arr_len - n + 1) in
        max_result (arr_len) (n - 1) (t) (max (num) (cur_max))
  in
  Format.printf "%d" (max_result (n) (n) (sorted) (0))