module IntTuple = struct
  type t = int * int
  let compare x y = 
    let x_1, x_2 = x in
    let y_1, y_2 = y in
    if x_1 > y_1 then 1
    else if x_1 < y_1 then -1
    else
      (
        if x_2 > y_2 then 1
        else if x_2 < y_2 then -1
        else 0
      )
  let hash (x, y) = 2002 * x + y
  let equal (x, y) (x', y') = x == x' && y == y'
end

module IntTupleHash = Hashtbl.Make (IntTuple)


let read () = 
  let s, e = Scanf.scanf "%d %d\n" (fun a b -> a, b) in
  s-1, e-1

let rec solve (arr : int array) (padlindrome_coord_tbl : bool IntTupleHash.t) (s : int) (e : int) : bool = 
  if s = e then true
  else
    (
      match IntTupleHash.find_opt (padlindrome_coord_tbl) (s, e) with
      | Some ans -> ans
      | None ->
        (
          if arr.(s) <> arr.(e) then false
          else solve (arr) (padlindrome_coord_tbl) (s + 1) (e - 1)
        )
    )

let _ = 
  let n = (Scanf.scanf "%d\n" (fun x -> x)) in
  let arr = Array.init (n) (fun _ -> Scanf.scanf " %d" (fun x -> x)) in
  let palindrome_coord_set : bool IntTupleHash.t = IntTupleHash.create 1000000 in
  let m = (Scanf.scanf "\n%d\n" (fun x -> x)) in
  let reps = Array.init (m) (fun _ -> ()) in
  let result = Array.map (fun _ -> let s, e = read () in let ans = solve (arr) (palindrome_coord_set) (s) (e) in IntTupleHash.add (palindrome_coord_set) (s, e) (ans) ; ans) reps in
  Array.iter (fun e -> Format.printf "%d\n" (if e = true then 1 else 0)) result
