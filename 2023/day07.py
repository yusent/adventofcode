from collections import Counter

def parse_line(line):
    hand, bid = line.split()
    return (hand, int(bid))

def p1_sort_key(hand_bid_pair):
    hand = hand_bid_pair[0]
    hand_type = tuple(freq for _, freq in Counter(hand).most_common())
    lex_score = tuple(map(lambda c: '23456789TJQKA'.index(c), hand))
    return hand_type, lex_score

def p2_sort_key(hand_bid_pair):
    hand = hand_bid_pair[0]
    freqs = Counter(hand)

    for card, freq in freqs.most_common():
        if card != 'J':
            freqs[card] += freqs['J']
            del freqs['J']
            break

    hand_type = tuple(freq for _, freq in freqs.most_common())
    lex_score = tuple(map(lambda c: 'J23456789TQKA'.index(c), hand))
    return hand_type, lex_score

def total_winnings(hand_bid_pairs, sort_key):
    hand_bid_pairs = sorted(hand_bid_pairs, key=sort_key)
    return sum(rank * bid for rank, (_, bid) in enumerate(hand_bid_pairs, 1))

hand_bid_pairs = list(map(parse_line, open('input/day07').readlines()))
print('Part 1:', total_winnings(hand_bid_pairs, p1_sort_key))
print('Part 2:', total_winnings(hand_bid_pairs, p2_sort_key))
