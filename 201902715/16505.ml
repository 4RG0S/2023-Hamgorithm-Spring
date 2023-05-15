let pow_positive (a : int) (n : int) : int =
  let rec pow_positive' (a : int) (n : int) (acc : int) : int =
    match n with
    | n when n < 0 -> failwith "undefined"
    | 0 -> 1
    | 1 -> acc * a
    | n -> pow_positive' (a) (n - 1) (acc * a)
  in
  pow_positive' (a) (n) (1)

let rec solve (result_arr : char array array) (n : int) (start_i, start_j : int * int) (end_i, end_j : int * int) : unit = 
  match n with
  | 0 -> ()
  | n -> 
    (
      let mid_offset = (pow_positive (2) (n)) / 2 in
      let (mid_i, mid_j) = (start_i + mid_offset, start_j + mid_offset) in
      for i = mid_i to end_i do
        for j = mid_j to end_j do
          result_arr.(i).(j) <- ' '
        done
      done ;
      begin
        solve (result_arr) (n - 1) (start_i, start_j) (mid_i - 1, mid_j - 1) ;
        solve (result_arr) (n - 1) (mid_i, start_j) (end_i, mid_j - 1) ;
        solve (result_arr) (n - 1) (start_i, mid_j) (mid_i - 1, end_j)
      end
    )

let _ = 
  let n = read_int () in
  let powered = pow_positive (2) (n) in
  let result_arr = Array.init (powered) (fun _ -> Array.init (powered) (fun _ -> '*')) in
  let print_result result_arr n = 
    for i = 1 to powered do
      let result_str = String.of_seq (Array.to_seq result_arr.(i-1)) in
      Format.printf "%s\n" (String.trim (result_str))
    done
  in
  solve (result_arr) (n) (0, 0) (powered - 1, powered - 1) ;
  print_result result_arr n
