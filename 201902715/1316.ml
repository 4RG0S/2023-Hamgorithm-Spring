module CharHash = struct
  type t = char
  let equal (i : char) (j : char) = i = j
  let hash i = int_of_char (i) land max_int
end

module CharHashtbl = Hashtbl.Make(CharHash)

let rec remove_duplicate (char_list : char list) : char list = 
  match char_list with
  | [] -> []
  | a :: b :: t -> if a = b then remove_duplicate (b :: t) else a :: remove_duplicate (b :: t)
  | h :: [] -> [h]

let solve (str : string) : int = 
  let hash = CharHashtbl.create (String.length (str)) in
  let rec solve' (char_list : char list) (hash : unit CharHashtbl.t) = 
    match char_list with
    | [] -> ()
    | h :: t -> 
      (
        match CharHashtbl.find_opt (hash) (h) with
        | Some _ -> failwith "failed"
        | None -> CharHashtbl.add (hash) (h) () ; solve' (t) (hash)
      )
  in
  let removed = (remove_duplicate (List.of_seq (String.to_seq str))) in
  try solve' removed (hash) ; 1 with Failure _ -> 0

let _ = 
  let n = Scanf.scanf "%d\n" (fun x -> x) in
  let reps = List.init (n) (fun _ -> ()) in
  let result = List.map (fun _ -> let str = Scanf.scanf "%s\n" (fun x -> x) in solve (str)) (reps) in
  Format.printf "%d" (List.fold_left (fun a b -> a + b) (0) (result))
