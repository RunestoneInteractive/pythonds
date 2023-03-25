# fix_xrefs
import re
import os
import pdb

xref_dict = {}

for root, dirs, files in os.walk("pretext"):
    for file in files:
        if "toctree" in file:
            continue
        if ".ptx" in file:
            with open(os.path.join(root, file)) as f:
                text = f.read()

                all_xrefs = re.findall(r'<xref ref="((lst-|fig-).*?)".*?>', text)
                for ref in all_xrefs:
                    if target := re.search(
                        r'xml:id="((.*?_.*?)+' + ref[0] + ')"', text
                    ):
                        print(target.groups(1))
                        # pdb.set_trace()
                        xref_dict[ref[0]] = target.groups(1)[0]


for root, dirs, files in os.walk("pretext"):
    for file in files:
        if "toctree" in file:
            continue
        if ".ptx" in file:
            with open(os.path.join(root, file)) as f:
                text = f.read()

            all_xrefs = re.findall(r'<xref ref="((lst-|fig-).*?)".*?>', text)
            for ref in all_xrefs:
                target = ref[0]
                # pdb.set_trace()
                if target in xref_dict:
                    text = text.replace(
                        f'<xref ref="{target}"', f'<xref ref="{xref_dict[target]}"'
                    )

            with open(os.path.join(root, file), "w") as f:
                f.write(text)

# print(xref_dict)
