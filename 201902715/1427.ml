let _ = 
  let n = read_int () in
  let li = List.of_seq (String.to_seq (Int.to_string n)) in
  Format.printf "%s" (String.of_seq (List.to_seq (List.rev (List.sort Char.compare li))))
