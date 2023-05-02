let count_IOI (num_of_O : int) (li : char list) =
  let rec find_IOIO_patterns_length_list (li : char list) (expected_char : char)
      (next_expected_char : char) (current_length : int) (result : int list) :
      int list =
    match li with
    | [] -> if current_length = 0 then result else result @ [ current_length ]
    | h :: t -> (
        match (expected_char, h) with
        | 'I', 'I' | 'O', 'O' ->
            find_IOIO_patterns_length_list t next_expected_char expected_char
              (current_length + 1) result
        | 'I', 'O' ->
            if current_length = 0 then
              find_IOIO_patterns_length_list t 'I' 'O' 0 result
            else
              find_IOIO_patterns_length_list t 'I' 'O' 0
                (result @ [ current_length ])
        | 'O', 'I' ->
            if current_length = 0 then
              find_IOIO_patterns_length_list li 'I' 'O' 0 result
            else
              find_IOIO_patterns_length_list li 'I' 'O' 0
                (result @ [ current_length ])
        | _, _ -> failwith "invalid input")
  in
  let count_valid (num_of_O : int) (pattern_length : int) : int =
    let ioi_pattern_len =
      if pattern_length mod 2 = 0 then pattern_length - 1 else pattern_length
    in
    let expected_len = (2 * num_of_O) + 1 in
    let diff = (ioi_pattern_len - expected_len) / 2 in
    if diff < 0 then 0 else diff + 1
  in
  List.map (count_valid num_of_O)
    (find_IOIO_patterns_length_list li 'I' 'O' 0 [])

let _ =
  let n = read_int () in
  let _ = read_int () in
  let str = read_line () in
  Format.printf "%d"
    (List.fold_left ( + ) 0 (count_IOI n (List.of_seq (String.to_seq str))))
