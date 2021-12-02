defmodule Day01 do
  def solve() do
    depths =
      "input/day01"
      |> File.read!()
      |> (&Regex.scan(~r/\S+/, &1)).()
      |> Enum.map(&String.to_integer(hd(&1)))

    IO.inspect(count_increments(1, depths), label: "Part 1")
    IO.inspect(count_increments(3, depths), label: "Part 2")
  end

  defp count_increments(window_size, xs) do
    xs
    |> Enum.drop(window_size)
    |> Enum.zip(xs)
    |> Enum.reduce(0, fn {current, prev}, count ->
      count + if(current > prev, do: 1, else: 0)
    end)
  end
end

Day01.solve()
