type time = 
  | Morning
  | Afternoon
  | Evening

let get_time (t : int) : time = 
  match t with
  | t when t <= 11 -> Morning
  | t when t <= 16 -> Afternoon
  | _ -> Evening

let solve (time : time) (alcohol : bool) : int = 
  match time, alcohol with
  | Afternoon, false -> 320
  | _ -> 280

let _ = 
  let t, s = Scanf.scanf "%d %d" (fun x y -> x, y) in
  let time = get_time (t) in 
  let alcohol = s = 1 in
  Format.printf "%d" (solve (time) (alcohol))
