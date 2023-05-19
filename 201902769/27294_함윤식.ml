let () =
  let a, b = Scanf.scanf "%d %d\n" (fun x y -> x, y) in

  if (b = 1 || (not (12 <= a && a <= 16))) then Printf.printf "280"
  else
    Printf.printf "320"