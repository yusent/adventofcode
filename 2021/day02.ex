defmodule Solution do
  def exec(commands, acc) do
    state = Enum.reduce(commands, acc, &run/2)
    elem(state, 0) * elem(state, 1)
  end

  defp run({"forward", x}, {h, depth}), do: {h + x, depth}
  defp run({"down", x}, {h, depth}), do: {h, depth + x}
  defp run({"up", x}, {h, depth}), do: {h, depth - x}
  defp run({"forward", x}, {h, d, aim}), do: {h + x, d + aim * x, aim}
  defp run({"down", x}, {h, d, aim}), do: {h, d, aim + x}
  defp run({"up", x}, {h, d, aim}), do: {h, d, aim - x}
end

commands =
  "input/day02"
  |> File.read!()
  |> String.trim()
  |> String.split("\n")
  |> Enum.map(fn cmd ->
    [command, steps] = String.split(cmd)
    {command, String.to_integer(steps)}
  end)

IO.inspect(Solution.exec(commands, {0, 0}), label: "Part 1")
IO.inspect(Solution.exec(commands, {0, 0, 0}), label: "Part 2")
