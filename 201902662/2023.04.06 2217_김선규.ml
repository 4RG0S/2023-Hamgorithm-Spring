let _ =
  let n = read_int () in
  let li = List.init n (fun _ -> read_int()) in
  let sortedli = List.sort (fun a b -> if a > b then 1 else -1) li in
  let rec func list length max_value =
    match list with
    | [] -> max_value
    | h :: t -> func t (length-1) (max max_value (h * length))
  in Format.printf "%d" (func sortedli n 0)