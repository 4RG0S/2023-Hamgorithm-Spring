module HashString = struct
  type t = string

  let hash (str : t) : int = 
    let rec calc_hash (ch_list : char list) (i : int) (acc : int) : int = 
      match ch_list with
      | [] -> acc
      | h :: t -> calc_hash (t) (i + 1) (int_of_char (h) * i + acc)
    in
    calc_hash (List.of_seq (String.to_seq (str))) (0) (0)
  
  let equal (str1 : t) (str2 : t) = (str1 = str2)
end

module StringHashtbl = Hashtbl.Make (HashString)

let _ = 
  let n, m = Scanf.scanf "%d %d\n" (fun x y -> x, y) in 
  let table = StringHashtbl.create (n) in
  let reps_n = List.init (n) (fun _ -> ()) in
  let reps_m = List.init (m) (fun _ -> ()) in
  let _ = List.iter (fun _ -> StringHashtbl.add (table) (Scanf.scanf "%s\n" (fun x -> x)) (())) (reps_n) in
  let result = Array.init 1 (fun _ -> 0) in
  let _ = List.map (fun _ -> 
    let str = Scanf.scanf "%s\n" (fun str -> str) in
    match StringHashtbl.find_opt (table) (str) with
    | Some _ -> result.(0) <- result.(0) + 1
    | None -> ()
    ) (reps_m)
  in
  Format.printf "%d" result.(0)
