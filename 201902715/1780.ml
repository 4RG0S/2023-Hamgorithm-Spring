let solve (paper_matrix) (n : int) : (int * int * int) = 
  (* start_coord ~ end_coord가 같은 수로 이루어져 있는가? *)
  let rec is_same_number (paper_matrix : int array array) (num : int) (current_coord : (int * int)) (start_coord : (int * int)) (end_coord : (int * int)) : bool = 
    let i, j = current_coord in 
    let start_i, _ = start_coord in
    let end_i, end_j = end_coord in
    let current = Array.get (Array.get paper_matrix i) j in 
    if (current != num) then false
    else
      (
        if (i = end_i && j = end_j) then
          true
        else
          if (i = end_i) then
            is_same_number (paper_matrix) (num) (start_i, j+1) (start_coord) (end_coord)
          else
            is_same_number (paper_matrix) (num) (i+1, j) (start_coord) (end_coord)
      )
  in
  (* paper_matrix에서 start_coord ~ end_coord까지가 몇 개의 -1, 0, 1 종이로 이루어져 있는가? *)
  let rec solve' (paper_matrix : int array array) (start_coord : (int * int)) (end_coord : (int * int)) : (int * int * int) = 
    let i, j = start_coord in 
    let num = Array.get (Array.get paper_matrix i) j in 
    if (is_same_number paper_matrix num start_coord start_coord end_coord) then
      (
        match num with
        | -1 -> (1, 0, 0)
        | 0 -> (0, 1, 0)
        | 1 -> (0, 0, 1)
        | _ -> failwith "num should be -1 or 0 or 1"
      )
    else
      (
        let start_i, start_j = start_coord in 
        let end_i, _ = end_coord in 
        let step = (end_i - start_i + 1) / 3 in 
        
        let a1, b1, c1 = solve' (paper_matrix) (start_i, start_j) (start_i + step - 1, start_j + step - 1) in
        let a2, b2, c2 = solve' (paper_matrix) (start_i + step, start_j) (start_i + step + step - 1, start_j + step - 1) in
        let a3, b3, c3 = solve' (paper_matrix) (start_i + step + step, start_j) (start_i + step + step + step - 1, start_j + step - 1) in

        let a4, b4, c4 = solve' (paper_matrix) (start_i, start_j + step) (start_i + step - 1, start_j + step + step - 1) in
        let a5, b5, c5 = solve' (paper_matrix) (start_i + step, start_j + step) (start_i + step + step - 1, start_j + step + step - 1) in
        let a6, b6, c6 = solve' (paper_matrix) (start_i + step + step, start_j + step) (start_i + step + step + step - 1, start_j + step + step - 1) in

        let a7, b7, c7 = solve' (paper_matrix) (start_i, start_j + step + step) (start_i + step - 1, start_j + step + step + step - 1) in
        let a8, b8, c8 = solve' (paper_matrix) (start_i + step, start_j + step + step) (start_i + step + step - 1, start_j + step + step + step - 1) in
        let a9, b9, c9 = solve' (paper_matrix) (start_i + step + step, start_j + step + step) (start_i + step + step + step - 1, start_j + step + step + step - 1) in

        (a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9, b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8 + b9, c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9)
      )  
  in
  solve' (paper_matrix) (0, 0) (n - 1, n - 1)

let _ = 
  let n = read_int () in 
  let array = Array.init n (fun _ -> Array.init n (fun _ -> Scanf.scanf " %d" (fun x -> x))) in 
  let a, b, c = solve array n in 
  Format.printf "%d\n%d\n%d\n" a b c
