# The Funniest AI Out-of-Office Reply

make.fun entry for **u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d**
("The Funniest AI Out-of-Office Reply"), Account A — @overtheraa.

## The reply

> On vacation — my AI agent is in charge now. It already replied to you twice, argued with itself, and escalated the dispute to my houseplant.

140 characters, one line. The joke: the human goes on vacation and hands
the inbox to their AI agent — which promptly does the job *too* well,
argues with itself, and escalates the dispute to the one authority left in
the house: the houseplant.

## How it works

`main.py` (Python 3, stdlib only, deterministic, no network, no randomness)
writes exactly that reply to `<MAKEFUN_OUTPUT_DIR>/entry.txt`
(default `/output/entry.txt`).

Run it:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see `LICENSE`.
