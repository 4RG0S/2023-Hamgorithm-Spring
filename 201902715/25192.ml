module StringSet = Set.Make (String)

let one_step (msg : string) (set : StringSet.t) : (StringSet.t * int) = 
  if msg = "ENTER" then StringSet.empty, 0
  else 
    (
      match StringSet.find_opt (msg) (set) with
      | Some _ -> set, 0
      | None -> StringSet.add (msg) (set), 1
    )

let _ = 
  let n = Scanf.scanf "%d\n" (fun x -> x) in
  let reps = Array.init (n) (fun _ -> ()) in
  let ans = [|0|] in
  let _ = Array.fold_left (
    fun a b -> 
      (
        let set, num = one_step (Scanf.scanf "%s\n" (fun x -> x)) (a) in
        let _ = ans.(0) <- ans.(0) + num in
        set 
      )
    ) (StringSet.empty) (reps)
  in
  Format.printf "%d\n" (ans.(0))
