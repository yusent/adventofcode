defmodule Day01 do
  def solve() do
    depths =
      "input/day01"
      |> File.read!()
      |> String.split("\n", trim: true)
      |> Enum.map(&String.to_integer/1)

    IO.inspect(count_increments(1, depths), label: "Part 1")
    IO.inspect(count_increments(3, depths), label: "Part 2")
  end

  defp count_increments(window_size, xs) do
    xs
    |> Enum.drop(window_size)
    |> Enum.zip(xs)
    |> Enum.count(fn {current, prev} -> current > prev end)
  end
end

Day01.solve()
