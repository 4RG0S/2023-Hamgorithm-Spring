let rec combinations n m start result =
  if m = 0 then
    begin
      List.iter (fun num -> Printf.printf "%d " num) (List.rev result);
      Printf.printf "\n";
    end
  else
    begin
      for i = start to n do
        combinations n (m - 1) i (i :: result);
      done;
    end

let () =
  let n, m = Scanf.scanf "%d %d\n" (fun x y -> x, y) in
  combinations n m 1 []
