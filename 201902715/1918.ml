let rec solve (li : char list) (stack) : unit = 
  let should_pop (cur : char) (stack) : bool = 
    (* top의 우선순위가 cur보다 높거나 같으면 stack에서 빼야 한다. (true) *)
    (* 스택에 아무 것도 없으면 반드시 push (false) *)
    if Stack.is_empty stack then false
    else
      (
        let top = Stack.top stack in
        match cur with
        | '+' | '-' ->
          (
            if top = '(' then false
            else true
          )
        | '*' | '/' ->
          (
            if top = '(' || top = '+' || top = '-' then false
            else true
          )
        | _ -> failwith "[pop] undefined cur"
      )
  in
  match li with
  | [] -> 
    (
      if Stack.is_empty stack then ()
      else
        (
          Format.printf "%c" (Stack.pop (stack)) ; 
          solve [] (stack)
        )
    )
  | '(' :: t -> 
    (
      Stack.push '(' stack ;
      solve (t) (stack)
    )
  | ')' :: t -> 
    (
      let top = Stack.pop (stack) in
      if top = '(' then solve (t) (stack)
      else
        (
          Format.printf "%c" (top) ; 
          solve (')' :: t) (stack)
        )
    )
  | '+' :: t | '-' :: t | '*' :: t | '/' :: t -> 
    (
      match li with
      | op :: t -> 
        (
          if should_pop op stack then
            (
              Format.printf "%c" (Stack.pop (stack)) ;
              solve (op :: t) (stack)
            )
          else
            (
              Stack.push (op) (stack) ; 
              solve (t) (stack)
            )
        )
      | [] -> failwith "undefined"
    )
  | id :: t -> Format.printf "%c" id ; solve (t) (stack)

let _ = 
  let expr_str = read_line () in
  let char_list = List.of_seq (String.to_seq expr_str) in
  let stack = Stack.create () in
  solve (char_list) (stack)
