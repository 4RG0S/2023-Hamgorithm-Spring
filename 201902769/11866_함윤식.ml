let () =
  let n, m = Scanf.scanf "%d %d\n" (fun x y -> x, y) in

  let enqueue_range n =
    let queue = Queue.create () in
    for i = 1 to n do
      Queue.add i queue (* 큐에 값을 추가 *)
    done;
    queue
  in
  let q = enqueue_range n in

  let rec circuit count =
    if count = m-1 then
      Queue.pop q
    else
      let temp = Queue.pop q in
      Queue.add temp q;
      circuit (count + 1)
  in

  let print () =
    Printf.printf "<";
    for i = 1 to n do
      if i <> 1 then Printf.printf ", ";
      Printf.printf "%d" (circuit 0)
    done;
    Printf.printf ">\n"
  in
  print ()
