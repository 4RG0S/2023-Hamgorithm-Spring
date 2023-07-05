let _ = 
  let n = Scanf.scanf "%d\n" (fun x -> x) in
  let inputs = Array.init n (fun _ -> Scanf.scanf "%d\n" (fun x -> x)) in
  let _ = Array.sort Int.compare inputs in
  let list_size = Array.length inputs in
  let num_to_remove = int_of_float (Float.round ((float_of_int list_size) *. 0.15)) in
  let sum = [|0|] in
  let _ = 
    for i = num_to_remove to list_size - num_to_remove - 1 do
      sum.(0) <- sum.(0) + inputs.(i)
    done
  in
  let result_size = list_size - num_to_remove * 2 in
  let result_sum = sum.(0) in
  let result_avg = (float_of_int result_sum) /. (float_of_int result_size) in
  Format.printf "%d\n" (int_of_float (Float.round result_avg))
