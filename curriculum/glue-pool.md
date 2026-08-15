# Shared Glue Pool — function words woven through every batch

**What this is.** The Goethe B1 list contains **326 closed-class function words** with no depictable referent — prepositions, conjunctions, pronouns, determiners, particles, question words, directional adverbs, modal/auxiliary verbs. You cannot draw *zwischen*, *obwohl*, *derselbe* or *ziemlich* the way you can draw a heater or a cat. Forcing standalone scenes out of them produces exactly the un-imaginable texts this method exists to avoid.

So they are **not** a batch. They are a shared pool the text-writer draws from **while writing every other topic's texts**, as connective tissue. A glue word is covered the first time it appears in any finalized text — anywhere in the corpus.

The dividing line is **grammatical class, not abstractness**: every open-class word stays in a topic, even abstract ones (`die Meinung`, `entscheiden`, `wichtig`, `zweifeln` are grounded via situations — that's the whole method). Only closed-class operators pool.

---

## THE RULE

> **It's OKAY to repeat these words. It's NOT okay to leave them out.**

Repetition across many texts is expected and good — that's how glue words actually get learned, in varied context, many times over. The only failure mode is a word that never appears in *any* text.

### Coverage never retires a word

The ledger records one fact per word: *this word has appeared in at least one finalized text*. That is **not** a used-up marker. A covered glue word is exactly as available as an uncovered one — keep reaching for `weil`, `aber`, `schon` in every text where they fit. That repetition is the point, not an inefficiency to optimise away.

The same holds for words you never aimed at. Building sentences out of attested collocations drags pool words in for free: query `Wohnung` and you get `Wohnung und Job`, `in der Wohnung`, `Wohnung ist klein`. Those incidental hits count as coverage and change nothing else.

### Where the tracking lives

Not here. The pool, its functional groups and its coverage state are in the ledger:

```bash
python3 tools/vocab.py glue --open                 # every pool word no text has used yet
python3 tools/vocab.py glue --open --group Frage   # just the question words
python3 tools/vocab.py glue --format md            # all 326, grouped by function
python3 tools/vocab.py status                      # the running X / 326
```

Group names to filter on: `Konjunktionen`, `Bedingungen`, `Präpositionen`, `Richtungs`, `Fragewörter`, `Partikeln`, `Pronomen`, `Modal`, `Alltags`.

**Recompute, don't increment.** `vocab.py scan --apply` re-derives a batch's coverage from the text as it now stands, so a rewrite that deletes a sentence also deletes the coverage that sentence earned. Never hand-increment a count: an increment on a deleted sentence is a word silently marked covered that no text contains.

---

## Dialogue is what drains this pool

Every text is a dialogue, which makes the pool far easier to drain than narration ever did. Whole groups below barely occur in narrative prose but are unavoidable in two-voice speech — reach for them deliberately:

- **Fragewörter** (`was für ein-`, `wieso`, `weshalb`, `woher`, `wie viel`) — one speaker asks, the other answers. A single question-and-answer scene can cover five of these.
- **Modalpartikeln & hedges** (`eben`, `halt`, `doch`, `ja`, `wohl`, `sowieso`, `überhaupt`, `nämlich`, `allerdings`, `zwar`) — near-ungrammatical in written narration, near-obligatory in spoken German. Dialogue is the only place they sound right.
- **Reaktions- & Small-Talk-Wörter** (`klar`, `natürlich`, `nein`, `einverstanden`, `meinetwegen`, `übrigens`, `unbedingt`, `gern/gerne`, `leid tun`, `komisch`) — a listener's turn is built out of these.
- **Modalverben** (`dürfen`, `möchten`, `mögen`, `sollen`) — asking permission, offering, negotiating: all dialogue moves.

## How the writer uses the pool

1. **While drafting:** pull in whatever pool words fit naturally, plus whatever the collocation queries hand you for free. Don't force them, don't avoid them.
2. **While enriching:** run `vocab.py glue --open`, and give a still-missing question word or particle a speaker turn built around it — the cheapest placement there is. A particle that has to be wedged in doesn't go in.
3. **On the last batches:** the stragglers that resist every natural placement get a purpose-built home — folded into a fitting scene, or a short dedicated exchange. Goal: all 326 covered by the end of the corpus, not by the end of any one batch.

_Pool composition: assembled from the former Batches 25 (Logik) + 26 (Grammatik-Glue), plus Batch 24 (Raum & Richtung) dissolved into it (70 prepositions/adverbs; its 10 position verbs + `nah/weit/lang` moved to a real Handlungen scene), plus closed-class stragglers swept out of Batch 21 (18 determiners/degree-particles) and Batch 23 (`einerseits`, `ausschließlich`). Coverage of the full 2886 is preserved — these words moved from scene-assignment to pool-assignment; none were dropped._
