let solve box_sizes =
  let n = List.length box_sizes in
  let dp = Array.make n 1 in
  let box_sizes_array = Array.of_list box_sizes in

  for i = 1 to n - 1 do
    for j = 0 to i - 1 do
      if box_sizes_array.(j) < box_sizes_array.(i) then
        dp.(i) <- max dp.(i) (dp.(j) + 1)
    done
  done;

  Array.fold_left max 0 dp


let _ = 
  let n = read_int () in
  let li = List.init n (fun _ -> Scanf.scanf " %d" (fun x -> x)) in
  Format.printf "%d" (solve li)
