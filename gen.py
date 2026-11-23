import os,re,sys
from urllib.parse import urlparse
name,folder,intro,anchor=sys.argv[1:5]
cats={}
for l in open('urls.txt'):
    c,n,u=l.strip().split('|'); cats.setdefault(c,[]).append((n,u))
d='docs/'+folder;os.makedirs(d,exist_ok=True)
img=lambda u:f'<img src="https://www.google.com/s2/favicons?domain={urlparse(u).netloc}&sz=32" width="16" height="16" alt="">'
idx=[f'# {name}\n','[← Back to Roadmap](../../README.md)\n',intro+'\n','## Pages\n']
for c,items in cats.items():
    s=re.sub(r'[^a-z0-9]+','-',c.lower()).strip('-')
    open(f'{d}/{s}.md','w').write(f'# {c}\n\n[← Back to Roadmap](../../README.md) · [{name}](README.md)\n\n'+'\n'.join(f'- {img(u)} [{n}]({u})' for n,u in items)+'\n')
    idx.append(f'- [{c}]({s}.md) ({len(items)})')
open(f'{d}/README.md','w').write('\n'.join(idx)+'\n')
r=open('README.md').read();k='### '+anchor
assert k in r
open('README.md','w').write(r.replace(k,f'### {name}\n- [{name}](docs/{folder}/README.md)\n\n'+k))
