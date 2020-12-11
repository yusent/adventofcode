defmodule M do
  def parse_passport(section) do
    section
    |> String.split(~r/(\s+|:)/)
    |> Enum.chunk_every(2)
    |> Map.new(fn [k, v] -> {k, v} end)
  end

  def check1(passport) do
    ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    |> Enum.all?(&Map.has_key?(passport, &1))
  end

  def check2(passport) do
    passport
    |> Enum.all?(fn
      {"byr", val} -> in_range?(val, 1920..2002)

      {"iyr", val} -> in_range?(val, 2010..2020)

      {"eyr", val} -> in_range?(val, 2020..2030)

      {"hgt", val} ->
        case Regex.run(~r/^(\d+)(cm|in)$/, val) do
          [_, height, "cm"] ->
            in_range?(height, 150..193)

          [_, height, "in"] ->
            in_range?(height, 59..76)

          _ ->
            false
        end

      {"hcl", val} -> Regex.match?(~r/^#[0-9a-f]{6}$/, val)

      {"ecl", val} -> Regex.match?(~r/^(amb|blu|brn|gry|grn|hzl|oth)$/, val)

      {"pid", val} -> Regex.match?(~r/^\d{9}$/, val)

      _ -> true
    end)
  end

  defp in_range?(val, range) do
    val |> String.to_integer() |> (&Enum.member?(range, &1)).()
  end
end

{count1, count2} =
  "input/day04"
  |> File.read!()
  |> String.trim()
  |> String.split("\n\n")
  |> Enum.reduce({0, 0}, fn section, {c1, c2} ->
    passport = M.parse_passport(section)
    passed_check1 = M.check1(passport)

    {
      c1 + if(passed_check1, do: 1, else: 0),
      c2 + if(passed_check1 and M.check2(passport), do: 1, else: 0)
    }
  end)

IO.inspect(count1, label: "Part 1")
IO.inspect(count2, label: "Part 2")
