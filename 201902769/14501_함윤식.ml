let () =
  let n = read_int () in
  let my_array = Array.make 20 0 in
  for i = 0 to n-1 do
    let a, b = Scanf.scanf "%d %d\n" (fun x y -> x, y) in
    for j = i + a to 19 do
      if my_array.(i) + b > my_array.(j) then my_array.(j) <- my_array.(i) + b
    done
  done;

  print_int my_array.(n);
  