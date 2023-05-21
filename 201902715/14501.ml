type time_needed = Time of int

type payment = Payment of int

type schedule = time_needed * payment

let rec read_n_schedules (n : int) (acc : schedule list) : schedule list = 
  match n with
  | 0 -> List.rev (acc)
  | n -> read_n_schedules (n - 1) (((Scanf.scanf "%d %d\n" (fun x y -> Time x, Payment y)) :: acc))

let rec pop_list (li : 'a list) (n : int) = 
  match li with
  | [] -> []
  | h :: t -> 
    (
      if n = 0 then li
      else pop_list (t) (n - 1)
    )

let rec solve (schedules : schedule list) : int = 
  match schedules with
  | [] -> 0
  | (Time t, Payment p) :: others -> 
    (
      let (without_current : int) = solve (others) in
      let (with_current : int) = 
        (
          if t > (List.length (others) + 1) then 0
          else
            (
              solve (pop_list (others) (t - 1)) + p
            )
        )
      in
      max without_current with_current
    )

let _ = 
  let n = Scanf.scanf "%d\n" (fun x -> x) in
  let schedule_list = read_n_schedules (n) ([]) in
  let solution = solve (schedule_list) in
  Format.printf "%d" solution
