module IntTupleHash = struct
  type t = int * int

  let equal (a : t) (b : t) = 
    let a1, a2 = a in
    let b1, b2 = b in
    a1 = b1 && a2 = b2
  
  let hash (e : t) = 
    let e1, e2 = e in
    e1 * 100 + e2
end

module IntTupleHashtbl = Hashtbl.Make (IntTupleHash)

let add_10_position_to_paper (acc : int array) (drawing_paper : unit IntTupleHashtbl.t) ((s, e) : int * int) : unit = 
  for i = s to s + 10 - 1 do
    for j = e to e + 10 - 1 do
      match IntTupleHashtbl.find_opt (drawing_paper) (i, j) with
      | Some _ -> ()
      | None -> IntTupleHashtbl.add (drawing_paper) (i, j) () ; acc.(0) <- acc.(0) + 1
    done
  done

let _ = 
  let (drawing_paper : unit IntTupleHashtbl.t) = IntTupleHashtbl.create (100) in
  let n = Scanf.scanf "%d\n" (fun x -> x) in
  let acc = Array.init (1) (fun _ -> 0) in
  for i = 1 to n do
    let s, e = Scanf.scanf "%d %d\n" (fun x y -> x, y) in
    add_10_position_to_paper (acc) (drawing_paper) (s, e)
  done ;
  Format.printf "%d" (acc.(0))
