let solve (str : string) : string = 
  let get_two_point (len : int) : (int * int) list = 
    (* 
      결과로 i, j 리스트가 나오면
      문장 1: [0, i]
      문장 2: (i, j]
      문장 3: (j, -1]
    *)
    let x = List.init (len - 1) (fun x -> x) in
    let xy = List.init (len - 1) (fun y -> List.map (fun x -> y, x) (x)) in
    let xy_flat = List.flatten (xy) in
    let rec remove_tril (li : (int * int) list) (acc : (int * int) list) = 
      match li with
      | [] -> List.rev (acc)
      | (i, j) :: t -> 
        (
          if i >= j then remove_tril (t) (acc)
          else remove_tril (t) ((i, j) :: acc)
        )
    in
    remove_tril (xy_flat) ([])
  in
  let get_i_to_j (str : string) (i : int) (j : int) : char list =
    let rec get_i_to_j_rev' (ch_li : char list) (i : int) (j : int) (result : char list) : char list = 
      if i > j then result
      else
        (
          get_i_to_j_rev' (ch_li) (i + 1) (j) (List.nth (ch_li) (i) :: result)
        )
    in
    get_i_to_j_rev' (List.of_seq (String.to_seq (str))) (i) (j) []
  in
  let li = List.map 
    (
      fun (i, j) ->
        (
          String.of_seq (List.to_seq (get_i_to_j (str) (0) (i))) ^
          String.of_seq (List.to_seq (get_i_to_j (str) (i + 1) (j))) ^
          String.of_seq (List.to_seq (get_i_to_j (str) (j + 1) (String.length (str) - 1))) 
        )
    )
    (get_two_point (String.length (str)))
  in
  (* List.iter (fun (x, y) -> Format.printf "%d, %d\n" x y) (get_two_point (String.length (str))); *)
  (* List.iter (fun s -> Format.printf "%s\n" s) (li) ; *)
  List.nth (List.sort (fun a b -> String.compare (a) (b)) (li)) (0)

let _ = 
  let str = Scanf.scanf "%s" (fun x -> x) in
  let solution = solve (str) in 
  Format.printf "%s" solution
