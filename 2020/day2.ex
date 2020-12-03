defmodule M do
  alias Regex

  def parse_line(line) do
    ~r/^(?<l>\d+)-(?<r>\d+) (?<char>\w): (?<password>\w+)$/
    |> Regex.named_captures(line)
    |> Map.update!("r", &String.to_integer/1)
    |> Map.update!("l", &String.to_integer/1)
  end

  def check1(%{"l" => l, "r" => r, "char" => char, "password" => password}) do
    password
    |> String.graphemes()
    |> Enum.reduce(0, &(if &1 == char, do: &2 + 1, else: &2))
    |> (&(&1 >= l and &1 <= r)).()
  end

  def check2(%{"l" => l, "r" => r, "char" => char, "password" => password}) do
    (String.at(password, l - 1) == char) != (String.at(password, r - 1) == char)
  end
end

{:ok, input} = File.read("day2-input")

{count1, count2} =
  input
  |> String.trim()
  |> String.split("\n")
  |> Enum.reduce({0, 0}, fn line, {c1, c2} ->
    data = M.parse_line(line)
    {
      c1 + (if M.check1(data), do: 1, else: 0),
      c2 + (if M.check2(data), do: 1, else: 0)
    }
  end)

IO.inspect(count1, label: "Part 1")
IO.inspect(count2, label: "Part 2")
