❯ yarn run build
yarn run v1.22.19
$ run-p type-check build-only
$ vue-tsc --noEmit -p tsconfig.app.json --composite false
$ vite build
vite v4.4.4 building for production...
✓ 135 modules transformed.
dist/index.html                                      0.42 kB │ gzip:   0.28 kB
dist/assets/PluginReport-2cbf3e5e.css                0.13 kB │ gzip:   0.11 kB
dist/assets/ContentsCard_CoinView-4f84e4e3.css       0.46 kB │ gzip:   0.27 kB
dist/assets/PluginGitReadme-3f6fb3b0.css             0.47 kB │ gzip:   0.27 kB
dist/assets/ContentsCard_StockView-b4a2b8d2.css      0.56 kB │ gzip:   0.28 kB
dist/assets/javascript-fe1e3b76.css                  1.25 kB │ gzip:   0.59 kB
dist/assets/WebsocketView-0ab4ef46.css               1.70 kB │ gzip:   0.52 kB
dist/assets/ReportScreenView-3a59c056.css            1.93 kB │ gzip:   0.52 kB
dist/assets/index-c48e2819.css                     162.31 kB │ gzip:  24.35 kB
dist/assets/tickers_rating_order-c07a9c6e.js         0.50 kB │ gzip:   0.23 kB
dist/assets/GitReadmeView-139fda2b.js                1.99 kB │ gzip:   1.10 kB
dist/assets/MarkdownView-827b2cd6.js                 3.07 kB │ gzip:   1.31 kB
dist/assets/PluginReport-45003615.js                 3.93 kB │ gzip:   1.50 kB
dist/assets/mkdocs_posts_nav-b93e22b2.js             4.37 kB │ gzip:   1.51 kB
dist/assets/ReportScreenView-6053b458.js             4.84 kB │ gzip:   1.68 kB
dist/assets/WebsocketView-7c54b1ba.js                8.44 kB │ gzip:   3.58 kB
dist/assets/index-6e7f8bf5.js                      115.66 kB │ gzip:  44.86 kB
dist/assets/ContentsCard_StockView-cb75c008.js     197.67 kB │ gzip:  16.87 kB
dist/assets/ContentsCard_CoinView-c1e78229.js      244.15 kB │ gzip:  21.57 kB
dist/assets/javascript-5c126d07.js               1,093.31 kB │ gzip: 370.63 kB

(!) Some chunks are larger than 500 kBs after minification. Consider:
- Using dynamic import() to code-split the application
- Use build.rollupOptions.output.manualChunks to improve chunking: https://rollupjs.org/configuration-options/#output-manualchunks
- Adjust chunk size limit for this warning via build.chunkSizeWarningLimit.
✓ built in 9.58s
✨  Done in 10.49s.
  ~/DEV/Web/hg-project-bootstrap              



❯ git add .
❯ git commit -m "commit st-web"
[st-web 4f97c0b] commit st-web
 30 files changed, 803 insertions(+), 450 deletions(-)
 delete mode 100644 assets/ContentsCard_CoinView-3d5b1b1d.css
 create mode 100644 assets/ContentsCard_CoinView-4f84e4e3.css
 rename assets/{ContentsCard_CoinView-e1f5da25.js => ContentsCard_CoinView-c1e78229.js} (98%)
 delete mode 100644 assets/ContentsCard_StockView-9131f773.css
 create mode 100644 assets/ContentsCard_StockView-b4a2b8d2.css
 rename assets/{ContentsCard_StockView-bbb07e17.js => ContentsCard_StockView-cb75c008.js} (98%)
 rename assets/{GitReadmeView-6e5a931f.js => GitReadmeView-139fda2b.js} (86%)
 delete mode 100644 assets/MarkdownView-31d98ad3.js
 create mode 100644 assets/MarkdownView-827b2cd6.js
 create mode 100644 assets/PluginReport-2cbf3e5e.css
 create mode 100644 assets/PluginReport-45003615.js
 delete mode 100644 assets/PluginReport-7ae0c96d.js
 create mode 100644 assets/ReportScreenView-3a59c056.css
 create mode 100644 assets/ReportScreenView-6053b458.js
 create mode 100644 assets/WebsocketView-0ab4ef46.css
 delete mode 100644 assets/WebsocketView-451c7011.js
 create mode 100644 assets/WebsocketView-7c54b1ba.js
 delete mode 100644 assets/WebsocketView-e9292312.css
 rename assets/{index-dcc99063.js => index-6e7f8bf5.js} (68%)
 rename assets/{index-58315931.css => index-c48e2819.css} (99%)
 rename assets/{javascript-f24458bc.js => javascript-5c126d07.js} (99%)
 create mode 100644 assets/tickers_rating_order-c07a9c6e.js
 create mode 100644 md/Gpt/gpt-ChatGPT-(3).md
 create mode 100644 md/Gpt/gpt-Vue-3-script-setup.md
 create mode 100644 md/Gpt/gpt-Vue-3-with-Composition-API.md
 create mode 100644 "md/Gpt/gpt-Vue3-\352\263\204\354\202\260\353\220\234-\355\224\214\353\236\230\352\267\270-\354\204\244\354\240\225.md"
 create mode 100644 "md/Gpt/gpt-Vue3-\354\264\210\352\270\260\355\231\224-\354\275\224\353\223\234.md"
❯ git push origin st-web
Enumerating objects: 35, done.
Counting objects: 100% (35/35), done.
Delta compression using up to 8 threads
Compressing objects: 100% (28/28), done.
Writing objects: 100% (28/28), 486.22 KiB | 9.72 MiB/s, done.
Total 28 (delta 6), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (6/6), completed with 4 local objects.
To https://github.com/d10000usd/d10000usd.github.io.git
   291514c..4f97c0b  st-web -> st-web