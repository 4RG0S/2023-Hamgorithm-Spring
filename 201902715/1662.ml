let solve (s : string) : int = 
  let string_list : string list = List.of_seq (Seq.map (fun x -> String.make 1 x) (String.to_seq (s))) in
  let stack : string Stack.t = Stack.create () in
  let rec solve' (string_list : string list) (stack : string Stack.t) : unit = 
    match string_list with
    | [] -> ()
    | num :: "(" :: ")" :: t -> 
      (
        Stack.push "0" (stack) ;
        solve' (t) (stack)
      )
    | num :: "(" :: t -> 
      (
        Stack.push (num) (stack) ;
        Stack.push ("(") (stack) ;
        solve' (t) (stack)
      )
    | ")" :: t -> 
      (
        let num = Stack.pop (stack) in
        let top = Stack.pop (stack) in
        if top = "(" then
          (
            let mul = Stack.pop (stack) in
            Stack.push (string_of_int ((int_of_string mul) * (int_of_string num))) (stack) ;
            solve' (t) (stack)
          )
        else
          (
            Stack.push (string_of_int ((int_of_string num) + (int_of_string top))) (stack) ;
            solve' (")" :: t) (stack)
          )
      )
    | _ :: t ->
      (
        Stack.push ("1") (stack) ;
        solve' (t) (stack)
      )
  in
  solve' (string_list) (stack) ;
  Stack.fold (fun a b -> a + int_of_string (b)) (0) (stack)

let _ = 
  let s : string = read_line () in
  Format.printf "%d" (solve (s))
