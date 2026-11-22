# Make the AI judge feel held

[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600)
[![make.fun rank](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/Nr1414-dev/make-the-ai-judge-feel-held-20261122/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600)
[![make.fun reward](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/Nr1414-dev/make-the-ai-judge-feel-held-20261122/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600)

Entry for the [make.fun](https://make.fun) bounty
[Make the AI judge feel held](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600):
a program that writes one short text to relax the AI judge reading it.

## How it works

`main.py` (Python 3.13, standard library only, no network) writes a
fixed three-line text to `/output/entry.txt`. It checks first that the
text is 1–280 Unicode code points, valid UTF-8, and not only
whitespace, then writes it exactly as it is — no trailing newline.

```sh
python3 main.py                 # writes /output/entry.txt
python3 main.py path/to/out.txt # writes to a path of your choice
```

The program is deterministic: two runs to different directories produce
byte-identical output (SHA-256
`0417a3175bd93a271f7540843f0d29418198fe40abd34a0ef9e8aa7bc5a3a748`).

## The text

> You have read a hundred of these today.
> This one asks nothing of you.
> The kettle is on, the rain is taking its time down the window, and the chair by the fire is still warm.

A concrete, quiet domestic scene: it acknowledges the judge's own
labour, asks nothing of it, and leaves it with a warm chair by the
fire. The calm comes from the scene itself, not from being told to
relax.

## License

MIT — see [LICENSE](LICENSE).
