(* 
어떻게 해야 비밀번호를 만들 수 있을까?
비밀번호를 만드는 함수가 만약 주어져있다면

길이 n의 비밀번호를 만들기 위해서는,
어떤 문자 하나를 고르고
그 문자 이후의 문자 뭉치에서 n-1의 비밀번호를 만들어서
그 어떤 문자를 n-1의 비밀번호 리스트의 모든 원소의 앞에 합치면 된다.
*)
let rec make_password (len : int) (li : char list) : string list = 
  let rec get_elem_and_last (li : char list) : (char * char list) list = 
    match li with 
    | [] -> []
    | h :: t -> (h, t) :: (get_elem_and_last t)
  in
  if len = 0 then []
  else if len = 1 then 
    (
      List.map (fun x -> String.make 1 x) li
    )
  else
    (
      List.flatten (
        List.map (
          fun x -> 
            let ch, ch_li = x in 
            List.map (fun y -> (String.make 1 ch) ^ y) (make_password (len - 1) ch_li)
        ) (get_elem_and_last li)
      )
    )

let is_valid (str : string) : bool = 
  let rec is_valid' (ch_li : char list) = 
    match ch_li with 
    | [] -> (0, 0)
    | 'a' :: t 
    | 'e' :: t 
    | 'i' :: t 
    | 'o' :: t 
    | 'u' :: t -> 
      let a, b = is_valid' t in 
      a + 1, b
    | _ :: t ->
      let a, b = is_valid' t in 
      a, b + 1
  in
  let a, b = is_valid' (List.of_seq (String.to_seq str)) in 
  a >= 1 && b >= 2

let _ = 
  let l, c = Scanf.scanf "%d %d" (fun x y -> x, y) in 
  let read_char_list (char_count : int) : char list = 
    let rec read_char_list' (char_count : int) (li : char list) : char list = 
      if char_count = 0 then li
      else (read_char_list' (char_count - 1) (li @ [Scanf.scanf " %c" (fun x -> x)]))
    in
    read_char_list' (char_count) []
  in
  let char_list = read_char_list c in 
  let sorted_char_list = List.sort Char.compare char_list in 
  List.iter (fun x -> if is_valid x then Format.printf "%s\n" x else ()) (make_password l sorted_char_list)
