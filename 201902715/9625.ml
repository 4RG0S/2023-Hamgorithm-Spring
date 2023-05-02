let solve n = 
    let rec solve_ n a b = 
        match n with
        | 0 -> (a, b)
        | n -> solve_ (n-1) b (b+a)
    in
    solve_ n 1 0

let _ =
    let n = Scanf.scanf " %d" (fun x -> x) in
    let (a, b) = solve n in
    Printf.printf "%d %d\n" a b