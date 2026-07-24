import textwrap
from build import TOPICS, load_entries
from subgroups import SUBGROUPS
from premises import PREMISES, TOPIC_META

entries = load_entries()

def chunk(lst, n=13, min_tail=6):
    """Chunk into groups of ~n, but if the final group would be smaller
    than min_tail, merge it into the previous group instead of leaving a
    stub scene."""
    out = []
    for i in range(0, len(lst), n):
        out.append(lst[i:i+n])
    if len(out) >= 2 and len(out[-1]) < min_tail:
        out[-2].extend(out[-1])
        out.pop()
    return out

# Build ordered scene list: topic -> list of (subgroup_label_or_None, words)
TOPIC_SCENES = {}
for topic, words in TOPICS.items():
    if topic in SUBGROUPS:
        scenes = []
        for label, ws in SUBGROUPS[topic]:
            for c in chunk(ws, 13):
                scenes.append((label, c))
        TOPIC_SCENES[topic] = scenes
    else:
        scenes = [(None, c) for c in chunk(words, 13)]
        TOPIC_SCENES[topic] = scenes

def dump_scaffold():
    for topic in TOPICS:
        print(f"## {topic}  ({len(TOPICS[topic])} words)")
        for i, (label, words) in enumerate(TOPIC_SCENES[topic], 1):
            key = (topic, i)
            has = key in PREMISES
            tag = "OK" if has else "TODO"
            print(f"  [{tag}] Scene {i} ({label}) -- {len(words)} words: {', '.join(words)}")
        print()

def total_scene_count():
    return sum(len(v) for v in TOPIC_SCENES.values())

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'scaffold':
        dump_scaffold()
    elif len(sys.argv) > 1 and sys.argv[1] == 'missing':
        n = 0
        for topic in TOPICS:
            for i, (label, words) in enumerate(TOPIC_SCENES[topic], 1):
                key = (topic, i)
                if key not in PREMISES:
                    n += 1
                    print(f"{topic} | scene {i} | {label} | {', '.join(words)}")
        print(f"\nTOTAL MISSING PREMISES: {n} / {total_scene_count()}")
    else:
        print("total scenes:", total_scene_count())
