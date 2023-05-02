let solve (a : int) (b : int) : int = 
  let rec solve' (a : int) (b : int) (current_step : int) : int = 
    if (a > b) then -1
    else if (a = b) then current_step
    else
      let selection1 = solve' (2 * a) (b) (current_step + 1) in 
      let selection2 = solve' (a * 10 + 1) (b) (current_step + 1) in 
      match selection1, selection2 with 
      | -1, -1 -> -1
      | selection1, -1 -> selection1
      | -1, selection2 -> selection2
      | selection1, selection2 -> min (selection1) (selection2)
  in
  solve' (a) (b) (1)

let _ = 
  Scanf.scanf "%d %d" (fun a b -> (Format.printf "%d" (solve a b)))
