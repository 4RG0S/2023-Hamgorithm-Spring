let print_chli_str (li : char list) : unit = 
  let str = String.of_seq (List.to_seq li) in
  Format.printf "%s\n" str

let calc_difference (str1 : string) (str2 : string) : int = 
  let rec calc_difference' (list_str1 : char list) (list_str2 : char list) : int = 
    match list_str1, list_str2 with
    | [], l -> 0
    | h1 :: t1, h2 :: t2 -> if h1 = h2 then calc_difference' t1 t2 else 1 + calc_difference' t1 t2
    | _ -> failwith "unreachable"
  in
  let rec calc_difference_of_all_combination (list_str1 : char list) (list_str2 : char list) : int = 
    (* let _ = print_chli_str list_str1 in 
    let _ = print_chli_str list_str2 in *)
    let size_of_1 = List.length list_str1 in 
    let size_of_2 = List.length list_str2 in 
    let local = calc_difference' list_str1 list_str2 in 
    if size_of_1 = size_of_2 then local
    else
      (
        match list_str2 with
        | h :: t -> min local (calc_difference_of_all_combination list_str1 t)
        | _ -> failwith "unreachable"
      )
  in
  calc_difference_of_all_combination (List.of_seq (String.to_seq str1)) (List.of_seq (String.to_seq str2))

let _ = 
  let str1, str2 = Scanf.scanf "%s %s" (fun a b -> a, b) in
  let solution = calc_difference str1 str2 in 
  Format.printf "%d" solution
