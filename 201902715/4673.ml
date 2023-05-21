module IntHash = struct
  type t = int

  let equal a b = a = b

  let hash a = a
end

module IntHashtbl = Hashtbl.Make (IntHash)

let add_digits (num : int) : int = 
  let str_num = Int.to_string (num) in
  let list_char_num = List.of_seq (String.to_seq str_num) in
  List.fold_left (fun acc elem -> acc + ((int_of_char elem) - (int_of_char '0'))) (0) (list_char_num)

let _ = 
  let (result_hashtbl : unit IntHashtbl.t) = IntHashtbl.create (10000) in
  for i = 1 to 10000 do
    IntHashtbl.add (result_hashtbl) (i + add_digits (i)) ()
  done ;
  for i = 1 to 10000 do
    match IntHashtbl.find_opt (result_hashtbl) (i) with
    | Some _ -> ()
    | None -> Format.printf "%d\n" i
  done
