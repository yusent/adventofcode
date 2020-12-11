defmodule M do
  def counter(rows = [row | _]) do
    &count(rows, String.length(row), 0, 0, &1, &2)
  end

  defp count(rows, width, col, trees, right, down) do
    case Enum.drop(rows, down) do
      remaining_rows = [row | _] ->
        new_col = rem(col + right, width)
        char = String.at(row, new_col)
        new_trees = trees + if(char == "#", do: 1, else: 0)
        count(remaining_rows, width, new_col, new_trees, right, down)

      _ ->
        trees
    end
  end
end

count =
  "input/day03"
  |> File.read!()
  |> String.trim()
  |> String.split("\n")
  |> M.counter()

part1 = count.(3, 1)
part2 = part1 * count.(1, 1) * count.(5, 1) * count.(7, 1) * count.(1, 2)

IO.inspect(part1, label: "Part 1")
IO.inspect(part2, label: "Part 2")
