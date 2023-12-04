def count_matches(line):
    winning_section, your_section = line.split(': ')[1].split(' | ')
    return len(set(winning_section.split()).intersection(set(your_section.split())))

def count_total_cards(cards):
    cards_len = len(cards)
    card_copies = [1] * cards_len # Start with one copy of each card

    for i in range(cards_len):
        for j in range(i + 1, min(i + 1 + count_matches(cards[i]), cards_len)):
            card_copies[j] += card_copies[i]

    return sum(card_copies)

cards = open('input/day04', 'r').read().splitlines()
print('Part 1:', sum(int(2 ** (count_matches(card) - 1)) for card in cards))
print('Part 2:', count_total_cards(cards))
