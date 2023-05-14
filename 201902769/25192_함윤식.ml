module StringSet = Set.Make (String)

let rec count (n : int) (set : StringSet.t) : int =
  if n == 0 then 0
  else
    let msg = (Scanf.scanf "%s\n" (fun x -> x)) in
    let set', num = 
      if msg = "ENTER" then StringSet.empty, 0
      else
        match StringSet.find_opt msg set with
        | Some _ -> set, 0
        | None -> StringSet.add msg set, 1
    in
    num + count (n - 1) set'

let () =
  let n = read_int () in
  let ans = count n StringSet.empty in
  Printf.printf "%d\n" ans