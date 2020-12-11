defmodule M do
  def find_pair_multiplication(prev, [value | values]) do
    complement = 2020 - value

    if MapSet.member?(prev, complement) do
      value * complement
    else
      find_pair_multiplication(MapSet.put(prev, value), values)
    end
  end

  def find_triple_multiplication(sums, prev, [value | values]) do
    complement = Map.get(sums, 2020 - value)

    if complement do
      value * complement
    else
      prev
      |> Enum.reduce(sums, &Map.put(&2, &1 + value, &1 * value))
      |> find_triple_multiplication([value | prev], values)
    end
  end
end

expenses =
  "input/day01"
  |> File.read!()
  |> String.trim()
  |> String.split("\n")
  |> Enum.map(&String.to_integer/1)

IO.inspect(M.find_pair_multiplication(MapSet.new(), expenses), label: "Part 1")
IO.inspect(M.find_triple_multiplication(%{}, [], expenses), label: "Part 2")
