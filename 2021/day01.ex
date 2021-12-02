defmodule Day01 do
  def solve() do
    depths =
      "input/day01"
      |> File.read!()
      |> String.trim()
      |> String.split("\n")
      |> Enum.map(&String.to_integer/1)

    IO.inspect(count_increments(1, depths), label: "Part 1")
    IO.inspect(count_increments(3, depths), label: "Part 2")
  end

  defp count_increments(window_size, xs) do
    [first_window | windows] = window_sums(window_size, xs)

    windows
    |> Enum.reduce({0, first_window}, fn x, {acc, prev} ->
      {acc + if(x > prev, do: 1, else: 0), x}
    end)
    |> elem(0)
  end

  defp window_sums(size, xs) when length(xs) < size, do: []
  defp window_sums(size, [_ | rest] = xs) do
    sum = xs |> Enum.take(size) |> Enum.sum()
    [sum | window_sums(size, rest)]
  end
end

Day01.solve()
